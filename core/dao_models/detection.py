import jsonpickle as jp
from core.config import IMAGE_SEGMENT_SIZE_PX as WIDTH, IMAGE_SEGMENT_SIZE_PX as HEIGHT


class Detection:
    def __init__(self,
                 x: int,
                 y: int,
                 mass: int,
                 width: int = WIDTH,
                 height: int = HEIGHT):
        self.x = x
        self.y = y
        self.mass = mass
        self.width = width
        self.height = height

    def get_json(self) -> str:
        str = jp.encode(self, unpicklable=False)
        print(str)
        return str

    @classmethod
    def from_json(cls, json: str):
        print("JSON:" + json)
        return cls(**jp.decode(json))
