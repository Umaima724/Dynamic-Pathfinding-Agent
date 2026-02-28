# algorithms.py

import math
import heapq


def manhattan(a, b):
    return abs(a.row - b.row) + abs(a.col - b.col)


def euclidean(a, b):
    return math.sqrt((a.row - b.row) ** 2 + (a.col - b.col) ** 2)


def reconstruct_path(current):
    path = []
    while current.parent:
        path.append(current)
        current = current.parent
    return path
def a_star(grid, start, goal, heuristic):
    count = 0
    open_set = []
    heapq.heappush(open_set, (0, count, start))

    start.g = 0
    start.f = heuristic(start, goal)

    visited_nodes = []

    while open_set:
        current = heapq.heappop(open_set)[2]
        visited_nodes.append(current)

        if current == goal:
            return reconstruct_path(goal), visited_nodes

        for neighbor in grid.get_neighbors(current):
            temp_g = current.g + 1

            if temp_g < neighbor.g:
                neighbor.parent = current
                neighbor.g = temp_g
                neighbor.h = heuristic(neighbor, goal)
                neighbor.f = neighbor.g + neighbor.h

                count += 1
                heapq.heappush(open_set, (neighbor.f, count, neighbor))

    return None, visited_nodes