from robotcar.geometries import Rectangle
from random import randrange
import numpy as np


class Map:
    """ Abstract class for Environment

    Attributes:
        map_width, map_height {float} : dimension of map in pixel
        start_x, start_y {float} : start position of robot
        goal_x, goal_y {float} : goal position
        obstacles {[Geometry]} : list of Geometries in the environment
    """
    ROBOT = (255, 0, 0)
    OBSTACLE = (0, 0, 0)
    GOAL = (0, 0, 255)
    BLANK = (255, 255, 255)

    def __init__(self, map_json):
        self.map_width, self.map_height = 500, 500
        self.start_x, self.start_y = randrange(500), randrange(500)
        self.goal_x, self.goal_y = randrange(500), randrange(500)

        # Boundary
        self.obstacles = [
            Rectangle(0, 0, self.map_width - 1,
                      10, Map.OBSTACLE),      # UP
            Rectangle(0, self.map_height - 10, self.map_width,
                      self.map_height - 1, Map.OBSTACLE),               # DOWN
            Rectangle(0, 0, 10, self.map_height - 1, Map.OBSTACLE),     # LEFT
            Rectangle(self.map_width - 10, 0, self.map_width - 1,
                      self.map_height - 1, Map.OBSTACLE),               # RIGHT
        ]

    def get_map(self):
        """ Return map 
        """
        map = np.ones((self.map_height, self.map_width)) * 255

        for obstacle in self.obstacles:
            obstacle.draw(map)
        return map
