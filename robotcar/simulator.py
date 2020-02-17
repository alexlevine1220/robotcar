from cv2 import cv2
from time import time
from geometry import Rectangle, create_geometry
from collision import Collision
from vtkplotter import Box, show
from robot import *
from sensor import *
import numpy as np


class Simulator:
    def __init__(self, config, debug=False):

        robot_type = config["robot_type"]
        sensor_types = config["sensor_types"]
        self.width = config["width"]
        self.height = config["height"]
        self.start_x = config["start_x"]
        self.start_y = config["start_y"]
        self.goal_x = config["goal_x"]
        self.goal_y = config["goal_y"]
        self.map = np.ones((self.width, self.height)) / 2
        self.obstacles = []
        if "obstacles" in config:
            for obs in config["obstacles"]:
                self.obstacles.append(create_geometry(obs))
        self.collision = Collision(self.width, self.height, self.obstacles)

        self.robot = self.create_robot(
            robot_type, sensor_types, self.start_x, self.start_y)
        self.world = Box([self.width / 2, self.height/2, 10/2],
                         self.width, self.height, 10).wireframe()
        show(self.world, axes=1, bg="white", viewup="z", interactive=0)

        # print for vtk plotter
        self.vt_boxes = ()

        if debug:
            for obs in self.obstacles:
                self.vt_boxes += (obs.vtk_object('black'), )

        self.vt_goal = Box((self.goal_x, self.goal_y, 0),
                           10, 10, 10, size=(), c="b", alpha=1)

        self.vt_car = Box((0, 0, 0), 10, 10, 10, size=(), c='r', alpha=1)

    def create_robot(self, robot_type, sensor_types, start_x, start_y):
        sensors = []
        for sensor_type in sensor_types:
            sensors.append(self.create_sensor(sensor_type))
        if robot_type == Robot.SQUARE:
            return Squarebot(self.collision, sensors, start_x, start_y)

    def create_sensor(self, sensor_type):
        if sensor_type == Sensor.BIRDEYE:
            return Birdeye(self.collision)

    def reset(self):
        self.robot.x = self.start_x
        self.robot.y = self.start_y
        self.total_step = 0
        return self.robot.sense(), 0, self.goal_x, self.goal_y

    def step(self, action_type):
        self.total_step += 1

        if self.robot.x == self.goal_x and self.robot.y == self.goal_y:
            done = self.total_step
        else:
            done = 0

        return self.robot.step(action_type), done

    def running(self):
        return True

    def render(self):
        vt_robots = self.robot.vtk_object('red')
        show(vt_robots, self.vt_boxes, self.vt_goal)
