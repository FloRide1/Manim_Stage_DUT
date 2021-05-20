from manimlib import *


class LidarScene(Scene):
    CONFIG = {
        "color": BLUE,
        "stroke_color": BLUE_E,
        "stroke_width": 4,
        "opacity": 0.5
    }

    def setup(self):
        self.lidar_object = LidarObject()

    def construct(self):
        lidar_circle = Circle()
        lidar_circle.set_fill(self.color, opacity=self.opacity)
        lidar_circle.set_stroke(self.stroke_color, width=self.stroke_width)

        self.play(ShowCreation(lidar_circle))


class LidarObject(object):
    def __init__(self, position=None, view: dict = {}):
        if position is None:
            position = {"x": 0, "y": 0, "theta": 0}

        self.position: dict = position
        self.view: dict = view

