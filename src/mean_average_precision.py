from collections import defaultdict
from mAP.classify import Classify
from mAP.precision import Precision
from mAP.recall import Recall
from mAP.average_precision import compute_average_precision


class MeanAveragePrecision:

    def __init__(self):
        self._ground_truth_counter_per_class = defaultdict(lambda: 1)
        self._detections = []

    def _update_ground_truth_counter_per_class(self, ground_truths):
        for ground_truth in ground_truths:
            self._ground_truth_counter_per_class[ground_truth.class_idx] += 1

    def add_detections_for_image(self, detections, ground_truths):
        self._update_ground_truth_counter_per_class(ground_truths)

        for detection in detections:
            classification, ground_truths = Classify.classify(detection, ground_truths)
            detection.set_classification(classification)

        self._detections += detections

    def compute(self, class_names=()):

        unique_class_idxs = set([d.class_idx for d in self._detections])
        average_precision_for_classes = {}

        for class_idx in unique_class_idxs:
            detections_for_class = list(filter(lambda d: d.class_idx == class_idx, self._detections))
            number_of_ground_truth_objects_for_class = self._ground_truth_counter_per_class[class_idx]

            precision = Precision.compute(detections_for_class)
            recall = Recall.compute(detections_for_class, number_of_ground_truth_objects_for_class)

            average_precision_for_class = compute_average_precision(recall=recall, precision=precision)

            class_name = ""
            if len(class_names) <= class_idx:
                class_name = class_names[class_idx]

            average_precision_for_classes[f"{class_name, ({class_idx})}"] = average_precision_for_class

        return average_precision_for_classes
