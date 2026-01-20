from vector import Vector
from math import cos, sin


class Matrix:

  def __init__(self, rows: int = 3):
    self.rows = rows
    self.values: list[Vector] = [Vector(0, 0, 0) for _ in range(rows)]


class RotationMatrix(Matrix):

  def __init__(self, axis: Vector, angle: float, rows: int = 3):
    super().__init__(rows)
    self.axis = axis.normalize()
    self.angle = angle
    self.values: list[Vector] = [
      Vector(axis.x ** 2 * (1 - cos(angle)) + cos(angle),
             axis.x * axis.y * (1 - cos(angle)) + axis.z * sin(angle),
             axis.x * axis.z * (1 - cos(angle)) - axis.y * sin(angle)),
      Vector(axis.x * axis.y * (1 - cos(angle)) - axis.z * sin(angle),
             axis.y ** 2 * (1 - cos(angle)) + cos(angle),
             axis.y * axis.z * (1 - cos(angle)) + axis.x * sin(angle)),
      Vector(axis.x * axis.z * (1 - cos(angle)) + axis.y * sin(angle),
             axis.y*axis.z*(1 - cos(angle)) - axis.x * sin(angle),
             axis.z ** 2 * (1 - cos(angle)) + cos(angle))]

  def __mul__(self, vector: Vector):
    return Vector(vector.x * self.values[0].x + vector.y * self.values[0].y + vector.z * self.values[0].z,
                    vector.x * self.values[1].x + vector.y * self.values[1].y + vector.z * self.values[1].z,
                    vector.x * self.values[2].x + vector.y * self.values[2].y + vector.z * self.values[2].z)
