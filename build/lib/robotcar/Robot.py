import math
from Constants import Color
from time import sleep
from cv2 import cv2


class Robot:
    def __init__(self, robot_type, sensor_type, env, x, y, debug):
        """
        Params:
            __env__ (3d_nparray): (row, col, channel) np array where the robot resides
            robot_type (string) : read robot_types in README
            sensor_type (string): read sensor_type in README
            x (float): x position of the robot
            y (float): y position of the robot
        """
        self.__env = env
        self.sensor_type = sensor_type
        self.robot_type = robot_type
        self.debug = debug

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
        Params:
            action (string): action robot takes in this step
        Returns:
            sensor_data (object): sensored data from robot
            done (bool): checked whether robot reached the goal
        """

        new_x = self.x
        new_y = self.y

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

            sensor_data = self.sense(self.x, self.y)
            done = (self.__env.map[int(self.x),
                                   int(self.y)] == Color.GOAL).all()

            return sensor_data, done

    def sense(self, x, y):
        """
        Attributes:
            x (float): current x position of sensor
            y (float): current y position of sensor
        Returns:
            data (Objects): sensed data
        """

        if self.sensor_type == "birdeye":
            return self.__env
        elif self.sensor_type == "rays":
            """
            data = [self.sensor_range] * self.sensor_count
            for i in range(self.sensor_count):
                angle = -self.sensor_angle / 2 + \
                    (self.sensor_angle / (self.sensor_count - 1)) * i
                for length in range(self.sensor_range):
                    ray_x = int(x + math.cos(angle) * length)
                    ray_y = int(y + math.sin(angle) * length)
                    if (self.__env.map[ray_x][ray_y] == Color.OBSTACLE).all():
                        data[i] = length
                        break
            """
            return 0
        else:
            return 0

    def draw(self):
        """ Draw Robot on the map

        Returns:
            map (3d_with_map) : [description]
        """
        if self.robot_type == "square":
            return cv2.rectangle(self.__env.map, (int(self.x - self.side / 2), int(self.y - self.side / 2)),
                                 (int(self.x + self.side / 2), int(self.y + self.side / 2)), color=Color.ROBOT, thickness=-1)
        elif self.robot_type == "circle":
            return cv2.circle(self.__env.map, (self.x, self.y), color=Color.ROBOT, radius=5, thickness=-1)
        else:
            # TODO
            return 0

    def reset(self):
        """
        Returns:
            sensor : sensor data from robot
            done :   0 if not finish, otherwise the number of step taken
        """
        return self.sense(self.x, self.y), 0
