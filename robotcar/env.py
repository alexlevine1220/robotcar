from robotcar.geometries import Rectangle
from random import randrange
import numpy as np
from cv2 import cv2


class Env:
    """ Abstract class for Environment

    Attributes:
        map_width, map_height {float} : dimension of map in pixel
        start_x, start_y {float} : start position of robot
        goal_x, goal_y {float} : goal position
        obstacles {[Geometry]} : list of Geometries in the environment
    """
    ROBOT = (1, 0, 0)
    OBSTACLE = (0, 0, 0)
    GOAL = (0, 0, 1)
    SAFE = (1, 1, 1)
    UNKNOWN = (0.5, 0.5, 0.5)

    def __init__(self, width, height, start_x, start_y, goal_x, goal_y, obstacles):
        self.map_width, self.map_height = width, height
        self.start_x, self.start_y = start_x, start_y
        self.goal_x, self.goal_y = goal_x, goal_y

        # Boundary
        self.obstacles = [
            Rectangle(0, 0, self.map_width - 1, 10, Env.OBSTACLE),      # UP
            Rectangle(0, self.map_height - 10, self.map_width,
                      self.map_height - 1, Env.OBSTACLE),               # DOWN
            Rectangle(0, 0, 10, self.map_height - 1, Env.OBSTACLE),     # LEFT
            Rectangle(self.map_width - 10, 0, self.map_width - 1,
                      self.map_height - 1, Env.OBSTACLE),               # RIGHT
        ]
        for obstacle in obstacles:
            self.obstacles.append(self.create_obstacle(obstacle))

        grid = cv2.circle(np.ones((height, width, 3)),
                          (goal_x, goal_y), 10, Env.GOAL, -1)

        for obstacle in self.obstacles:
            grid = obstacle.draw(grid)

        self.grid = grid

    def create_obstacle(self, config):
        """ Create Obstacles object based on config

        Arguments:
            config (Obstacle) : look at README.md in robotcar/practice
        Returns:
            Rectangle : Created object
        """
        if config["type"] == "RECTANGLE":
            return Rectangle(config["x1"], config["y1"], config["x2"], config["y2"], Env.OBSTACLE)
