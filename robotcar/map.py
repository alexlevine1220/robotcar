from robotcar.geometries import Rectangle
from random import randrange
import numpy as np
from cv2 import cv2


class Map:
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

    OBSTACLE_COUNT = 10
    OBSTACLE_SIDE_LENGTH = 10

    def __init__(self, map_json):
        self.map_width, self.map_height = 500, 500
        self.start_x, self.start_y = 250, 250
        self.goal_x, self.goal_y = 100, 400

        # Boundary
        self.obstacles = [
            Rectangle(Map.OBSTACLE, False, [0, 0, self.map_width - 1, 10]),                                               # UP
            Rectangle(Map.OBSTACLE, False, [0, self.map_height - 10, self.map_width, self.map_height - 1]),               # DOWN
            Rectangle(Map.OBSTACLE, False, [0, 0, 10, self.map_height - 1]),                                              # LEFT
            Rectangle(Map.OBSTACLE, False, [self.map_width - 10, 0, self.map_width - 1, self.map_height - 1]),            # RIGHT
        ]

        xInterval = (0 + Map.OBSTACLE_SIDE_LENGTH, self.map_width - Map.OBSTACLE_SIDE_LENGTH)
        yInterval = (0 + Map.OBSTACLE_SIDE_LENGTH, self.map_height - Map.OBSTACLE_SIDE_LENGTH)
        for i in range(Map.OBSTACLE_COUNT):
            self.obstacles.append(Rectangle(Map.OBSTACLE, True, None, Map.OBSTACLE_SIDE_LENGTH, xInterval, yInterval))

    def get_map(self):
        """ Return map
        """
        map = np.ones((self.map_height, self.map_width, 3))
        map = cv2.circle(map, (self.goal_x, self.goal_y), 10, Map.GOAL, -1)

        for obstacle in self.obstacles:
            map = obstacle.draw(map)
        return map
