# grid.py

import random
from node import Node


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.grid = [[Node(r, c) for c in range(cols)] for r in range(rows)]

        self.start = self.grid[0][0]
        self.goal = self.grid[rows - 1][cols - 1]

        self.start.is_start = True
        self.goal.is_goal = True

    def reset_algorithm(self):
        for row in self.grid:
            for node in row:
                node.reset_algorithm()

    def toggle_wall(self, row, col):
        node = self.grid[row][col]
        if not node.is_start and not node.is_goal:
            node.is_wall = not node.is_wall

    def generate_random_obstacles(self, density):
        for row in self.grid:
            for node in row:
                if not node.is_start and not node.is_goal:
                    node.is_wall = random.random() < density

    def get_neighbors(self, node):
        neighbors = []
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for dr, dc in directions:
            r = node.row + dr
            c = node.col + dc

            if 0 <= r < self.rows and 0 <= c < self.cols:
                neighbor = self.grid[r][c]
                if not neighbor.is_wall:
                    neighbors.append(neighbor)

        return neighbors