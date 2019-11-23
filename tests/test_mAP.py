from .context import *




def test_ground_truth_update():
    map = MeanAveragePrecision()

    detections = [
        Detection(file_id='img1', class_idx=1, confidence=0.6,
                              bounding_box=BoundingBox(1, 1, 2, 2))

    ]

    map.add_detections_for_image()
