from vtkplotter import *
import random
import pygame
import CollisionCheck
import math
import numpy as np

rectCoordinates = [] # List holding the coordinates of rectangles
angles = [0, 90, 342] # List holding angles to send sensors out
sensorPoints = [] # List holding points to draw lines with

slope0and180 = 0
slope45andn135 = 1
slopen45and135 = -1

DEFAULT_ANGLE_DIST = 141.42
DEFAULT_NO_ANGLE_DIST = 200

# World diension constants
WORLD_X = 1000
WORLD_Y = 1000
WORLD_Z = 1000

PYGAME_WIN = 100

DELAY_MILLI = 100

MAX_DIST = 200

# Obsticle dimension constants
NUM_RECTS = 10
RECT_WIDTH = 50
RECT_LENGTH = 50
RECT_HEIGHT = 50
Z_OFFSET = 25

# Car dimenison constants
CAR_WIDTH = 30
CAR_HEIGHT = 30
CAR_LENGTH = 30
CAR_Z_OFFSET = 15

# Initial position of the car
car_x = (WORLD_X / 2)
car_y = (WORLD_Y / 2)
car_z = CAR_Z_OFFSET

car = Box((car_x, car_y, car_z), CAR_LENGTH, CAR_WIDTH, CAR_HEIGHT, size=(), c='g', alpha=1).c("red")

SPEED = 5

for i in range(NUM_RECTS):
    rX = random.randint(0 + CAR_WIDTH, WORLD_X - CAR_WIDTH)
    rY = random.randint(0 + CAR_WIDTH, WORLD_Y - CAR_WIDTH)
    rZ = Z_OFFSET
    rectCoordinates.append((rX, rY, rZ))

world = Box([WORLD_X/2,WORLD_Y/2,WORLD_Z/2], WORLD_X, WORLD_Y, WORLD_Z).wireframe()

# setup the world
pygame.init()
WORLD = pygame.display.set_mode((PYGAME_WIN, PYGAME_WIN))
show(world, axes=1, bg="white", viewup="z", interactive=0)

# Show obsticles
rect = Box(rectCoordinates[0], RECT_LENGTH, RECT_WIDTH, RECT_HEIGHT, size=(), c='g', alpha=1)
rect2 = Box(rectCoordinates[1], RECT_LENGTH, RECT_WIDTH, RECT_HEIGHT, size=(), c='g', alpha=1)
rect3 = Box(rectCoordinates[2], RECT_LENGTH, RECT_WIDTH, RECT_HEIGHT, size=(), c='g', alpha=1)
rect4 = Box(rectCoordinates[3], RECT_LENGTH, RECT_WIDTH, RECT_HEIGHT, size=(), c='g', alpha=1)
rect5 = Box(rectCoordinates[4], RECT_LENGTH, RECT_WIDTH, RECT_HEIGHT, size=(), c='g', alpha=1)
rect6 = Box(rectCoordinates[5], RECT_LENGTH, RECT_WIDTH, RECT_HEIGHT, size=(), c='g', alpha=1)
rect7 = Box(rectCoordinates[6], RECT_LENGTH, RECT_WIDTH, RECT_HEIGHT, size=(), c='g', alpha=1)
rect8 = Box(rectCoordinates[7], RECT_LENGTH, RECT_WIDTH, RECT_HEIGHT, size=(), c='g', alpha=1)
rect9 = Box(rectCoordinates[8], RECT_LENGTH, RECT_WIDTH, RECT_HEIGHT, size=(), c='g', alpha=1)
rect10 = Box(rectCoordinates[9], RECT_LENGTH, RECT_WIDTH, RECT_HEIGHT, size=(), c='g', alpha=1)

show(car, rect, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, rect10)

