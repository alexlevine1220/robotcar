import math
from Constants import ROBOT, OBSTACLE, GOAL
from time import sleep
from cv2 import cv2


class Robot:
    def __init__(self, robot_type, sensor_type, env, x, y, debug):
        """
        :param env: (row, col, channel) np array where the robot resides
        :param robot_type: read robot_types in README
        :param sensor_type: read sensor_type in README
        :param x: x position of the robot
        :param y: y position of the robot
        """
        self.env = env
        self.sensor_type = sensor_type
        self.robot_type = robot_type

        if debug:
            print("Sensor Types of " + sensor_type + " is created")

        # Configuring sensor
        if sensor_type == "birdeye":
            pass
        elif sensor_type == "rays":
            self.sensor_angle = 360
            self.sensor_count = 4
            self.sensor_range = 100

        # Configuring robot
        if robot_type == "circle":
            self.radius = 5
            self.action_space = ["move", "turn_left", "turn_right"]
            self.watching = 0
            self.x = x
            self.y = y
        if robot_type == "square":
            self.action_space = ["move_left",
                                 "move_right", "move_up", "move_down"]
            self.x = x
            self.y = y
            self.side = 5
        elif robot_type == "four_wheel":
            # TODO IMPLEMENT AS REALISTIC
            self.x = x
            self.y = y

    def step(self, action):
        """
        :param action: action robot takes in this step
        :return: sensor data from robot
        ""[summary]
        Returns:
            [type] -- [description]
        """

        new_x = 0
        new_y = 0

        if self.robot_type == "square":
            if action == "move_left":
                new_x = self.x - 1
                new_y = self.y
            elif action == "move_right":
                new_x = self.x + 1
                new_y = self.y
            elif action == "move_up":
                new_x = self.x
                new_y = self.y - 1
            elif action == "move_down":
                new_x = self.x
                new_y = self.y + 1
            if True:
                self.x = new_x
                self.y = new_y
        elif self.robot_type == "circle":
            if action == "move":
                new_x = self.x + math.sin(self.watching)
                new_y = self.y + math.cos(self.watching)
            elif action == "turn_left":
                self.watching -= 0.1
            elif action == "turn_right":
                self.watching += 0.1

            data = self.sense(self.x, self.y)
            done = (self.env.map[int(self.x), int(self.y)] == GOAL).all()

            return data, done

    def sense(self, x, y):
        """
        :param x: current x position of sensor
        :param y: current y position of sensor
        :return: sensed data
        """

        if self.sensor_type == "birdeye":
            return self.env.map
        elif self.sensor_type == "rays":
            data = [self.sensor_range] * self.sensor_count
            for i in range(self.sensor_count):
                angle = -self.sensor_angle / 2 + \
                    (self.sensor_angle / (self.sensor_count - 1)) * i
                for length in range(self.sensor_range):
                    ray_x = int(x + math.cos(angle) * length)
                    ray_y = int(y + math.sin(angle) * length)
                    if (self.env.map[ray_x][ray_y] == OBSTACLE).all():
                        data[i] = length
                        break

            return data
        else:
            return 0

    def draw(self, erase=False):
        if self.robot_type == "square":
            if erase:
                return cv2.rectangle(self.env.map, (self.x - side / 2, self.y - side / 2),
                                     (self.x + side / 2, self.y + side / 2), color=BLANK, thickness=-1)
            else:
                return cv2.rectangle(self.env.map, (self.x - side / 2, self.y - side / 2),
                                     (self.x + side / 2, self.y + side / 2), color=ROBOT, thickness=-1)
        elif self.robot_type == "circle":
            if erase:
                return cv2.circle(self.env.map, (self.x, self.y), color=BLANK, radius=5, thickness=-1)
            else:
                return cv2.circle(self.env.map, (self.x, self.y), color=ROBOT, radius=5, thickness=-1)
        else:
            # TODO
            return 0

    def reset(self):
        """
        :return:
        sensor  sensor data from robot
        done    0 if not finish, otherwise the number of step taken
        """
        #print(self.sense(self.x, self.y))
        return self.sense(self.x, self.y), 0
