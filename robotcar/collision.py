""" Collision Detector class
"""

from cv2 import cv2

import numpy as np


class Collision:
    def __init__(self, width, height, obstacles):
        self.map = np.zeros((width, height))  # 1 with obstacle

    def isCollide(self, obj):
        pass