# Set control window text
font = pygame.font.Font('freesansbold.ttf', 8)
text = font.render('PRESS TO MOVE', True, (255, 0, 0))
textRect = text.get_rect()
textRect.center = (PYGAME_WIN // 2, PYGAME_WIN // 2)

# Animation
direction = 0
running = True
while running:
    pygame.time.delay(DELAY_MILLI)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    """ Action listeners to move the car. """
    if keys[pygame.K_LEFT]:
        direction = 0
        newX = car_x - SPEED
        if (newX > 0 and CollisionCheck.rectCheck(rectCoordinates, newX, car_y, car_z, RECT_HEIGHT, RECT_WIDTH, RECT_LENGTH, CAR_HEIGHT, CAR_WIDTH, CAR_LENGTH, direction) == False):
            car_x -= SPEED

    if keys[pygame.K_RIGHT]:
        direction = 0
        newX = car_x + SPEED + CAR_WIDTH
        if (newX < WORLD_X and CollisionCheck.rectCheck(rectCoordinates, newX, car_y, car_z, RECT_HEIGHT, RECT_WIDTH, RECT_LENGTH, CAR_HEIGHT, CAR_WIDTH, CAR_LENGTH, direction) == False):
            car_x += SPEED

    if keys[pygame.K_UP]:
        direction = 1
        newY = car_y + SPEED + CAR_HEIGHT
        if (newY > 0 and CollisionCheck.rectCheck(rectCoordinates, car_x, newY, car_z, RECT_HEIGHT, RECT_WIDTH, RECT_LENGTH, CAR_HEIGHT, CAR_WIDTH, CAR_LENGTH, direction) == False):
            car_y += SPEED

    if keys[pygame.K_DOWN]:
        direction = 1
        newY = car_y - SPEED
        if (newY < WORLD_Y and CollisionCheck.rectCheck(rectCoordinates, car_x, newY, car_z, RECT_HEIGHT, RECT_WIDTH, RECT_LENGTH, CAR_HEIGHT, CAR_WIDTH, CAR_LENGTH, direction) == False):
            car_y -= SPEED

    """ Mouse Click action listener. When the mouse is clicked it calculates the distances for each of the 8 signals. If the signal doesn't hit anything
        the distance is set to 500 """
    if pygame.mouse.get_pressed()[0] == True:
        start = np.array([car_x + (CAR_WIDTH/2), car_y + (CAR_HEIGHT/2)])
        distances = []
        dist = 0

    """ Drawing """
    sensorPoints = [] # Reset sensor points on every game iteration

    # Simulate sensors at the specified angles
    for i in range(len(angles)):
        radians = math.radians(angles[i])
        endPoints = CollisionCheck.signalCheck(rectCoordinates, RECT_HEIGHT, RECT_WIDTH, RECT_LENGTH, radians, car_x, car_y, car_z)

        shortP = 1001
        shortN = 1001

        # Figure out the negative and pointive points
        if(math.cos(radians) > 0):
            pointP = (DEFAULT_NO_ANGLE_DIST * math.cos(radians), DEFAULT_NO_ANGLE_DIST * math.sin(radians))
            pointN = (-pointP[0], -pointP[1])
        else:
            pointN = (DEFAULT_NO_ANGLE_DIST * math.cos(radians), DEFAULT_NO_ANGLE_DIST * math.sin(radians))
            pointP = (-pointN[0], -pointN[1])

        pointP = (pointP[0] + car_x, pointP[1] + car_y, car_z)
        pointN = (pointN[0] + car_x, pointN[1] + car_y, car_z)

        a = angles[i]
        # Check if endPoints are valid
        if (endPoints != []):
            for i in range(len(endPoints)):
                if endPoints[i][0] <= DEFAULT_NO_ANGLE_DIST:
                    if(a == 90):
                        if endPoints[i][2] <= car_y and endPoints[i][0] <= shortN:
                            shortN = endPoints[i][0]
                            pointN = (endPoints[i][1], endPoints[i][2], car_z)
                        if endPoints[i][2] >= car_y and endPoints[i][0] <= shortP:
                            shortP = endPoints[i][0]
                            pointP = (endPoints[i][1], endPoints[i][2], car_z)
                    else:
                        if endPoints[i][1] <= car_x and endPoints[i][0] <= shortN:
                            shortN = endPoints[i][0]
                            pointN = (endPoints[i][1], endPoints[i][2], car_z)
                        if endPoints[i][1] >= car_x and endPoints[i][0] <= shortP:
                            shortP = endPoints[i][0]
                            pointP = (endPoints[i][1], endPoints[i][2], car_z)
            sensorPoints.append(pointN)
            sensorPoints.append(pointP)
        else:
            sensorPoints.append(pointN)
            sensorPoints.append(pointP)

    # Create sensor lines
    lidar1 = Line(sensorPoints[0], (car_x, car_y, car_z), c='r', alpha=1, lw=1, dotted=False, res=None).c("blue")
    lidar2 = Line(sensorPoints[1], (car_x, car_y, car_z), c='r', alpha=1, lw=1, dotted=False, res=None).c("blue")
    lidar3 = Line(sensorPoints[2], (car_x, car_y, car_z), c='r', alpha=1, lw=1, dotted=False, res=None).c("blue")
    lidar4 = Line(sensorPoints[3], (car_x, car_y, car_z), c='r', alpha=1, lw=1, dotted=False, res=None).c("blue")
    lidar5 = Line(sensorPoints[4], (car_x, car_y, car_z), c='r', alpha=1, lw=1, dotted=False, res=None).c("blue")
    lidar6 = Line(sensorPoints[5], (car_x, car_y, car_z), c='r', alpha=1, lw=1, dotted=False, res=None).c("blue")

    # Updates pygame text display
    WORLD.blit(text, textRect)
    pygame.display.update()

    car.pos(car_x, car_y, car_z)
    show(car, rect, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, rect10, lidar1, lidar2, lidar3, lidar4, lidar5, lidar6)

interactive()
pygame.quit()
