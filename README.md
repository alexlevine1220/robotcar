Types of Sensor :

    - birdeye()
        - just returns map
    - continuous(angle)
        - can use getDistance(angle) to calculate the closest distance
    - rays(angle, n_rays)
        - only have finite number of angles you can get distance from

Types of robot Shape :

    - circle(radius)
        - action_space = ["move", "rotate_left", "rotate_right"]
    - square(length)
        - action_space = ["move_left", "move_right", "move_up", "move_down"]
    - car(radius)
        - action_space = ["accel_left", "accel", "accel_right"]
