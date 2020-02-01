import math
from robotcar.core import COLOR, Robot, ROBOT, ACTION
from time import sleep
from cv2 import cv2


class CircleBot(Robot):
    """
    Attributes:
    """

    def __init__(self, env, robot_type, sensors):
        """
        """
        self.robot_type = robot_type
        self.radius = 5
        self.action_space = [ACTION.MOVE, ACTION.LTURN, ACTION.RTURN]
        self.angle = 0
        self._x = env.start_x
        self._y = env.start_y
        self._env = env

    def step(self, x, y, action):
        """
        Params:
            x (float)
        Returns:
            new_x (float) : after action
            new_y (float) : after action

        """

        new_x = self._x
        new_y = self._y

        if action == ACTION.MOVE:
            new_x += math.sin(self.angle)
            new_y += math.cos(self.angle)
        elif action == ACTION.LTURN:
            self.radius -= 0.1
        elif action == ACTION.RTURN:
            self.radius += 0.1

        return new_x, new_y
