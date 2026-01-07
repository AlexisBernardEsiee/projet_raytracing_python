from color import Color
from vector import Vector

class Canva:
    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height
        self.pixels: list[list[Color]] = [[Color(0, 0, 0) for _ in range(width)] for _ in range(height)]

    def put_pixel(self, x: int, y: int, color: Color) -> None:
        """
        Put the pixel at (x, y) with the given color.
        The origin (0,0) is at the center of the canvas.
        """
        screen_x: int = self.width // 2 + x
        screen_y: int = self.height // 2 - y - 1
        
        if 0 <= screen_x < self.width and 0 <= screen_y < self.height:
            self.pixels[screen_y][screen_x] = color
    
    def save(self, filename: str) -> None:
        """
        Save the canvas to a PPM file.
        The filename should end with .ppm
        """
        with open(filename, 'w') as f:
            f.write(f"P3\n{self.width} {self.height}\n255\n")
            for row in self.pixels:
                for color in row:
                    r, g, b = color.to_tuple()
                    f.write(f"{r} {g} {b} ")
                f.write("\n")
    
    def to_viewport(self, x: int, y: int) -> Vector:
        """ Convert canvas coordinates to viewport coordinates.
         The origin (0,0) is at the center of the canvas.
        """
        vp_x: float = x * (1 / self.width)
        vp_y: float = y * (1 / self.height)
        vp_z: float = 1.0
        #TODO: The viewport dimensions (I assumed 1x1 here) should be parameters of the Canva class
        return Vector(vp_x, vp_y, vp_z)
