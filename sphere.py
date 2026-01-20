from color import Color
from vector import Vector
from object import Object

class Sphere(Object):
    def __init__(self, position: 'Vector', radius: float, color: 'Color', specular: float = 500, reflective: float = 0):
        self.position = position
        self.radius = radius
        self.color = color
        self.specular = specular
        self.reflective = reflective

    def intersect(self, origin, direction) -> tuple[float, float]:
        """
        Calculate the intersections of a ray with the sphere.
        
        :param self: himself (the sphere)
        :param origin: the origin of the ray
        :param direction: the description of the ray
        :return: A tuple containing the two intersection points (t1, t2)
        :rtype: tuple[float, float]
        """
        r = self.radius
        CO = origin - self.position

        a = direction.dot(direction)
        b = 2 * CO.dot(direction)
        c = CO.dot(CO) - r * r

        discriminant = b*b - 4*a*c

        if discriminant < 0:
            return float('inf'), float('inf')
        t1 = (-b + discriminant**0.5) / (2*a)
        t2 = (-b - discriminant**0.5) / (2*a)
        return t1, t2