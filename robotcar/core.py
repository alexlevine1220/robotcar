""" Constants and abstract class for robotcar
"""

import numpy as np
import robotcar


class Geometry:
    def __init__(self, x, y, color):
        raise NotImplementedError

    def distance(self, x, y, angle):
        """ Check  distance from a point with given angle

        Arguments:
            x (float) : staring position
            y (float) : [description]
            angle (float) : [description]
        Returns:
            distance (float) :
        """
        return float("inf")

    def draw(self, map):
        """ draw following object on the map

        Arguments:
            map {np.array} : map where the geometry will be drawn
        """
        raise NotImplementedError


class Robot(Geometry):
    """ Abstract class for Robot
    """
    CIRCLE = "CIRCLE"
    SQUARE = "SQUARE"
    SIDE = 10

    def __init__(self, map, sensors, x, y):
        self.action_space = None
        self.sensors = sensors
        self._map = map
        self._x = x
        self._y = y

    def draw(self, map):
        raise NotImplementedError

    def step(self, action):
        raise NotImplementedError

    def sense(self):
        sensor_data = {}
        print(self.sensors)
        for k, v in self.sensors.items():
            sensor_data[k] = v.sense(self._x, self._y)
        return sensor_data


class Sensor:
    """ Abstract class for Sensor

    Class Varibale:
        BIRDEYE

    Attributes:
        sensor_type {SENSOR} : sensor types
        env {Environment} : environment where sensor resides
    """
    BIRDEYE = "BIRDEYE"

    def __init__(self, env):
        self._env = env

    def sense(self, x, y):
        raise NotImplementedError
