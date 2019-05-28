import sys
import os
import glob

# make sure that the cwd() in the beginning is the location of the python script (so that every path makes sense)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

if len(sys.argv) != 2:
  print("Error: wrong format.\nUsage: python find_class.py [class_name]")
  sys.exit(0)

searching_class_name = sys.argv[1]

def find_class(class_name):
  file_list = glob.glob('*.txt')
  file_list.sort()
  # iterate through the text files
  file_found = False
  for txt_file in file_list:
    # open txt file lines to a list
    with open(txt_file) as f:
      content = f.readlines()
    # remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    # go through each line of eache file
    for line in content:
      class_name = line.split()[0]
      if class_name == searching_class_name:
        print(" " + txt_file)
        file_found = True
        break
  if not file_found:
    print(" No file found with that class")

parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
parent_path = os.path.abspath(os.path.join(parent_path, os.pardir))
GT_PATH = os.path.join(parent_path, 'input','ground-truth')
DR_PATH = os.path.join(parent_path, 'input','detection-results')

print("ground-truth folder:")
os.chdir(GT_PATH)
find_class(searching_class_name)
print("detection-results folder:")
os.chdir(DR_PATH)
find_class(searching_class_name)
