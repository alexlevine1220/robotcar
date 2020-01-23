from Environment import Environment
from Robot import Robot
from cv2 import cv2


class Simulator:
    def __init__(self, robot_type, sensor_type, map_path, debug=False):
        """
        :param map_path:
        """
        self.env = Environment(map_path)
        self.robot = Robot(robot_type, sensor_type, self.env,
                           self.env.start_x, self.env.start_y, debug)
        self.total_step = 0
        self.action_space = self.robot.action_space

    def reset(self):
        """
        :return:
        sensor  : sensor data from robot
        done    : 0 if not done, otherwise total_step
        """

        self.robot.x = self.env.start_x
        self.robot.y = self.env.start_y
        self.total_step = 0
        return self.robot.sense(self.robot.x, self.robot.y), 0

    def step(self, action_type):
        """
        :param action_type: choose action
        :return:
        sensor  : sensor data from robot
        done    : 0 if not done, otherwise total_step
        """
        self.total_step += 1
        return self.robot.step(action_type), 0

    def render(self):
        """
        Draw environment and robot on the screen.
        """
        # Draw robot
        cv2.imshow("lab", self.robot.draw(True))
        cv2.waitKey(1)
        self.robot.draw(False)

    def close(self):
        """
        Close image and finish return
        """
        pass
