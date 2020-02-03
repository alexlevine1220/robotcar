from cv2 import cv2
from time import time

from robotcar.core import Sensor, Robot
from robotcar.robots import *
from robotcar.sensors import *
from robotcar.map import Map


class Simulator:
    """ Simulator stores environment, robot and keep tracks of movement

    Attributes:
        env (Environment) : Where robot resides
        robot (Robot) : Simulating robot 
        total_step (int) : number of steps taken by Tobot
        debug (bool) : whether print debug information (default: {False})
        start_time (int) : start time in microsecond
    """

    def __init__(self, robot_type, sensor_types, map_type, debug=False):
        """ Constructor for simulator

        Arguments:
            robot_type (str) : available robot_types are listed in README
            sensors ([str]) : available sensor_types are listed in README
            map_type (str) : Read README.md to learn more
            debug (bool) : whether print debug information (default: {False})
        """
        self.env = Map(map_type)
        self.robot = self.create_robot(robot_type, sensor_types,
                                       self.env.start_x, self.env.start_y)
        self.total_step = 0
        self.debug = debug

    def create_robot(self, robot_type, sensor_types, start_x, start_y):
        sensors = {}
        for sensor_type in sensor_types:
            sensors[sensor_type] = self.create_sensor(sensor_type)
        if robot_type == Robot.SQUARE:
            return Squarebot(self.env, sensors, start_x, start_y)

    def create_sensor(self, sensor_type):
        if sensor_type == Sensor.BIRDEYE:
            return Birdeye(self.env)

    def reset(self):
        """ Reset robot to the start position
        Returns:
            sensor  : sensor data from robot
            done    : 0 if not done, otherwise total_step
        """

        self.robot._x = self.env.start_x
        self.robot._y = self.env.start_y
        self.total_step = 0
        return self.robot.sense(), 0

    def step(self, action_type):
        """ Take one step for robot 
        Args:
            action_type (string): choose action
        Returns:
            sensor_data (object): sensor data from robot
            done (int): 0 if not done, otherwise total_step
        """

        self.total_step += 1
        if self.robot._x == self.env.goal_x and self.robot._y == self.env.goal_y:
            done = self.total_step
        else:
            done = 0
        return self.robot.step(action_type), done

    def render(self):
        """ Draw environment and robot on the screen.
        """

        map = self.env.get_map()
        map = self.robot.draw(map)
        cv2.imshow("lab", map)
        cv2.waitKey(1)
