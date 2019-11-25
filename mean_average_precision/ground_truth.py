class GroundTruth:

    def __init__(self, file_id, class_id, bounding_box):
        self.file_id = file_id
        self.class_id = class_id
        self.bounding_box = bounding_box


    def __repr__(self):
        return f"GroundTruth({self.file_id}, {self.class_id}, {self.bounding_box})"
