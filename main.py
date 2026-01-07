from canva import Canva
from color import Color
from vector import Vector
from sphere import Sphere
from scene import Scene
from object import Object
from scene import Scene

def main():
    # Create a canvas
    canvas = Canva(600, 600)

    # Create a scene
    scene = Scene()
    scene.set_background_color(Color(50, 50, 50))

    # Add a red sphere to the scene
    sphere = Sphere(center=Vector(0, 0, 5), radius=1, color=Color(255, 0, 0))
    scene.add_object(sphere)
    sphere2 = Sphere(center=Vector(2, 0, 4), radius=1, color=Color(0, 255, 0))
    scene.add_object(sphere2)
    sphere3 = Sphere(center=Vector(-2, 0, 4), radius=1, color=Color(0, 0, 255))
    scene.add_object(sphere3)

    # Trace rays for each pixel in the canvas
    for x in range(-canvas.width // 2, canvas.width // 2):
        for y in range(-canvas.height // 2, canvas.height // 2):
            # Convert canvas coordinates to viewport coordinates
            direction = canvas.to_viewport(x, y)
            origin = Vector(0, 0, 0)

            # Trace the ray and get the color
            color = scene.trace_ray(origin, direction, 1.0, float('inf'))
            # Put the pixel on the canvas
            canvas.put_pixel(x, y, color)
    # Save the canvas to a file
    canvas.save("scene.ppm")

if __name__ == "__main__":
    main()