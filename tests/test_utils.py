from .context import *


def test_iou():
    ious = iou(Detection(file_id='img1', class_id=1, confidence=0.6,
                         bounding_box=BoundingBox(1, 1, 2, 2)),
               [GroundTruth(file_id='img1', class_id=1,
                            bounding_box=BoundingBox(1, 1, 2, 2)),
                GroundTruth(file_id='img1', class_id=1,
                            bounding_box=BoundingBox(1, 1, 2.3, 2.3))
                ]
               )

    assert ious == [1.0, 0.7561436672967865]


def test_iou2():
    assert bbox_iou2(box1=BoundingBox(1, 1, 2, 2),
                     box2=BoundingBox(1, 1, 2, 2)) == 1

    iou = bbox_iou2(box1=BoundingBox(1, 1, 2, 2),
                    box2=BoundingBox(1, 1, 2.3, 2.3))

    print(iou)
