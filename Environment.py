from cv2 import cv2
import math
from Constants import Color


class Environment:
    """ Environmnet class

    Attributes:
        map (numpy_3d_array) : (y, x, RGB_channel)
        map_width (int): maxmimum x of the map
        map_height (int): maximum y of the map
    """

    def __init__(self, map_path):
        """ Constructor for Environment

        Arguments:
            map_path (string) : map path
        """
        self.map = cv2.resize(cv2.imread(map_path),
                              (500, 400))  # 2d numpy [row][col][channel-rgb]
        self.map_width = self.map.shape[1]
        self.map_height = self.map.shape[0]

        # TODO : once drawing is done, change to this
        """
        min_robot_x = math.inf
        max_robot_x = -math.inf
        min_goal_x = math.inf
        max_goal_x = -math.inf

        for i in range(self.map_width):
            for j in range(self.map_height):
                if self.map[i][j] == ROBOT:
                    min_robot_x = min(min_robot_x, i)
                    max_robot_x = max(max_robot_x, i)
                if self.map[i][j] == GOAL:
                    min_goal_x = min(min_goal_x, i)
                    max_goal_x = max(max_goal_x, i)

        self.start_x = (min_robot_x + max_robot_x)
        self.start_y = (min_robot_y + max_robot_y)
        self.goal_x = (min_goal_x + max_goal_x)
        self.goal_y = (min_goal_y + max_goal_y)
        """
        self.start_x = 25
        self.start_y = 25
        self.goal_x = 300
        self.goal_y = 210

    def type(self, x, y):
        """ TODO PIXEL -> VERTEX 

        Arguments:
            x {} -- [description]
            y {} -- [description]

        Returns:
            type_pixel -- [description]
        """
        if x < 0 or y < 0 or x >= self.map_width or y >= self.map_height or (self.map[y][x] == Color.OBSTACLE).all():
            return "OBSTACLE"
        elif (self.map[y][x] == Color.BLANK).all():
            return "SAFE"
        elif (self.map[y][x] == Color.BLANK).all():
            return "GOAL"
        else:
            return "UNKNOWN"
