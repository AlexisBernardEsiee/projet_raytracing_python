from vector import Vector
from color import Color

class Object:
    def __init__(self, position: 'Vector', color: 'Color'):
        self.position = position
        self.color = color

    def intersect(self, ray_origin: 'Vector', ray_direction: 'Vector') -> tuple[float, float]:
        raise NotImplementedError("Subclasses must implement this method")