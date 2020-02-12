from cv2 import cv2
from time import time

from robotcar.core import Sensor, Robot
from robotcar.robots import *
from robotcar.sensors import *
from robotcar.map import Map

from vtkplotter import Box, show


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
        self.map = Map(map_type)
        self.robot = self.create_robot(robot_type, sensor_types,
                                       self.map.start_x, self.map.start_y)
        self.total_step = 0
        self.debug = debug
        self.world = Box([self.map.map_width / 2, self.map.map_height/2, 10/2],
                         self.map.map_width, self.map.map_height, 10).wireframe()
        # show(self.world, axes=1, bg="white", viewup="z", interactive=0)

        self.vt_boxes = ()

        for obs in self.map.obstacles:
            ob = Box(obs.center, obs.width, obs.height,
                     10, size=(), c='black', alpha=1)
            self.vt_boxes += (ob, )

        self.vt_goal = Box((self.map.goal_x, self.map.goal_y, 0),
                           10, 10, 10, size=(), c="r", alpha=1)

        self.vt_car = Box((0, 0, 0), 10, 10, 10, size=(),
                          c='b', alpha=1)

    def create_robot(self, robot_type, sensor_types, start_x, start_y):
        sensors = []
        for sensor_type in sensor_types:
            sensors.append(self.create_sensor(sensor_type))
        if robot_type == Robot.SQUARE:
            return Squarebot(self.map, sensors, start_x, start_y)

    def create_sensor(self, sensor_type):
        if sensor_type == Sensor.BIRDEYE:
            return Birdeye(self.map)

    def reset(self):
        """ Reset robot to the start position
        Returns:
            sensor  : sensor data from robot
            done    : 0 if not done, otherwise total_step
        """

        self.robot._x = self.map.start_x
        self.robot._y = self.map.start_y
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
        if self.robot._x == self.map.goal_x and self.robot._y == self.map.goal_y:
            done = self.total_step
        else:
            done = 0
        return self.robot.step(action_type), done

    def render(self):
        """ Draw map and robot on the screen.
        """

        # map = self.map.get_map()
        # map = self.robot.draw(map)
        # cv2.imshow("lab", map)
        # cv2.waitKey(1)
        self.vt_car.pos(self.robot._x, self.robot._y, 0)
        show(self.vt_car, self.vt_boxes, self.vt_goal)
