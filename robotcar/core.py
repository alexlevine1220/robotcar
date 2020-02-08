""" Constants and abstract class for robotcar
"""

import numpy as np
import robotcar


class Geometry:
    def __init__(self, color):
        self.color = color

    def distance(self, x, y, angle):
        """ Check distance from a point with given angle

        Arguments:
            x (float) : staring position
            y (float) : [description]
            angle (float) : [description]
        Returns:
            distance (float) :
        """
        return float("inf")

    def contains_point(self, x, y):
        """ Check whether (x, y) is in the geometry

        Arguments:
            (x, y) : coordinate to check
        """
        raise NotImplementedError

    def draw_grid(self, grid):
        """ draw following object on the grid

        Arguments:
            grid {np.array} : grid where the geometry will be drawn
        """
        raise NotImplementedError


class Robot(Geometry):
    """ Abstract class for Robot
    Attributes:
        action_space : types of actions that robot can have
        sensors : types of sensors that robot has

    """

    # robots/README.md for more information
    SQUARE = "SQUARE"

    def __init__(self, env, sensors, x, y):
        self.action_space = None
        self.sensors = sensors
        self._env = env
        self._x = x
        self._y = y
        self.color = (1, 0, 0)

    def step(self, action):
        raise NotImplementedError

    def boundaries(self):
        raise NotImplementedError

    def sense(self):
        sensor_data = {}
        for sensor in self.sensors:
            for k, v in sensor.sense(self._x, self._y).items():
                sensor_data[k] = v
        return sensor_data


class Sensor:
    BIRDEYE = "BIRDEYE"

    def __init__(self, map):
        self._map = map

    def sense(self, x, y):
        raise NotImplementedError
