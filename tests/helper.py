import os
from .context import *

HERE = os.path.dirname(os.path.realpath(__file__))
GT_PATH = os.path.join(HERE, '../input/ground-truth')
DT_PATH = os.path.join(HERE, '../input/detection-results')



def get_from_file(filename):
    file_id = os.path.basename(filename).split('.txt', 1)[0]
    elements = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            splits = line.split()
            if len(splits) == 5:
                elements += [GroundTruth(file_id=file_id,
                                         class_id=splits[0],
                                         bounding_box=BoundingBox(
                                             x1=int(splits[1]),
                                             y1=int(splits[2]),
                                             x2=int(splits[3]),
                                             y2=int(splits[4])
                                         ))]

            elif len(splits) == 6:
                elements += [Detection(file_id=file_id,
                                       class_id=splits[0],
                                       confidence=float(splits[1]),
                                       bounding_box=BoundingBox(
                                           x1=int(splits[2]),
                                           y1=int(splits[3]),
                                           x2=int(splits[4]),
                                           y2=int(splits[5])
                                       ))]

    return elements


def get_from_file_list(file_list):
    elements = []
    for filename in file_list:
        elements += get_from_file(filename)
    return elements
