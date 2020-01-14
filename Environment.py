import pygame
import random

SCREEN_X = 1000
SCREEN_Y = 1000
DELAY_MILLI = 100

CAR_WIDTH = 30
CAR_HEIGHT = 30
RECT_WIDTH = 50
RECT_HEIGHT = 50
x = (SCREEN_X / 2)
y = (SCREEN_Y / 2)
SPEED = 5

print("Enter the number rectangles between 1 and 10: ")
numRects = input()
valid = True
while(valid):
    if(numRects.isdigit() == False):
        print("Error, user input was not a number.")
        print("Enter the number rectangles between 1 and 10: ")
        numRects = input()
    else:
        numRects = int(numRects)

        if (numRects < 1 or numRects > 10):
            print("Error, value entered is out of bounds.")
            print("Enter the number rectangles between 1 and 10: ")
            numRects = input()
        else:
            valid = False

rectCoordinates = []
for i in range(numRects):
    rX = random.randint(0 + CAR_WIDTH, SCREEN_X - CAR_WIDTH)
    rY = random.randint(0 + CAR_WIDTH, SCREEN_X - CAR_WIDTH)
    rectCoordinates.append((rX, rY))


pygame.init()

screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("First Game")

running = True
while running:
    pygame.time.delay(DELAY_MILLI)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if (x - SPEED > 0):
            x -= SPEED
    if keys[pygame.K_RIGHT]:
        if (x + SPEED + CAR_WIDTH < SCREEN_X):
            x += SPEED
    if keys[pygame.K_UP]:
        if (y - SPEED > 0):
            y -= SPEED
    if keys[pygame.K_DOWN]:
        if (y + SPEED + CAR_HEIGHT < SCREEN_Y):
            y += SPEED

    screen.fill((0, 0, 0))

    for i in range(len(rectCoordinates)):
        rX, rY = rectCoordinates[i]
        pygame.draw.rect(screen, (0, 255, 0), (rX, rY, RECT_WIDTH, RECT_HEIGHT))

    pygame.draw.rect(screen, (255, 0, 0), (x, y, CAR_WIDTH, CAR_HEIGHT))
    pygame.display.update()

pygame.quit()
