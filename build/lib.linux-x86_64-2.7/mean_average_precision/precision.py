from mean_average_precision.classify import Classification
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

        true_positives = np.array([1 if detection.classification == Classification.TRUE_POSITIVE else 0
                                   for detection in detections])

        false_positives = np.array([1 if detection.classification == Classification.FALSE_POSITIVE else 0
                                    for detection in detections])

        return Precision.from_true_positives_and_false_positives(true_positives, false_positives)

    @staticmethod
    def from_true_positives_and_false_positives(true_positives, false_positives):
        true_positives_cumulative = true_positives.cumsum()
        false_positives_cumulative = false_positives.cumsum()

        return true_positives_cumulative / (true_positives_cumulative + false_positives_cumulative)