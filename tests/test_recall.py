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


def test_recall():
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
    recall = Recall.compute(detections, 8)
    print(recall)


def test_recall_backpack():
    true_positives = np.array( [1, 0, 1, 1, 0])
    recall = Recall.from_true_positives_and_total_number_ground_truth_objects_for_class(true_positives, 11)
    assert recall.tolist() ==  [0.09090909090909091, 0.09090909090909091, 0.18181818181818182, 0.2727272727272727, 0.2727272727272727]

def test_recall_bed():
    true_positives = np.array([1, 1, 1, 1, 1, 1, 0, 1])
    recall = Recall.from_true_positives_and_total_number_ground_truth_objects_for_class(true_positives, 8)
    assert recall.tolist() == [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.75, 0.875]
