import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument('--no_animation', help="If true, no animation is shown.", action="store_true")
args = parser.parse_args()

if not args.no_animation:
  import cv2

# create a list with all the classes in the ground-truth
for tmp_file in glob.glob('ground-truth/*.txt'):
  print(tmp_file)


# iterate through each of the classes
