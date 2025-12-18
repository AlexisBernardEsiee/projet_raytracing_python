class Color:
    def __init__(self, r, g, b):
        self.r = r % 256
        self.g = g % 256
        self.b = b % 256
    
    def to_tuple(self):
        return (self.r, self.g, self.b)
    
    @staticmethod
    def from_tuple(t):
        return Color(t[0], t[1], t[2])
    
