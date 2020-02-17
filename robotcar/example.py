from simulator import Simulator
import random
import time
import math
from collections import deque

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
            "x": 200,
            "y": 300,
            "width": 30,
            "height": 50,
        },
        {
            "type": "RECTANGLE",
            "x": 500,
            "y": 500,
            "width": 30,
            "height": 50,
        }
    ]
}

sim = Simulator(config, debug=True)
sensor_data, done, goal_x, goal_y = sim.reset()

right = 200
up = 200

while sim.running():
    sim.render()
    if right > 0:
        sensor = sim.step("RIGHT")
        right -= 1
    elif up > 0:
        up -= 1
        sensor = sim.step("UP")
