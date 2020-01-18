import cv2
import math
from Constants import ROBOT, GOAL


class Environment:
    def __init__(self, map_path):
        self.map = cv2.imread(map_path)
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
        self.start_x = 50
        self.start_y = 50
        self.goal_x = 150
        self.goal_y = 150

        self.map = cv2.circle(self.map, (int(self.goal_x), int(self.goal_y)),
                              color=(255, 0, 0), radius=5, thickness=-1)
