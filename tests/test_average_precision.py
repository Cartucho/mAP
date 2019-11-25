from sklearn import metrics

from .context import *


def test_average_precision_backpack():
    recall = [0.09090909090909091, 0.09090909090909091, 0.18181818181818182, 0.2727272727272727, 0.2727272727272727]
    precision = [1.0, 0.5, 0.6666666666666666, 0.75, 0.6]

    ap = compute_average_precision(recall, precision)
    print(ap)
    assert ap == 0.22727272727272724


def test_average_precision_bed():
    recall = [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.75, 0.875]
    precision = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.8571428571428571, 0.875]

    ap = compute_average_precision(recall, precision)
    print(ap)
    assert ap == 0.859375
