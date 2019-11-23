class GroundTruth:
    def __init__(self, file_id, class_idx, bounding_box):
        self.file_id = file_id
        self.class_idx = class_idx
        self.bounding_box = bounding_box

    def __repr__(self):
        return f"Detection({self.file_id}, {self.class_idx}, {self.bounding_box})"
