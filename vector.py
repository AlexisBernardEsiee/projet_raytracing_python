class Vector:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x: float = x
        self.y: float = y
        self.z: float = z
    
    def __add__(self, other) -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other) -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar: float) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, other):
        if isinstance(other, float):
            return Vector(self.x / other, self.y / other, self.z / other)
        return self
    
    def dot(self, other: 'Vector') -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other: 'Vector') -> 'Vector':
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def magnitude(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5
    
    def normalize(self) -> 'Vector':
        mag: float = self.magnitude()
        if mag == 0:
            return Vector(0, 0, 0)
        return Vector(self.x / mag, self.y / mag, self.z / mag)
    
    @staticmethod
    def origin() -> 'Vector':
        return Vector(0, 0, 0)

    @staticmethod
    def reflect(vector, normal):
        return normal * 2 * vector.dot(normal) - vector
    
    def from_to(v1: 'Vector', v2: 'Vector') -> 'Vector':
        return v2 - v1
    
    def direction(v1: 'Vector', v2: 'Vector') -> 'Vector':
        return Vector.from_to(v1, v2).normalize()
    
    def midpoint(v1: 'Vector', v2: 'Vector') -> 'Vector':
        return Vector(
            (v1.x + v2.x) / 2,
            (v1.y + v2.y) / 2,
            (v1.z + v2.z) / 2
        )
    
    def between(v1: 'Vector', v2: 'Vector', t: float) -> 'Vector':
        return Vector(
            v1.x + (v2.x - v1.x) * t,
            v1.y + (v2.y - v1.y) * t,
            v1.z + (v2.z - v1.z) * t
        )