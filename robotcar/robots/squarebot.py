from robotcar.core import Robot, Geometry
from robotcar.geometries import Rectangle
from robotcar.map import Map
from cv2 import cv2


class Squarebot(Robot):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"

    def __init__(self, map, sensors, start_x, start_y):
        super().__init__(map, sensors, start_y, start_y)
        self.action_space = {Squarebot.LEFT,
                             Squarebot.RIGHT, Squarebot.UP, Squarebot.DOWN}

    def draw(self, map):
        return cv2.rectangle(map, (int(self._x - self.SIDE / 2), int(self._y - self.SIDE / 2)), (int(self._x + self.SIDE / 2), int(self._y + self.SIDE / 2)), Map.ROBOT, -1)

    def step(self, action):
        if action == Squarebot.LEFT:
            self._x -= 1
        if action == Squarebot.RIGHT:
            self._x += 1
        if action == Squarebot.UP:
            self._y += 1
        if action == Squarebot.DOWN:
            self._y -= 1
