from sklearn import metrics

from .context import *


def test_average_precision():
    recall = [0.125, 0.25, 0.375, 0.375, 0.375, 0.375]
    precision = [1., 1., 1., 0.75, 0.6, 0.5]

    ap = compute_average_precision(recall, precision)
    print(ap)
