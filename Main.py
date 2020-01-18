import random
import time
import math

import Simulator


class RandomAgent(object):
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, inp):
        return random.choice(self.action_space)


if __name__ == "__main__":
    sim = Simulator.Simulator("circle", "images/maze00.jpg")

    sensor_data, done = sim.reset()
    agent = RandomAgent(sim.action_space)

    while True:
        time.sleep(10)
        sim.render()
        action = agent.act(sensor_data)
        sim.reset()
        sensor, done = sim.step(action)
        if done:
            break

    sim.close()
