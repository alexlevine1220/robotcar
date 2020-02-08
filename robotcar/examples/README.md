# Sample Maps
## [1] empty
    config = {
        "name": "Empty",
        "robot_type": "SQUARE",
        "sensor_types": ["BIRDEYE"],
        "width": 100,
        "height": 100,
        "start_x": 30,
        "start_y": 30,
        "goal_x": 430,
        "goal_y": 430
    }

### Solution 1: Simple 

### Solution 2: With agent

    class 
    

## [2]Random bar
    "name": "[2]bar",
    "robot_type": "SQUARE",
    "sensor_types": ["BIRDEYE"],
    "width": 500,
    "height": 500,
    "start_x": 10,
    "start_y": 30,
    "goal_x": 430,
    "goal_y": 430,
    "obstacles": [
        {
        "type": "RECTANGLE",
        "x1":200,
        "y1":300,
        "x2":300,
        "y2":350
        }
    ]
    }

### BFS