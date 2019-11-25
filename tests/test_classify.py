from .context import *
from .helper import *


def test_classify_true_positive():
    ground_truths = np.array(get_from_file(os.path.join(GT_PATH, '2007_000636.txt')))

    detection = Detection(2007_000636, 'bed', 0.263161, BoundingBox(33, 57, 117, 194))

    classification, remaining = Classify.classify(detection, ground_truths)
    assert classification == Classification.TRUE_POSITIVE

