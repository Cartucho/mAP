from collections import defaultdict
from mean_average_precision.classify import Classify
from mean_average_precision.precision import Precision
from mean_average_precision.recall import Recall
from mean_average_precision.average_precision import compute_average_precision
import numpy as np


class MeanAveragePrecision:

    def __init__(self):
        self._ground_truth_counter_per_class = defaultdict(lambda: 0)
        self._detections = []
        self._unique_class_ids = set()

    def _update_ground_truth_counter_per_class(self, ground_truths):
        for ground_truth in ground_truths:
            self._ground_truth_counter_per_class[ground_truth.class_id] += 1
            self._unique_class_ids.add(ground_truth.class_id)

    def add_detections_for_image(self, detections, ground_truths):
        """
        :param detections: list of Detection objects
        :param ground_truths: list of GroundTruth objects
        :return:
        """
        self._update_ground_truth_counter_per_class(ground_truths)
        ground_truths = np.array(ground_truths)

        detections.sort(key=lambda d: d.confidence, reverse=True)
        for detection in detections:
            classification, ground_truths = Classify.classify(detection, ground_truths)
            detection.set_classification(classification)

        self._detections += detections

    def compute(self):
        """
        computes mAP and returns a dictionary containing all classes mAP scores

        :return:
        """

        average_precision_for_classes = {}

        for class_id in self._unique_class_ids:
            detections_for_class = list(filter(lambda d: d.class_id == class_id, self._detections))
            number_of_ground_truth_objects_for_class = self._ground_truth_counter_per_class[class_id]

            detections_for_class.sort(key=lambda d: d.confidence, reverse=True)

            precision = Precision.compute(detections_for_class)
            recall = Recall.compute(detections_for_class, number_of_ground_truth_objects_for_class)
            average_precision_for_class = compute_average_precision(recall=recall, precision=precision)

            average_precision_for_classes[f"{class_id}"] = average_precision_for_class
        return average_precision_for_classes
