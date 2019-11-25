from enum import Enum
from mean_average_precision.iou import iou
import numpy as np


class Classification(Enum):
    TRUE_POSITIVE = 1
    FALSE_POSITIVE = 2


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
        classification = Classification.FALSE_POSITIVE

        ious = iou(detection, ground_truths)
        high_enough_ious = ious >= iou_threshold
        matching_class_ids = np.array([detection.class_id == ground_truth.class_id for ground_truth in ground_truths])

        matching_ground_truths = np.array(list(zip(ious, ground_truths)))[high_enough_ious & matching_class_ids]
        remaining_ground_truths = ground_truths[~ (high_enough_ious & matching_class_ids)]

        matching_ground_truths.tolist().sort(key=lambda x: x[0], reverse=True)
        if len(matching_ground_truths) == 1:
            classification = Classification.TRUE_POSITIVE
        elif len(matching_ground_truths) > 1:
            classification = Classification.TRUE_POSITIVE
            for i in range(1, len(matching_ground_truths)):
                remaining_ground_truths = np.concatenate((remaining_ground_truths, np.array([
                    matching_ground_truths[i][1]
                ])))

        return classification, remaining_ground_truths
