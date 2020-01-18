import Environment
import Robot
import cv2


class Simulator:
    def __init__(self, robot_type, map_path):
        """
        :param map_path:
        """
        self.env = Environment.Environment(map_path)
        self.robot = Robot.Robot(self.env, robot_type, self.env.start_x, self.env.start_y)
        self.total_step = 0
        self.action_space = self.robot.action_space

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
        self.total_step += 1
        return self.robot.step(action_type)

    def render(self):
        """
        Draw environment and robot on the screen.
        """
        # Draw robot
        self.env.map = cv2.circle(self.env.map, (int(self.robot.x), int(self.robot.y)),
                                  color=(0, 0, 255), radius=self.robot.radius, thickness=-1)
        cv2.imshow("lab", self.env.map)
        # Erase previous robot
        self.env.map = cv2.circle(self.env.map, (int(self.robot.x), int(self.robot.y)),
                                  color=(255, 255, 255), radius=self.robot.radius, thickness=-1)
        cv2.waitKey()

    def close(self):
        """
        Close image and finish return
        """
        pass
