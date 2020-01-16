import Environment
import random
import time


class RandomAgent(object):
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, inp):
        return random.choice(self.action_space)


if __name__ == "__main__":
    env = Environment.Environment("circle", "basic", "images/maze00.jpg")
    sensor, done = env.reset()
    agent = RandomAgent(env.action_space)

    while True:
        time.sleep(0.1)
        env.render()
        action = agent.act(sensor)
        print(type(env), action)
        env.reset()
        sensor, done = env.step(action)
        # Use sensor data to take plan action
        #if done:
        #    break

    env.close()
