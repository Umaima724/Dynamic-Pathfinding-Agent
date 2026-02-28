# node.py

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col

        self.is_wall = False
        self.is_start = False
        self.is_goal = False
        self.is_visited = False
        self.is_frontier = False
        self.is_path = False

        self.g = float("inf")
        self.h = 0
        self.f = float("inf")
        self.parent = None

    def reset_algorithm(self):
        self.is_visited = False
        self.is_frontier = False
        self.is_path = False
        self.g = float("inf")
        self.h = 0
        self.f = float("inf")
        self.parent = None