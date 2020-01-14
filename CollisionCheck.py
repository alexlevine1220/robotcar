import numpy as np
import math

ZERO_APPROX = 0.001

""" Checks if the signal at the specified angle hits an object """
def signalCheck(rectCoordinates, rectHeight, rectWidth, rectLength, angle, x, y, z):
    distances = [(1001, -1, -1), (1001, -1, -1), (1001, -1, -1), (1001, -1, -1)]
    endPoints = []

    direction = [math.cos(angle), math.sin(angle)]
    if (math.cos(angle) <= ZERO_APPROX and math.cos(angle) >= -ZERO_APPROX):
        direction = False

    for i in range(len(rectCoordinates)):
        tX = rectCoordinates[i][0] - rectWidth / 2
        tY = rectCoordinates[i][1] - rectLength / 2
        tZ = rectCoordinates[i][2] - rectHeight / 2

        # Left vertical line intersection point
        point = segCheck((x, y), direction, (tX, tY), (tX, tY + rectHeight))

        if (point != False and tY <= point[1] and point[1] <= tY + rectHeight):
            distances[0] = (np.sqrt((point[0] - x)**2 + (point[1] - y)**2), point[0], point[1])

        # Right vertical line intersection point
        point = segCheck((x, y), direction, (tX + rectWidth, tY), (tX + rectWidth, tY + rectHeight))

        if (point != False and tY <= point[1] and point[1] <= tY + rectHeight):
            distances[1] = (np.sqrt((point[0] - x)**2 + (point[1] - y)**2), point[0], point[1])

        # Bottom horizontal line intersection point
        point = segCheck((x, y), direction, (tX, tY), (tX + rectWidth, tY))

        if (point != False and tX <= point[0] and point[0] <= tX + rectWidth):
            distances[2] = (np.sqrt((point[0] - x)**2 + (point[1] - y)**2), point[0], point[1])

        # Top horizontal line intersection point
        point = segCheck((x, y), direction, (tX, tY + rectHeight), (tX + rectWidth, tY + rectHeight))

        if (point != False and tX <= point[0] and point[0] <= tX + rectWidth):
            distances[3] = (np.sqrt((point[0] - x)**2 + (point[1] - y)**2), point[0], point[1])

        # find the shortest distance and store the index
        shortest = 1001
        coord = (-1, -1)
        for i in range(len(distances)):
            if shortest > distances[i][0]:
                shortest = distances[i][0]
                coord = (distances[i][1], distances[i][2])

        if shortest != 1001:
            endPoints.append((shortest, coord[0], coord[1]))

    return endPoints


""" Checks collisions for individual line segments """
def segCheck(start, direction, segP1, segP2):
    ret = False

    # Check if the sensor slope is undefined(vertical)
    if(direction != False):
        sensorSlope = direction[1]/direction[0]
        sensorB = start[1] - (sensorSlope * start[0])

        # Check for undefined segment slope
        if(segP1[0] - segP2[0] != 0):
            segSlope = (segP1[1] - segP2[1]) / (segP1[0] - segP2[0])

            segB = segP1[1] - (segSlope * segP1[0])

            # Check if the lines intersect
            if (segSlope != sensorSlope or sensorB == segB):
                # Check if the lines are the same. If so return the point with the shortest distance to the
                # start. If not, return the intersection point.
                if(segSlope == sensorSlope and sensorB == segB):
                    dist1 = np.sqrt((segP1[0] - start[0])**2 + (segP1[1] - start[1])**2)
                    dist2 = np.sqrt((segP2[0] - start[0])**2 + (segP2[1] - start[1])**2)

                    if(dist1 > dist2):
                        ret = segP2
                    else:
                        ret = segP1
                else:
                    # Find x intersection point
                    x = (segB - sensorB) / (sensorSlope - segSlope)

                    # Find y intersection point
                    y = (sensorSlope * x) + sensorB

                    ret = (x, y)
        else:
            # Find the intersection between the sensor line and the x coordinate of the segment
            y = (sensorSlope * segP1[0]) + sensorB

            ret = (segP1[0], y)
    else:
        # Check for undefined segment slope
        if(segP1[0] - segP2[0] == 0):
            # Check if x coordinates are the same
            if(segP1[0] == start[0]):
                # Find the point with the shortest distance to the start
                dist1 = np.sqrt((segP1[0] - start[0])**2 + (segP1[1] - start[1])**2)
                dist2 = np.sqrt((segP2[0] - start[0])**2 + (segP2[1] - start[1])**2)

                if(dist1 > dist2):
                    ret = segP2
                else:
                    ret = segP1
        else:
            segSlope = (segP1[1] - segP2[1]) / (segP1[0] - segP2[0])

            segB = segP1[1] - (segSlope * segP1[0])

            # Find the intersection between the sensor x coordinate and the segment
            y = (segSlope * start[0]) + segB

            ret = (start[0], y)

    return ret


""" Checks if the car hits the obsticles """
def rectCheck(rectCoordinates, x, y, z, rectHeight, rectWidth, rectLength, carHeight, carWidth, carLength, direction):
    nX = x - carWidth / 2
    nY = y - carLength / 2
    nZ = z - carLength / 2

    ret = False
    top = False

    if direction == 0:
        for i in range(len(rectCoordinates)):
            tX = rectCoordinates[i][0] - rectWidth / 2
            tY = rectCoordinates[i][1] - rectLength / 2
            tZ = rectCoordinates[i][2] - rectHeight / 2

            if(tY <= nY and tY + rectLength >= nY):
                if(tX <= nX and tX + rectWidth >= nX):
                    ret = True

        if ret == False:
            nY = nY + carHeight
            for i in range(len(rectCoordinates)):
                tX = rectCoordinates[i][0] - rectWidth / 2
                tY = rectCoordinates[i][1] - rectLength / 2
                tZ = rectCoordinates[i][2] - rectHeight / 2

                if(tY <= nY and tY + rectLength >= nY):
                    if(tX <= nX and tX + rectWidth >= nX):
                        ret = True

    if direction == 1:
        for i in range(len(rectCoordinates)):
            tX = rectCoordinates[i][0] - rectWidth / 2
            tY = rectCoordinates[i][1] - rectLength / 2
            tZ = rectCoordinates[i][2] - rectHeight / 2

            if(tY <= nY and tY + rectLength >= nY):
                if(tX <= nX and tX + rectWidth >= nX):
                    ret = True

        if ret == False:
            nX = nX + carWidth
            for i in range(len(rectCoordinates)):
                tX = rectCoordinates[i][0] - rectWidth / 2
                tY = rectCoordinates[i][1] - rectLength / 2
                tZ = rectCoordinates[i][2] - rectHeight / 2

                if(tY <= nY and tY + rectLength >= nY):
                    if(tX <= nX and tX + rectWidth >= nX):
                        ret = True

    return ret
