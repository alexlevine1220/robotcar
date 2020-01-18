import math
import Sensor
from Constants import OBSTACLE, GOAL


class Robot:
    def __init__(self, env, robot_type, x, y):
        """

        :param env: 2d np array where the robot resides
        :param robot_type:
        :param x: x position of the robot
        :param y: y position of the robot
        """
        self.env = env

        # able to move forward and rotate
        if "circle" in robot_type:
            self.sensor = Sensor.Sensor(self.env,
                {
                    "type": "rays",
                    "angle": 90,    # angle of sensor
                    "number": 5,
                    "range": 100
                },
            )
            self.radius = 5
            self.action_space = ["move", "turn_left", "turn_right"]
            self.watching = 0
            self.x = x
            self.y = y

    def step(self, action):
        """
        :param action:
        :return: sensor data from robot
        """
        print(action)

        if action == "move":
            new_x = self.x + math.sin(self.watching)
            new_y = self.y + math.cos(self.watching)
            # Collision Checking
            for d in range(360):
                corner_x = new_x + math.cos(d) * self.radius
                corner_y = new_y + math.sin(d) * self.radius

        elif action == "turn_left":
            self.watching -= 0.1
        elif action == "turn_right":
            self.watching += 0.1

        data = self.sensor.sense(self.x, self.y)
        done = (self.env.map[self.x, self.y] == GOAL).all()

        return data, done

    def reset(self):
        """
        :return:
        sensor  sensor data from robot
        done    0 if not finish, otherwise the number of step taken
        """
        return self.sensor.sense(self.x, self.y), 0
