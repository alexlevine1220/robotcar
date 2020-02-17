from collections import deque

Adj = {
    1: [2],
    2: [1, 3, 4],
    3: [2, 5],
    4: [2],
    5: [3]
}


def computeBFStree(Adj, S):
    """
    Arguments:
        Adj {dictionary} : {v : [v1, v2]} where v and v1 / v2 are neighbors
        S {start} : start Node
    Returns:
        dictionary : {v1 : v2} where v2 is parent of v1
    """
    parents = {}
    Q = [S]
    while len(Q) != 0:
        cur = Q.pop(0)
        for n in Adj[cur]:
            if n not in parents:
                Q.append(n)
                parents[n] = cur
    return parents


def computeBFSpath(Adj, S, G):
    """
    Arguments:
        Adj {dictionary} : {v : [v1, v2]} where v and v1 / v2 are neighbors
        S {start} : start Node
        G {goal} : goal Node
    Returns:
        list : path from S to G
    """

    paths = [G]
    parents = computeBFStree(Adj, S)
    current = G
    while current != S and current in parents:
        current = parents[current]
        paths = [current] + paths
    if current != S:
        return "No Path"
    return paths


print(computeBFSpath(Adj, 1, 5))
