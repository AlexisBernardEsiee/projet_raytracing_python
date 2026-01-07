from vector import Vector

class Light:
    def __init__(self, intensity: float):
        self.intensity = intensity

class AmbientLight(Light):
    def __init__(self, intensity: float):
        super().__init__(intensity)
    

class PointLight(Light):
    def __init__(self, position: 'Vector', intensity: float):
        self.position = position
        super().__init__(intensity)

class DirectionalLight(Light):
    def __init__(self, direction: 'Vector', intensity: float):
        self.direction = direction.normalize()
        super().__init__(intensity)