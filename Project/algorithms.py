# algorithms.py

import heapq
import math


def manhattan(a, b):
    return abs(a.row - b.row) + abs(a.col - b.col)


def euclidean(a, b):
    return math.sqrt((a.row - b.row)**2 + (a.col - b.col)**2)


def reconstruct_path(goal):
    path = []
    current = goal
    while current.parent:
        path.append(current)
        current = current.parent
    return path


def search(grid, start, goal, heuristic, use_g_cost=True):
    open_set = []
    count = 0
    heapq.heappush(open_set, (0, count, start))

    start.g = 0
    start.f = heuristic(start, goal)

    visited_nodes = []

    while open_set:
        current = heapq.heappop(open_set)[2]
        current.is_visited = True
        visited_nodes.append(current)

        if current == goal:
            return reconstruct_path(goal), visited_nodes

        for neighbor in grid.get_neighbors(current):

            temp_g = current.g + 1

            if use_g_cost:
                new_f = temp_g + heuristic(neighbor, goal)
            else:
                new_f = heuristic(neighbor, goal)

            if new_f < neighbor.f:
                neighbor.parent = current
                neighbor.g = temp_g
                neighbor.f = new_f
                neighbor.is_frontier = True
                count += 1
                heapq.heappush(open_set, (neighbor.f, count, neighbor))

    return None, visited_nodes