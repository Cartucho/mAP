from mAP.classify import Classification
import numpy as np


class Precision:

    @staticmethod
    def compute(detections):
        """
        tp
        -------
        tp + fp
        :param detections:
        :return:
        """
        # this will ensure the list of detections is sorted
        # list.sort is a stable sort - so it should not hurt when list is already sorted)
        detections.sort(key=lambda d: d.confidence, reverse=True)

        true_positives = np.array([1 if detection.classification == Classification.TRUE_POSITIVE else 0
                                   for detection in detections])

        false_positives = np.array([1 if detection.classification == Classification.FALSE_POSITIVE else 0
                                    for detection in detections])

        true_positives_cumulative = true_positives.cumsum()
        false_positives_cumulative = false_positives.cumsum()

        return true_positives_cumulative / (true_positives_cumulative + false_positives_cumulative)
