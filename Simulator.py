from Environment import Environment
from Robot import Robot
from cv2 import cv2
from time import time


class Simulator:
    """ Simulator stores environment, robot and keep tracks of movement

    Attributes:
        env (Environment) : Where robot resides
        robot (Robot) : Simulating robot 
        total_step (int) : number of steps taken by Tobot
        debug (bool) : whether print debug information (default: {False})
        start_time (int) : start time in microsecond
    """

    def __init__(self, robot_type, sensor_type, map_path, debug=False):
        """ Constructor for simulator

        Arguments:
            robot_type (string) -- possible robot_types are listed in README
            sensor_type (string) -- possible sensor_types are listed in README
            map_path (string) -- "/path/to/mapfile.jpg/"
            debug (bool) -- whether print debug information (default: {False})
        """
        self.env = Environment(map_path)
        self.robot = Robot(robot_type, sensor_type, self.env,
                           self.env.start_x, self.env.start_y, debug)
        self.total_step = 0
        self.debug = debug
        self.start_time = time()
        self.create_time = time()
        self.total_step_time = 0
        self.last_render_time = 0

    def reset(self):
        """ Reset robot to the start position
        Returns:
            sensor  : sensor data from robot
            done    : 0 if not done, otherwise total_step
        """

        self.robot.x = self.env.start_x
        self.robot.y = self.env.start_y
        self.total_step = 0
        return self.robot.sense(self.robot.x, self.robot.y), 0

    def step(self, action_type):
        """ Take one step for robot 
        Args:
            action_type (string): choose action
        Returns:
            sensor_data (object): sensor data from robot
            done        (int): 0 if not done, otherwise total_step
        """
        if self.total_step == 0:
            self.create_time = time() - self.start_time

        self.total_step += 1
        if self.robot.x == self.env.goal_x and self.robot.y == self.env.goal_y:
            print(self.robot.robot_type, "Robot Summary")
            print("Total step : ", self.total_step)
            print("Time for Create : ", self.create_time)
            print("Time for Total Step : ", self.total_step_time)
            done = self.total_step
        else:
            done = 0
        return self.robot.step(action_type), done

    def render(self):
        """ Draw environment and robot on the screen.
        """

        if self.last_render_time != 0:
            self.total_step_time += (time() - self.last_render_time)
        # Draw robot
        if self.debug:
            cv2.imshow("lab", self.robot.draw())
            cv2.waitKey(1)
        self.last_render_time = time()
