from robotcar import Geometry
from robotcar import Rectangle

"""

"""

class Robot(Geometry):
    """ Abstract class for Robot
    Attributes:
        action_space : types of actions that robot can have
        sensors : types of sensors that robot has

    """
    SQUARE = "SQUARE"

    def __init__(self, collision, sensors, x, y):
        self.action_space = None
        self.sensors = sensors
        self.collision = collision
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10

    def step(self, action):
        raise NotImplementedError

    def sense(self):
        sensor_data = {}
        for sensor in self.sensors:
            for k, v in sensor.sense(self.x, self.y).items():
                sensor_data[k] = v
        return sensor_data


class Squarebot(Robot, Rectangle):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"
    SIDE = 10

    def __init__(self, collision, sensors, start_x, start_y):
        super().__init__(collision, sensors, start_y, start_y)
        self.action_space = {Squarebot.LEFT,
                             Squarebot.RIGHT, Squarebot.UP, Squarebot.DOWN}

    def vertices(self):
        return [(self._x - self.SIDE / 2, self._y - self.SIDE / 2), (self._x - self.SIDE / 2, self._y + self.SIDE),
                (self._x + self.SIDE / 2, self._y + self.SIDE / 2), (self._x + self.SIDE / 2, self._y - self.SIDE / 2)]

    def step(self, action):
        nx = self.x
        ny = self.y
        if action == Squarebot.LEFT:
            nx -= 1
        if action == Squarebot.RIGHT:
            nx += 1
        if action == Squarebot.UP:
            ny += 1
        if action == Squarebot.DOWN:
            ny -= 1

        if not self.collision.isCollide(self):
            self._x = nx
            self._y = ny
