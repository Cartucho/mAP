import glob
import json
import os
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--no_animation', help="If true, no animation is shown.", action="store_true")
parser.add_argument('--no_plot', help="If true, no plot is shown.", action="store_true")
args = parser.parse_args()

if not args.no_animation:
  import cv2

if not args.no_plot:
  import matplotlib.pyplot as plt

MINOVERLAP = 0.5 # value defined in the PASCAL VOC2012 challenge


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
tmp_files_path = "tmp_files"
if not os.path.exists(tmp_files_path):
  os.makedirs(tmp_files_path)

"""
 Ground-Truth
   Load each of the ground-truth files into a temporary ".json" file.
   Create a list with all the class names present in the ground-truth (unique_classes).
"""
# get a list with the ground-truth files
ground_truth_files_list = glob.glob('ground-truth/*.txt')
ground_truth_files_list.sort()

unique_classes = set([])
counter_per_class = {}
for txt_file in ground_truth_files_list:
  #print(txt_file)
  lines = file_lines_to_list(txt_file)
  # create ground-truth dictionary
  bounding_boxes = []
  for line in lines:
    class_name, left, top, right, bottom = line.split()
    bbox = left + " " + top + " " + right + " " +bottom
    bounding_boxes.append({"class_name":class_name, "bbox":bbox, "used":False})
    # count that object
    if class_name in counter_per_class:
      counter_per_class[class_name] += 1
    else:
      # if class didn't exist yet
      counter_per_class[class_name] = 1
      unique_classes.add(class_name)
  # dump bounding_boxes into a ".json" file
  file_id = txt_file.split(".txt",1)[0]
  file_id = file_id.split("/",1)[1]
  with open(tmp_files_path + "/" + file_id + "_ground_truth.json", 'wb') as outfile:
    json.dump(bounding_boxes, outfile)

# let's sort the classes alphabetically
unique_classes = sorted(unique_classes)
#print(unique_classes)
#print(counter_per_class)

"""
 Predicted
   Load each of the predicted files into a temporary ".json" file.
"""
# get a list with the predicted files
predicted_files_list = glob.glob('predicted/*.txt')
predicted_files_list.sort()

for class_name in unique_classes:
  bounding_boxes = []
  for txt_file in predicted_files_list:
    #print txt_file
    lines = file_lines_to_list(txt_file)
    for line in lines:
      line_class_name, confidence, left, top, right, bottom = line.split()
      if line_class_name == class_name:
        #print("match")
        file_id = txt_file.split(".txt",1)[0]
        file_id = file_id.split("/",1)[1]
        bbox = left + " " + top + " " + right + " " +bottom
        bounding_boxes.append({"confidence":confidence, "file_id":file_id, "bbox":bbox})
        #print(bounding_boxes)
  # sort predictions by decreasing confidence
  bounding_boxes.sort(key=lambda x:x['confidence'], reverse=True)
  with open(tmp_files_path + "/" + class_name + "_predictions.json", 'wb') as outfile:
    json.dump(bounding_boxes, outfile)

"""
 Calculate the AP for each class
"""
sum_AP = 0.0
for class_name in unique_classes[1:]: # remove the [1:] !!!
  """
   Load predictions of that class
  """
  predictions_file = tmp_files_path + "/" + class_name + "_predictions.json"
  predictions_data = json.load(open(predictions_file))
  if not predictions_data:
    # no predictions found for that class
    print(class_name + " AP = 0.00")
    continue
  """
   Assign predictions to ground truth objects
  """
  nd = len(predictions_data)
  tp = [0] * nd # creates an array of zeros of size nd
  fp = [0] * nd
  for idx, prediction in enumerate(predictions_data):
    file_id = prediction["file_id"]
    # find ground truth image
    ground_truth_img = glob.glob1("images", file_id + "*")
    #tifCounter = len(glob.glob1(myPath,"*.tif"))
    if len(ground_truth_img) == 0:
      print("Error: unrecognized image " + file_id)
      sys.exit(0)
    elif len(ground_truth_img) > 1:
      print("Error: multiple image " + file_id)
      sys.exit(0)
    # assign prediction to ground truth object if any
    #   open ground-truth with that file_id
    gt_file = tmp_files_path + "/" + file_id + "_ground_truth.json"
    ground_truth_data = json.load(open(gt_file))
    ovmax = -1
    gt_match = -1
    for obj in ground_truth_data:
      # look for a class_name match
      if obj["class_name"] == class_name:
        bb = [ float(x) for x in prediction["bbox"].split() ]
        bbgt = [ float(x) for x in obj["bbox"].split() ]
        bi = [max(bb[0],bbgt[0]), max(bb[1],bbgt[1]), min(bb[2],bbgt[2]), min(bb[3],bbgt[3])]
        iw = bi[2] - bi[0] + 1
        ih = bi[3] - bi[1] + 1
        if iw > 0 and ih > 0:
          # compute overlap = area of intersection / area of union
          ua = (bb[2] - bb[0] + 1) * (bb[3] - bb[1] + 1) + (bbgt[2] - bbgt[0]
                  + 1) * (bbgt[3] - bbgt[1] + 1) - iw * ih
          ov = iw * ih / ua
          if ov > ovmax:
            ovmax = ov
            gt_match = obj

    # assign prediction as true positive or false positive
    if ovmax >= MINOVERLAP:
      if not bool(gt_match["used"]):
        # true positive
        tp[idx] = 1
        gt_match["used"] = True
        # update the ".json" file
        with open(gt_file, 'wb') as f:
            f.write(json.dumps(ground_truth_data))
      else:
        # false positive (multiple detection)
        fp[idx] = 1
    else:
      # false positive
      fp[idx] = 1

  #print(tp)
  # compute precision/recall
  cumsum = 0
  for idx, val in enumerate(fp):
    fp[idx] += cumsum
    cumsum += val
  cumsum = 0
  for idx, val in enumerate(tp):
    tp[idx] += cumsum
    cumsum += val
  #print(tp)
  rec = tp[:]
  for idx, val in enumerate(tp):
    rec[idx] = float(tp[idx]) / counter_per_class[class_name]
  #print(rec)
  prec = tp[:]
  for idx, val in enumerate(tp):
    prec[idx] = float(tp[idx]) / (fp[idx] + tp[idx])
  #print(prec)

  ap = voc_ap(rec, prec)
  sum_AP += ap
  print(class_name + " AP = %.4f" % ap)

  if not args.no_plot:
    plt.plot(rec, prec, '-o')
    # set window title
    fig = plt.gcf() # gcf - get current figure
    fig.canvas.set_window_title('AP - Average Precision')
    # set plot title
    plt.title('class: ' + class_name + ", AP = %.4f" % ap)
    #plt.suptitle('This is a somewhat long figure title', fontsize=16)
    # set axis titles
    plt.xlabel('recall')
    plt.ylabel('precision')
    # optional - set axes
    axes = plt.gca() # gca - get current axes
    axes.set_xlim([0.0,1.0])
    axes.set_ylim([0.0,1.05])
    # wait for button to be pressed
    while not plt.waitforbuttonpress(): pass
    plt.cla() # clear axes for next plot

mAP = sum_AP / len(unique_classes)
print("mAP = " + str(mAP))

# remove the tmp_files directory
shutil.rmtree(tmp_files_path)
