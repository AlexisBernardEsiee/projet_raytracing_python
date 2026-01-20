from cmath import inf

from vector import Vector
from color import Color
from object import Object
from light import Light, AmbientLight, PointLight, DirectionalLight

class Scene:
    def __init__(self, background_color: 'Color' = Color(0, 0, 0)):
        self.objects: list[Object] = []
        self.lights: list[Light] = []
        self.background_color = background_color

    def add_object(self, obj: 'Object'):
        self.objects.append(obj)
    
    def add_light(self, light: 'Light'):
        self.lights.append(light)

    def set_background_color(self, color: 'Color'):
        self.background_color = color

    def trace_ray(self, origin: 'Vector', direction: 'Vector', t_min: float, t_max: float, recursion_depth=5) -> 'Color':
        closest_object, closest_t = self.closest_intersection(origin, direction, t_min, t_max)
        if closest_object is None:
            return self.background_color
        P = origin + direction * closest_t
        N = P - closest_object.position
        N = N / N.magnitude()
        local_color: Color = closest_object.color * self.compute_lighting(P, N, direction * -1,
                                                     closest_object.specular)
        r = closest_object.reflective
        if recursion_depth <= 0 or r <= 0:
            return local_color
        R = Vector.reflect(direction*-1, N)
        reflected_color = self.trace_ray(P, R, 0.001, inf, recursion_depth-1)
        return local_color * (1 - r) + reflected_color * r

    def compute_lighting(self, P: 'Vector', N: 'Vector', V: 'Vector' = None, s: float = 500) -> float:
        i = 0.0
        for light in self.lights:
            if isinstance(light, AmbientLight):
                i += light.intensity
            else:
                t_max = 1
                if isinstance(light, PointLight):
                    L = light.position - P
                    t_max = 1
                else:
                    L = light.direction
                    t_max = inf
                shadow_object, shadow_t = self.closest_intersection(P, L, 0.001, t_max)
                if shadow_object is not None:
                    continue
                n_dot_l = N.dot(L)
                if n_dot_l > 0:
                    i += light.intensity * n_dot_l / (N.magnitude() * L.magnitude())

                if s != -1 and V is not None:
                    R = N * 2 * N.dot(L) - L
                    r_dot_v = R.dot(V)
                    if r_dot_v > 0:
                        i += light.intensity * ((r_dot_v / (R.magnitude() * V.magnitude())) ** s)
        return i

    def closest_intersection(self, origin: 'Vector', direction: 'Vector', t_min: float, t_max: float) -> tuple[Object, float]:
        closest_t: float = inf
        closest_object: Object = None
        for object in self.objects:
            t1, t2 = object.intersect(origin=origin, direction=direction)
            if t_min < t1 < t_max and t1 < closest_t:
                closest_t = t1
                closest_object = object

            if t_min < t2 < t_max and t2 < closest_t:
                closest_t = t2
                closest_object = object

        return closest_object, closest_t

