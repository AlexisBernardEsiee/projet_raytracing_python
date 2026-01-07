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
            P = ray_direction * closest_t + ray_origin
            N = (P - closest_object.center).normalize()
            return closest_object.color * self.compute_lighting(P, N, V=ray_direction * -1, s=closest_object.specular)
        return self.background_color
    
    def compute_lighting(self, P: 'Vector', N: 'Vector', V: 'Vector' = None, s: float = 500) -> float:
        i = 0.0
        for light in self.lights:
            if isinstance(light, AmbientLight):
                i += light.intensity
            else:
                if isinstance(light, PointLight):
                    L = light.position - P
                else:
                    L = light.direction
                n_dot_l = N.dot(L)
                if n_dot_l > 0:
                    i += light.intensity * n_dot_l / (N.magnitude() * L.magnitude())

                if s != -1 and V is not None:
                    R = N * 2 * N.dot(L) - L
                    r_dot_v = R.dot(V)
                    if r_dot_v > 0:
                        i += light.intensity * ((r_dot_v / (R.magnitude() * V.magnitude())) ** s)
        return i

