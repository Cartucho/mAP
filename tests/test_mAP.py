from .context import *
from .helper import *

import glob
from collections import defaultdict
from pprint import pprint


def test_ground_truth_update():
    map = MeanAveragePrecision()

    ground_truths = get_from_file_list(glob.glob(GT_PATH + '/*.txt'))
    detections = get_from_file_list(glob.glob(DT_PATH + '/*.txt'))

    ground_truths.sort(key=lambda o: o.file_id)
    detections.sort(key=lambda o: o.file_id)

    gts = defaultdict(list)
    for gt in ground_truths:
        gts[gt.file_id].append(gt)

    dts = defaultdict(list)
    for dt in detections:
        dts[dt.file_id].append(dt)

    for file_id, detections_for_file in dts.items():
        ground_truths_for_file = gts[file_id]

        map.add_detections_for_image(
            detections_for_file,
            ground_truths_for_file)

    bed_detections = list(filter(lambda d: d.class_id == 'bed', map._detections))

    bed_detections.sort(key=lambda d: d.confidence, reverse=True)

    true_positive_beds = [1 if detection.classification == Classification.TRUE_POSITIVE else 0
                          for detection in bed_detections]

    assert true_positive_beds == [1, 1, 1, 1, 1, 1, 0, 1]

    mean_average_precision = map.compute()
    pprint(sorted(mean_average_precision.items(), key=lambda kv: kv[1], reverse=True))

    assert "%.2f" % (mean_average_precision['backpack'] * 100) == '22.73'
    assert "%.2f" % (mean_average_precision['bed'] * 100) == '85.94'
    assert "%.2f" % (mean_average_precision['shelf'] * 100) == '0.00'

    # 22.73% = backpack AP
    # 85.94% = bed AP
    # 17.52% = book AP
    # 14.29% = bookcase AP
    # 23.48% = bottle AP
    # 31.86% = bowl AP
    # 7.93% = cabinetry AP
    # 53.84% = chair AP
    # 4.55% = coffeetable AP
    # 19.05% = countertop AP
    # 42.50% = cup AP
    # 39.66% = diningtable AP
    # 0.00% = doll AP
    # 20.69% = door AP
    # 7.69% = heater AP
    # 71.43% = nightstand AP
    # 42.86% = person AP
    # 17.71% = pictureframe AP
    # 13.01% = pillow AP
    # 62.31% = pottedplant AP
    # 73.21% = remote AP
    # 0.00% = shelf AP
    # 16.33% = sink AP
    # 90.48% = sofa AP
    # 1.39% = tap AP
    # 0.00% = tincan AP
    # 63.25% = tvmonitor AP
    # 18.75% = vase AP
    # 45.45% = wastecontainer AP
    # 23.53% = windowblind AP
    # mAP = 31.05%
