from vector import Vector
from color import Color

class Object:
    def __init__(self, position: 'Vector', color: 'Color', specular: float = 500, reflective: float = 0):
        self.position: Vector = position
        self.color: Color = color
        self.specular: float = specular
        self.reflective: float = reflective

    def intersect(self, origin: 'Vector', direction: 'Vector') -> tuple[float, float]:
        raise NotImplementedError("Subclasses must implement this method")