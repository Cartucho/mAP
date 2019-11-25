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


def test_precision_backpack():
    true_positives = np.array([1, 0, 1, 1, 0])
    false_positives = np.array([0, 1, 0, 0, 1])
    precision = Precision.from_true_positives_and_false_positives(true_positives, false_positives)
    print(precision)
    assert precision.tolist() == [1.0, 0.5, 0.6666666666666666, 0.75, 0.6]


def test_precision_bed():
    true_positives = np.array([1, 1, 1, 1, 1, 1, 0, 1])
    false_positives = np.array([0, 0, 0, 0, 0, 0, 1, 0])
    precision = Precision.from_true_positives_and_false_positives(true_positives, false_positives)
    print(precision)
    assert precision.tolist() == [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.8571428571428571, 0.875]
