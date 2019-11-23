from collections import defaultdict
from mAP.classify import Classify


class MeanAveragePrecision:

    def __init__(self):
        self._ground_truth_counter_per_class = defaultdict(lambda: 1)
        self._detections = []

    def _update_ground_truth_counter_per_class(self, ground_truths):
        for ground_truth in ground_truths:
            self._ground_truth_counter_per_class[ground_truth.class_name] += 1

    def add_detections_for_image(self, detections, ground_truths):
        self._update_ground_truth_counter_per_class(ground_truths)

        for detection in detections:
            classification, ground_truths = Classify.classify(detection, ground_truths)
            detection.set_classification(classification)

        self._detections += detections


