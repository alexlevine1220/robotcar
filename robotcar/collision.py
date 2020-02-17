""" Collision Detector class
"""

from cv2 import cv2

import numpy as np


class Collision:
    def __init__(self, width, height, obstacles):
        self.map = np.zeros((width, height))  # 1 with obstacle

        for obs in obstacles:
            self.map = obs.draw_grid(self.map)

    def isCollide(self, obj):
        for x, y in obj.collision_points():
            if self.map[int(x)][int(y)] == 1:
                return True
        return False
