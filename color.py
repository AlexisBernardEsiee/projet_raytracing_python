class Color:
    def __init__(self, r, g, b):
        self.r = r if r < 256 else 255
        self.g = g if g < 256 else 255
        self.b = b if b < 256 else 255

    def __mul__(self, scalar: float) -> 'Color':
        return Color(int(self.r * scalar), int(self.g * scalar), int(self.b * scalar))
    
    def to_tuple(self):
        return (self.r, self.g, self.b)
    
    @staticmethod
    def from_tuple(t):
        return Color(t[0], t[1], t[2])
    
