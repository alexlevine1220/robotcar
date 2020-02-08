import robotcar
from robotcar.robots import Squarebot
import random
import time
import math
from collections import deque


class BfsAgent:
    def __init__(self, sensor_data):
        env = sensor_data["grid"]
        start_x = sensor_data["x"]
        start_y = sensor_data["y"]
        goal_x = sensor_data["goal_x"]
        goal_y = sensor_data["goal_y"]
        parent = {}
        q = deque()
        cur = (start_x, start_y)
        q.append(cur)

        while len(q) != 0:
            (x, y) = q.popleft()
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (env[x + i][y + j] == robotcar.Env.SAFE).all() and (x + i, y + j) not in parent:
                    parent[(x + i, y + j)] = (x, y)
                    q.append((x + i, y + j))

        self.saved_action = deque(cur)

        count = 500
        while cur in parent and cur != (goal_x, goal_y):
            count -= 1
            if count == 0:
                break
            if cur[0] == parent[cur][0] + 1:
                self.saved_action.append(Squarebot.RIGHT)
            elif cur[0] == parent[cur][0] - 1:
                self.saved_action.append(Squarebot.LEFT)
            elif cur[1] == parent[cur][1] + 1:
                self.saved_action.append(Squarebot.DOWN)
            elif cur[1] == parent[cur][1] - 1:
                self.saved_action.append(Squarebot.UP)
            cur = parent[cur]
        print(self.saved_action)

    def act(self, sensor_data):
        return self.saved_action.pop()


if __name__ == "__main__":
    config = {
        "name": "[2]bar",
        "robot_type": "SQUARE",
        "sensor_types": ["BIRDEYE"],
        "width": 500,
        "height": 500,
        "start_x": 200,
        "start_y": 200,
        "goal_x": 450,
        "goal_y": 400,
        "obstacles": [
            {
                "type": "RECTANGLE",
                "x1": 200,
                "y1": 300,
                "x2": 300,
                "y2": 350
            }
        ]
    }

    sim = robotcar.Simulator(config, debug=True)

    sensor_data, done = sim.reset()

    right = 200
    up = 200

    while True:
        sim.render()
        if right > 0:
            sensor, done = sim.step("RIGHT")
            right -= 1
        elif up > 0:
            up -= 1
            sensor, done = sim.step("UP")
        if done != 0:
            print("the agent finisehd after " + done + " step")
