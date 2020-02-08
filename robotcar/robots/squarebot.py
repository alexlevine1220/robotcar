from robotcar.core import Robot, Geometry
from robotcar.geometries import Rectangle
from robotcar.env import Env
from cv2 import cv2


class Squarebot(Robot, Rectangle):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"
    SIDE = 10
    COLOR = (0, 0, 1)

    def __init__(self, env, sensors, start_x, start_y):
        super().__init__(env, sensors, start_y, start_y)
        self.action_space = {Squarebot.LEFT,
                             Squarebot.RIGHT, Squarebot.UP, Squarebot.DOWN}

    @property
    def vertices(self):
        return [(self._x - self.SIDE / 2, self._y - self.SIDE / 2), (self._x - self.SIDE / 2, self._y + self.SIDE),
                (self._x + self.SIDE / 2, self._y + self.SIDE / 2), (self._x + self.SIDE / 2, self._y - self.SIDE / 2)]

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
            for obs in self._env.obstacles:
                if not collide and obs.containsPoint(bx, by):
                    collide = True

        if not collide:
            self._x = nx
            self._y = ny
