from enum import Enum
from mAP.iou import iou


class Classification(Enum):
    FALSE_POSITIVE = 0
    TRUE_POSITIVE = 1


class Classify:

    @staticmethod
    def classify(detection, ground_truths, iou_threshold=0.5):
        """
        classify detection as TP, FP or FN

        :param detection:
        :param ground_truths:
        :param iou_threshold:
        :return:  classification, 'unused' ground_truths
        """

        ious = iou(detection, ground_truths)
        idxs = ious >= iou_threshold
        if idxs == 1:
            if detection.class_name == ground_truths[idxs[0]].class_name:
                return Classification.TRUE_POSITIVE, ground_truths[~idxs]
