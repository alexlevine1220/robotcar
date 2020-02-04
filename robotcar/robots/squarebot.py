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
        return cv2.rectangle(map, (int(self._x - self.SIDE / 2), int(self._y - self.SIDE / 2)),
                             (int(self._x + self.SIDE / 2), int(self._y + self.SIDE / 2)), Map.ROBOT, -1)

    def boundaries(self):
        return [(self._x - self.SIDE / 2, self._y - self.SIDE / 2), (self._x - self.SIDE / 2, self._y + self.SIDE),
                (self._x + self.SIDE / 2, self._y - self.SIDE / 2), (self._x + self.SIDE / 2, self._y + self.SIDE / 2)]

    def step(self, action):
        nx = self._x
        ny = self._y
        if action == Squarebot.LEFT:
            nx -= 1
        if action == Squarebot.RIGHT:
            nx += 1
        if action == Squarebot.UP:
            ny += 1
        if action == Squarebot.DOWN:
            ny -= 1
        collide = False

        for bx, by in self.boundaries():
            for obs in self._map.obstacles:
                if not collide and obs.containsPoint(bx, by):
                    collide = True

        if not collide:
            self._x = nx
            self._y = ny
