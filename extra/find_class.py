import sys
import os
import glob

if len(sys.argv) != 3:
  print("Error: wrong format.\nUsage: python find_class.py [class_name] [path]")
  sys.exit(0)

searching_class_name = sys.argv[1]
path = sys.argv[2]

os.chdir(path)

# iterate through the text files
for txt_file in glob.glob('*.txt'):
  # open txt file lines to a list
  with open(txt_file) as f:
    content = f.readlines()
  # remove whitespace characters like `\n` at the end of each line
  content = [x.strip() for x in content]
  # go through each line of eache file
  for line in content:
    class_name = line.split()[0]
    if class_name == searching_class_name:
      print(txt_file)
