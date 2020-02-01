""" Constants and abstract class for robotcar
"""


class COLOR:
    """ Color types constants
    """
    ROBOT = (255, 0, 0)
    OBSTACLE = (0, 0, 0)
    GOAL = (0, 0, 255)
    BLANK = (255, 255, 255)


class Object:
    def __init__(self, x, y, vertices=None, radius=None):
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


class Robot:
    """ Abstract class for Robot
    """
    CIRCLE = "CIRCLE"
    SQUARE = "SQUARE"

    def __init__(self, env, sensors, x, y):
        self.action_space = None
        self.sensors = sensors
        self._env = env
        self._x = x
        self._y = x

    def step(self, action):
        raise NotImplementedError

    def sense(self):
        sensor_data = {}
        for k, v in self.sensors:
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


class Environment:
    """ Abstract class for Environment

    Attributes:
        map_width, map_height {float} : dimension of map in pixel
        start_x, start_y {float} : start position of robot
        goal_x, goal_y {float} : goal position
        obstacles {[Object]} : list of obstacles in the environment
    """
    ENV_1 = "ENV_1"

    def __init__(self):
        self.map_width, self.map_height = None, None
        self.start_x, self.start_y = None, None
        self.goal_x, self.goal_y = None, None
        self.obstacles = []

        raise NotImplementedError
