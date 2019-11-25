from mean_average_precision.utils import xywh2xyxy


class BoundingBox:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @classmethod
    def from_xywh(cls, x, y, w, h):
        x1, y1, x2, y2 = xywh2xyxy(x, y, w, h)
        return BoundingBox(x1, y1, x2, y2)

    def __repr__(self):
        return f"BoundingBox({self.x1}, {self.y1}, {self.x2}, {self.y2})"
