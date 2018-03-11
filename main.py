import argparse
import glob
import json
import os

MINOVERLAP = 0.5 # value defined in the PASCAL VOC2012 challenge

parser = argparse.ArgumentParser()
parser.add_argument('--no_animation', help="If true, no animation is shown.", action="store_true")
args = parser.parse_args()

if not args.no_animation:
  import cv2


def voc_ap(rec, prec):
  """
  --- Official matlab code VOC2012---
  mrec=[0 ; rec ; 1];
  mpre=[0 ; prec ; 0];
  for i=numel(mpre)-1:-1:1
      mpre(i)=max(mpre(i),mpre(i+1));
  end
  i=find(mrec(2:end)~=mrec(1:end-1))+1;
  ap=sum((mrec(i)-mrec(i-1)).*mpre(i));
  """
  rec.insert(0, 0.0) # insert 0.0 at begining of list
  rec.append(1.0) # insert 1.0 at end of list
  mrec = rec[:]
  prec.insert(0, 0.0) # insert 0.0 at begining of list
  prec.append(0.0) # insert 1.0 at end of list
  mpre = prec[:]
  # matlab indexes start in 1 but python in 0, so I have to do:
  #   range(start=(len(mpre) - 2), end=0, step=-1)
  # also the python function range excludes the end, resulting in:
  #   range(start=(len(mpre) - 2), end=-1, step=-1)
  for i in range(len(mpre)-2, -1, -1):
    mpre[i] = max(mpre[i], mpre[i+1])
  # matlab: i=find(mrec(2:end)~=mrec(1:end-1))+1;
  ind = []
  for ind_1 in range(1, len(mrec)):
    if mrec[ind_1] != mrec[ind_1-1]:
      ind.append(ind_1) # if it was matlab would be ind_1 + 1
  print(ind)
  # matlab: ap=sum((mrec(i)-mrec(i-1)).*mpre(i));
  ap = 0.0
  for i in ind:
    ap += ((mrec[i]-mrec[i-1])*mpre[i])
  return ap


def file_lines_to_list(path):
  # open txt file lines to a list
  with open(path) as f:
    content = f.readlines()
  # remove whitespace characters like `\n` at the end of each line
  content = [x.strip() for x in content]
  return content


# create the "tmp_files" dir if it doesn't exist already
tmp_files_name = "tmp_files"
if not os.path.exists(tmp_files_name):
  os.makedirs(tmp_files_name)

# get a list with the ground-truth files
ground_truth_files_list = glob.glob('ground-truth/*.txt')
ground_truth_files_list.sort()

"""
 Load each of the ground-truth files into a temporary ".json" file.
 Create a list with all the class names present in the ground-truth (unique_classes).
"""
unique_classes = set([])
for txt_file in ground_truth_files_list:
  #print(txt_file)
  lines = file_lines_to_list(txt_file)
  # create ground-truth dictionary
  bounding_boxes = []
  for line in lines:
    class_name, left, top, right, bottom = line.split()
    bbox = left + " " + top + " " + right + " " +bottom
    bounding_boxes.append({"class_name":class_name, "bbox":bbox, "used":False})
    # since unique_classes is a set() it only adds if not already present
    unique_classes.add(class_name)
  # dump bounding_boxes into a ".json" file
  file_id = txt_file.split(".txt",1)[0]
  file_id = file_id.split("/",1)[1]
  with open(tmp_files_name + "/" + file_id + "_ground_truth.json", 'wb') as outfile:
    json.dump(bounding_boxes, outfile)

# let's sort the classes alphabetically
unique_classes = sorted(unique_classes)
#print(unique_classes)

# get a list with the predicted files
predicted_files_list = glob.glob('predicted/*.txt')
predicted_files_list.sort()

for class_name in unique_classes:
  bounding_boxes = []
  for txt_file in predicted_files_list:
    print txt_file
    lines = file_lines_to_list(txt_file)
    for line in lines:
      line_class_name, confidence, left, top, right, bottom = line.split()
      if line_class_name == class_name:
        print("match")
        file_id = txt_file.split(".txt",1)[0]
        file_id = file_id.split("/",1)[1]
        bbox = left + " " + top + " " + right + " " +bottom
        bounding_boxes.append({"confidence":confidence, "file_id":file_id, "bbox":bbox})
        print(bounding_boxes)
  # sort predictions by decreasing confidence
  bounding_boxes.sort(key=lambda x:x['confidence'], reverse=True)
  with open(tmp_files_name + "/" + class_name + "_predictions.json", 'wb') as outfile:
    json.dump(bounding_boxes, outfile)


###
import sys
sys.exit()
###

"""
 Calculate the AP for each class
"""
for class_name in unique_classes:
  print(class_name)

  """
   Assign predictions to ground truth objects
  """
  # find ground truth image
  # assign prediction to ground truth object if any
  # compute overlap = area of intersection / area of union
  # assign detection as true positive or false positive
  #   true positive
  #   false positive (multiple detection)
  #   false positive

  # compute precision/recall
  """
  fp=cumsum(fp);
  tp=cumsum(tp);
  rec=tp/npos;
  prec=tp./(fp+tp);
  """

  """
  rec = []
  rec.append(0.1)
  rec.append(0.1)
  rec.append(1.0)
  rec.append(0.5)
  prec = []
  prec.append(0.2)
  prec.append(0.3)
  prec.append(1.0)
  prec.append(0.8)
  """

  #ap = voc_ap(rec, prec)
  #print(ap)

  """
  --- Official matlab code VOC2012---
  if draw
      % plot precision/recall
      plot(rec,prec,'-');
      grid;
      xlabel 'recall'
      ylabel 'precision'
      title(sprintf('class: %s, subset: %s, AP = %.3f',cls,VOCopts.testset,ap));
  end
  """

# remove the tmp_files directory
os.rmdir(tmp_files_name)
