from .context import *


def _get_true_positive_detection(confidence):
    detection = Detection(file_id='img1', class_idx=1, confidence=confidence,
                          bounding_box=BoundingBox(1, 1, 2, 2))
    detection.set_classification(Classification.TRUE_POSITIVE)
    return detection


def _get_false_positive_detection(confidence):
    detection = Detection(file_id='img1', class_idx=1, confidence=confidence,
                          bounding_box=BoundingBox(1, 1, 2, 2))
    detection.set_classification(Classification.FALSE_POSITIVE)
    return detection


def test_precision():
    detections = [
        _get_true_positive_detection(0.4),
        _get_false_positive_detection(0.1),
        _get_true_positive_detection(0.7),
        _get_false_positive_detection(0.2),
        _get_false_positive_detection(0.3),
        _get_true_positive_detection(0.5),
    ]
    print()
    print(detections)
    precision = Precision.compute(detections)
    print(precision)
