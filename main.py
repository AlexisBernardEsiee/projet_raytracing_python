from canva import Canva
from color import Color
from vector import Vector
from sphere import Sphere
from scene import Scene
from object import Object
from scene import Scene
from light import Light, AmbientLight, PointLight, DirectionalLight
from camera import Camera
from math import pi
import time

def main():
    # Create a canvas
    canvas = Canva(600, 600)
    start_time = time.time()

    # Create a scene
    scene = Scene()
    scene.set_background_color(Color(50, 78, 38))

    # Add a red sphere to the scene
    sphere = Sphere(position=Vector(0, -1, 3), radius=1, color=Color(255, 0, 0), specular=500, reflective=0.2)
    scene.add_object(sphere)
    sphere2 = Sphere(position=Vector(2, 0, 4), radius=1, color=Color(0, 255, 0), specular=500)
    scene.add_object(sphere2)
    sphere3 = Sphere(position=Vector(-2, 0, 4), radius=0.5, color=Color(0, 0, 255), specular=10)
    scene.add_object(sphere3)
    sphere4 = Sphere(position=Vector(0, -5001, 0), radius=5000, color=Color(255, 255, 0), specular=1000, reflective=0.5)
    scene.add_object(sphere4)
    sphere5 = Sphere(position=Vector(0, 2, 3), radius=0.2, color=Color(255,255,0), reflective=0.3)
    scene.add_object(sphere5)

    # Add lights to the scene
    point_light = PointLight(position=Vector(0, 0, 0), intensity=0.6)
    scene.add_light(point_light)
    directional_light = DirectionalLight(direction=Vector(1, 4, 4), intensity=0.2)
    scene.add_light(directional_light)

    camera = Camera()
    camera.setPosition(Vector(0, 0, -1))
    camera.setRotation(Vector(0,0,1), 0)

    # Trace rays for each pixel in the canvas
    for x in range(-canvas.width // 2, canvas.width // 2):
        for y in range(-canvas.height // 2, canvas.height // 2):
            # Convert canvas coordinates to viewport coordinates
            direction = camera.rotation * canvas.to_viewport(x, y)
            origin = camera.position

            # Trace the ray and get the color
            color = scene.trace_ray(origin, direction, 1.0, float('inf'), recursion_depth=3)
            # Put the pixel on the canvas
            canvas.put_pixel(x, y, color)
    # Save the canvas to a file
    canvas.save("scene.ppm")
    end_time = time.time()
    print(f"Rendering completed in {end_time - start_time} seconds.")

if __name__ == "__main__":
    main()