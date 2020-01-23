from cv2 import cv2
import math
from Constants import ROBOT, GOAL, OBSTACLE, BLANK


class Environment:
    def __init__(self, map_path):
        """[summary]

        Arguments:
            map_path {[type]} -- [description]
        """
        self.map = cv2.resize(cv2.imread(map_path),
                              (200, 160))  # 2d numpy [row][col][channel-rgb]
        self.map_width = self.map.shape[0]
        self.map_height = self.map.shape[1]

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
        self.start_x = 10
        self.start_y = 20
        self.goal_x = 190
        self.goal_y = 150

        self.map = cv2.circle(self.map, (int(self.goal_x), int(
            self.goal_y)), color=GOAL, radius=5, thickness=-1)

    def type(self, x, y):
        if x < 0 or y < 0 or x >= self.map_width or y >= self.map_height:
            return "OUT"
        elif (self.map[y][x] == ROBOT).all():
            return "ROBOT"
        elif (self.map[y][x] == OBSTACLE).all():
            return "OBSTACLE"
        elif (self.map[y][x] == BLANK).all():
            return "SAFE"
        elif (self.map[y][x] == GOAL).all():
            return "GOAL"
        else:
            return "UNKNOWN"
