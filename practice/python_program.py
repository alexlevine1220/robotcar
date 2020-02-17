# A13528608
# HELPER

# %%
def distance(p1, p2):
    """Calculate distance between p1, p2.

    Args:
        p1 (float, float): coordinates of p1
        p2 (float, float): coordinates of p2

    Returns:
        float: distance
    """
    return ((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2) ** 0.5


def computeLineThroughTwoPoints(p1, p2):
    """

    Args:
        p1 (float, float): coordinates of p1
        p2 (float, float): coordinates of p2

    Returns:
        (float, float, float): a, b, c that satisfies a x + b y + c = 0 where a ^ 2 + b ^ 2 = 1
    """
    a = p1[1] - p2[1]
    b = p2[0] - p1[0]
    c = (p1[0] - p2[0]) * p1[1] + (p2[1] - p1[1]) * p1[0]

    norm = (a ** 2 + b ** 2) ** 0.5

    return (a / norm, b / norm, c / norm)


def calculateShortestPoint(q, p1, p2):
    """Calculates shortest Point between point q and segment (p1, p2)

    Args:
        q (float, float): point coordinate
        p1 (float, float): one point coordinate of segment
        p2 (float, float): another point coordinate of segment

    Returns:
        (float, float): shortest distance
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = q

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:
        return -1, -1

    u = ((x3 - x1) * dx + (y3 - y1) * dy) / (dx * dx + dy * dy)

    if u > 1:
        u = 1
    elif u < 0:
        u = 0

    return x1 + u * dx, y1 + u * dy


def distance_point_segment(q, p1, p2):
    return distance(calculateShortestPoint(q, p1, p2), q)


def computeDistancePointToPolygon(P, q):
    """ calculate distance from a point to polygon

    Args:
        P ([float, float]): list of points consists of polygon
        q ([]): [description]

    Returns:
        [type]: [description]
    """

    if len(P) < 3:
        raise(Exception("Polygon must have more than 2 vertices"))

    minDist = float('inf')
    for i in range(len(P)):
        minDist = min(minDist, distance_point_segment(
            q, P[i], P[(i + 1) % len(P)]))

    return minDist


def computeTangentVectorToPolygon(P, q):
    """
    Args:
        P ([float, float]): list of points consists of polygon
        q ([]): [description]

    Returns:
    """
    minDist = computeDistancePointToPolygon(P, q)
    indices = []

    for i in range(len(P)):
        if minDist == distance_point_segment(q, P[i], P[(i + 1) % len(P)]):
            indices.append(i)

    if len(indices) == 2:
        px, py = P[indices[1]] if distance(q, P[indices[1]]) < distance(
            q, P[(indices[1] + 1) % len(P)]) else P[(indices[1] + 1) % len(P)]
        qx, qy = q
        dx = qx - px
        dy = qy - py
        x = -dy
        y = dx
        norm = (x ** 2 + y ** 2) ** 0.5
        return x / norm, y / norm
    else:
        # segment
        a, b, c = computeLineThroughTwoPoints(
            P[indices[0]], P[(indices[0] + 1) % len(P)])
        return b, -a


q = [0, 1.1]
P = [[0, 0], [2, 0], [1, 1]]
