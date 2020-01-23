import random
import time
import math

from Constants import BLANK
from Simulator import Simulator


class BfsAgent:
    """ Used with circle + birdeye

    Arguments:
        object {} -- [description]

    Returns:
        [type] -- [description]
    """

    def __init__(self, action_space, env):
        self.action_space = action_space
        self.env = env
        self.count = 0
        self.saved_action = []
        self.parent = {}
        print(map)
        print(self.parent)
        self.bfs(env.start_x, env.start_y)

    def bfs(self, x, y):
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if self.env.type(x + i, y + j) == "BLANK" and (x + i, y + j) not in self.parent.keys():
                print(x + i, y + i)
                self.parent[(x + i, y + j)] = (x, y)
                self.bfs(x + i, y + i)

    def act(self):
        return 0
        #self.count += 1
        # return self.saved_action[self.count - 1]


class RandomAgent:
    """[summary]

    Returns:
        [type] -- [description]
    """

    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, sensor):
        return random.choice(self.action_space)


if __name__ == "__main__":
    sim = Simulator("square", "birdeye", "images/maze00.jpg", debug=True)

    sensor_data, done = sim.reset()
    agent = BfsAgent(sim.action_space, sim.env)

    sim.reset()
    while True:
        sim.render()
        action = agent.act()
        sensor, done = sim.step(action)

        if done:
            break

    sim.close()
