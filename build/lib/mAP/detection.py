class Detection:
    def __init__(self, file_id, class_id, confidence, bounding_box):
        self.file_id = file_id
        self.class_id = class_id
        self.confidence = confidence
        self.bounding_box = bounding_box

        self.classification = None

    def set_classification(self, classification):
        self.classification = classification

    def __repr__(self):
        return f"Detection({self.file_id}, {self.class_id}, {self.confidence}, {self.bounding_box}, {self.classification})"
