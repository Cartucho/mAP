from mean_average_precision.classify import Classification
import numpy as np


class Recall:

    @staticmethod
    def compute(detections, number_of_ground_truth_objects_for_class):
        """
        tp
        -------
        number_of_ground_truth_objects_for_class
        :param detections:
        :return:
        """
        assert len(set([d.class_id for d in detections])) <= 1

        # this will ensure the list of detections is sorted
        # list.sort is a stable sort - so it should not hurt when list is already sorted)
        detections.sort(key=lambda d: d.confidence, reverse=True)

        true_positives = np.array([1 if detection.classification == Classification.TRUE_POSITIVE else 0
                                   for detection in detections])

        return Recall.from_true_positives_and_total_number_ground_truth_objects_for_class(true_positives,
                                                                                          number_of_ground_truth_objects_for_class)

    @staticmethod
    def from_true_positives_and_total_number_ground_truth_objects_for_class(true_positives,
                                                                            number_of_ground_truth_objects_for_class):
        true_positives_cumulative = true_positives.cumsum()

        return true_positives_cumulative / (number_of_ground_truth_objects_for_class + 1e-16)
