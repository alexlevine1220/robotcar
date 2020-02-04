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

    def containsPoint(self, x, y):
        raise NotImplementedError

    def draw(self, map):
        """ draw following object on the map

        Arguments:
            map {np.array} : map where the geometry will be drawn
        """
        raise NotImplementedError


class Robot(Geometry):
    """ Abstract class for Robot
    """
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
