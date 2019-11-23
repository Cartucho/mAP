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


        classification = Classification.FALSE_POSITIVE
        remaining_ground_truths = []
        if len(idxs) == 1:
            if detection.class_name == ground_truths[idxs[0]].class_name:
                classification = Classification.TRUE_POSITIVE
                remaining_ground_truths = ground_truths[~idxs]
        elif len(idxs) == 0:
            # TODO
            pass

        return classification, remaining_ground_truths
