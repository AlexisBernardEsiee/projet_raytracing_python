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
import json
import sys
import time

file = "scenes/" + sys.argv[1] + ".json"
CANVA = "canva"
SCENE = "scene"
SCENE_BACKGROUND= "background"
SCENE_OBJECTS = "objects"
SCENE_LIGHTS = "lights"
SCENE_CAMERA = "camera"


def load():
  with open(file) as f:
    data = json.load(f)
    canva = Canva(data[CANVA]["width"], data[CANVA]["height"])
    scene = Scene()
    scene.set_background_color(Color(
        data[SCENE][SCENE_BACKGROUND]["r"],
        data[SCENE][SCENE_BACKGROUND]["g"],
        data[SCENE][SCENE_BACKGROUND]["b"]))

    for obj_data in data[SCENE].get(SCENE_OBJECTS, []):
        if obj_data["type"] == "sphere":
            position = Vector(*obj_data["position"])
            color = Color(*obj_data["color"])
            sphere = Sphere(position=position, radius=obj_data["radius"], color=color,
                            specular=obj_data.get("specular", 500), reflective=obj_data.get("reflective", 0))
            scene.add_object(sphere)

    for light_data in data[SCENE].get(SCENE_LIGHTS, []):
        if light_data["type"] == "point":
            position = Vector(*light_data["position"])
            light = PointLight(position=position, intensity=light_data["intensity"])
            scene.add_light(light)
        elif light_data["type"] == "directional":
            direction = Vector(*light_data["direction"])
            light = DirectionalLight(direction=direction, intensity=light_data["intensity"])
            scene.add_light(light)

    camera_data = data[SCENE].get(SCENE_CAMERA, {})
    camera = Camera()
    if "position" in camera_data:
        camera.setPosition(Vector(*camera_data["position"]))
    if "rotation_axis" in camera_data and "rotation_angle" in camera_data:
        camera.setRotation(Vector(*camera_data["rotation_axis"]), camera_data["rotation_angle"])

    start_time = time.time()
    for x in range(-canva.width // 2, canva.width // 2):
        for y in range(-canva.height // 2, canva.height // 2):
            direction = camera.rotation * canva.to_viewport(x, y)
            origin = camera.position
            color = scene.trace_ray(origin, direction, 1.0, float('inf'), recursion_depth=3)
            canva.put_pixel(x, y, color)
    canva.save(f"{sys.argv[1]}.ppm")
    end_time = time.time()
    print(f"Rendering completed in {end_time - start_time} seconds.")

load()