from sphere import Sphere
from vector import Vector
from color import Color
from object import Object

class Scene:
    def __init__(self, background_color: 'Color' = Color(0, 0, 0)):
        self.objects: list[Object] = []
        self.background_color = background_color

    def add_object(self, obj: 'Object'):
        self.objects.append(obj)

    def set_background_color(self, color: 'Color'):
        self.background_color = color

    def trace_ray(self, ray_origin: 'Vector', ray_direction: 'Vector', t_min: float, t_max: float) -> 'Color':
        closest_t: float = float('inf')
        closest_object = None
        for obj in self.objects:
            t1, t2 = obj.intersect(ray_origin, ray_direction)
            if t_min < t1 < t_max and t1 < closest_t:
                closest_t = t1
                closest_object = obj
            if t_min < t2 < t_max and t2 < closest_t:
                closest_t = t2
                closest_object = obj
        if closest_object is not None:
            return closest_object.color
        return self.background_color
