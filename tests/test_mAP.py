from .context import *

HERE = os.path.dirname(os.path.realpath(__file__))
GT_PATH = os.path.join(HERE, '../input/ground-truth')
DT_PATH = os.path.join(HERE, '../input/detection-results')

import glob
import os
from collections import defaultdict


def _get_from_file(filename):
    file_id = os.path.basename(filename).split('.txt', 1)[0]
    elements = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            splits = line.split()
            if len(splits) == 5:
                elements += [GroundTruth(file_id=file_id,
                                         class_idx=splits[0],
                                         bounding_box=BoundingBox(
                                             x1=int(splits[1]),
                                             y1=int(splits[2]),
                                             x2=int(splits[3]),
                                             y2=int(splits[4])
                                         ))]

            elif len(splits) == 6:
                elements += [Detection(file_id=file_id,
                                       class_idx=splits[0],
                                       confidence=float(splits[1]),
                                       bounding_box=BoundingBox(
                                           x1=int(splits[2]),
                                           y1=int(splits[3]),
                                           x2=int(splits[4]),
                                           y2=int(splits[5])
                                       ))]

    return elements


def _get_from_file_list(file_list):
    elements = []
    for filename in file_list:
        elements += _get_from_file(filename)
    return elements


def test_ground_truth_update():
    map = MeanAveragePrecision()

    ground_truths = _get_from_file_list(glob.glob(GT_PATH + '/*.txt'))
    detections = _get_from_file_list(glob.glob(DT_PATH + '/*.txt'))

    ground_truths.sort(key=lambda o: o.file_id)
    detections.sort(key=lambda o: o.file_id)

    gts = defaultdict(list)
    for gt in ground_truths:
        gts[gt.file_id].append(gt)

    dts = defaultdict(list)
    for dt in detections:
        dts[dt.file_id].append(dt)

    for file_id, detections_for_file in dts.items():
        ground_truths_for_file = gts[file_id]

        print(detections_for_file)
        print(ground_truths_for_file)
        print()

        map.add_detections_for_image(detections_for_file, ground_truths_for_file)
