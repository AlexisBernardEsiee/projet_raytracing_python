from vector import Vector
from matrix import Matrix, RotationMatrix

class Camera:

  def __init__(self, rotation_angle=1.0, rotation_axis: Vector=Vector.origin(), position=Vector.origin()):
    self.position = position
    self.rotation_angle = rotation_angle
    self.rotation_axis = rotation_axis
    self.rotation = RotationMatrix(rotation_axis, rotation_angle)

  def setPosition(self, position: Vector):
    self.position = position

  def setRotation(self, rotation_axis: Vector, rotation_angle: float):
    self.rotation_axis = rotation_axis
    self.rotation_angle = rotation_angle
    self.rotation = RotationMatrix(rotation_axis, rotation_angle)