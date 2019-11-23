

from .context import *

def test_ground_truth_update():

    map = MeanAveragePrecision()

    map.add_detection_for_image()