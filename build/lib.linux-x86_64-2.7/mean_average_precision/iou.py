import numpy as np


def iou(detection, ground_truths):
    """
    compute intersection over union for every ground_truth object in ground_truths list
    :param detection:
    :param ground_truths: list
    :return: list
    """
    return np.array([_bbox_iou(detection.bounding_box, ground_truth.bounding_box)
                     for ground_truth in ground_truths])


def _bbox_iou(box1, box2):
    """
    Returns the IoU of two bounding boxes
    Source https://github.com/eriklindernoren/PyTorch-YOLOv3
    :param x:
    :return:
    """


    # Get the coordinates of bounding boxes
    b1_x1, b1_y1, b1_x2, b1_y2 = box1.x1, box1.y1, box1.x2, box1.y2
    b2_x1, b2_y1, b2_x2, b2_y2 = box2.x1, box2.y1, box2.x2, box2.y2

    # get the corrdinates of the intersection rectangle
    inter_rect_x1 = max(b1_x1, b2_x1)
    inter_rect_y1 = max(b1_y1, b2_y1)
    inter_rect_x2 = min(b1_x2, b2_x2)
    inter_rect_y2 = min(b1_y2, b2_y2)

    # Intersection area
    inter_area = max(inter_rect_x2 - inter_rect_x1 + 1, 0) * max(inter_rect_y2 - inter_rect_y1 + 1, 0)

    # Union Area
    b1_area = (b1_x2 - b1_x1 + 1) * (b1_y2 - b1_y1 + 1)
    b2_area = (b2_x2 - b2_x1 + 1) * (b2_y2 - b2_y1 + 1)

    iou = inter_area / (b1_area + b2_area - inter_area + 1e-16)

    return iou
