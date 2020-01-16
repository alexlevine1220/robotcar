import numpy as np
import cv2
import gym
import Robot


class Environment:
    def __init__(self, robot_type, sensor_type, map_path):
        self.robot = Robot.Robot(robot_type, sensor_type)
        self.action_space = self.robot.action_space
        self.total_step = 0
        self.map = cv2.imread(map_path)

    def reset(self):
        """
        :return:
        sensor  : sensor data from robot
        done    : 0 if not done, otherwise total_step
        """
        self.robot.reset()
        self.total_step = 0
        return 0, 0

    def step(self, action_type):
        """
        :param action_type: choose action
        :return:
        sensor  : sensor data from robot
        done    : 0 if not done, otherwise total_step
        """
        self.robot.step(action_type)
        self.total_step += 1
        return self.robot, 0

    def render(self):
        """
        Draw environment and robot on the screen.
        """
        with_robot = cv2.circle(self.map, (int(self.robot.x), int(self.robot.y)), color=(0, 0, 255), radius=5, thickness=-1)
        cv2.imshow("lab", with_robot)
        cv2.waitKey(1)

    def close(self):
        pass
