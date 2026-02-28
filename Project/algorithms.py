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