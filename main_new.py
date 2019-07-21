""" This is the main function, the one you must run to evaluate your object detector. """
from __future__ import print_function
import argparse
import os

from code.modules import load_data

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--no-animation', help="No images are shown.", action="store_true")
PARSER.add_argument('--no-plot', help="No plots are shown.", action="store_true")
PARSER.add_argument('--quiet', help="Minimalistic console output.", action="store_true")
PARSER.add_argument('--set-iou', default=0.5, type=float, help="Set IoU threshold for all classes.")
# You can ignore some classes so that they do not affect the score. E.g.:
##  python main.py --ignore-classes person
##   or
##  python main.py --ignore-classes person car
PARSER.add_argument('--ignore-classes', nargs='+', type=str, help="Ignore a list of classes.")
# You can also set a specific IoU for some classes. E.g.:
##  python main.py --set-iou-specific-class person 0.7
##   or
##  python main.py --set-iou-specific-class person 0.7 car 0.8
PARSER.add_argument('--set-iou-specific-class',
                    nargs='+', type=str,
                    help="Set IoU threshold for a specific class.")
ARGS = PARSER.parse_args()


if __name__ == '__main__':
    # set the current working directory to this script's location
    #  so that opening relative paths will work
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #print(os.getcwd())

    # Step 1: Load data
    ## 1.1. load ground-truth
    load_data.load_ground_truth()
    ## 1.2. load detection-results
