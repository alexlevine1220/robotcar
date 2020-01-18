import math
import Sensor
from Constants import OBSTACLE, GOAL
from time import sleep


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
        :param action: action robot takes in this step
        :return: sensor data from robot
        """
        print(action)

        if action == "move":
            new_x = self.x + math.sin(self.watching)
            new_y = self.y + math.cos(self.watching)

            print(self.watching, math.sin(self.watching))

            hit = False

            # Collision Checking
            for d in range(1, 360):
                corner_x = new_x + math.cos(2 * math.pi * d / 360) * self.radius
                corner_y = new_y + math.sin(2 * math.pi * d / 360) * self.radius

                if (self.env.map[int(corner_x)][int(corner_y)] == OBSTACLE).all():
                    hit = True
                    print("HIT")
                    break

            if not hit:
                self.x = new_x
                self.y = new_y
        elif action == "turn_left":
            self.watching -= 0.1
        elif action == "turn_right":
            self.watching += 0.1

        data = self.sensor.sense(self.x, self.y)
        done = (self.env.map[int(self.x), int(self.y)] == GOAL).all()

        return data, done

    def reset(self):
        """
        :return:
        sensor  sensor data from robot
        done    0 if not finish, otherwise the number of step taken
        """
        return self.sensor.sense(self.x, self.y), 0
