# grid.py
class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col

        self.is_wall = False
        self.is_start = False
        self.is_goal = False

        # For algorithms (later)
        self.g = float("inf")
        self.h = 0
        self.f = float("inf")
        self.parent = None

    def reset(self):
        self.g = float("inf")
        self.h = 0
        self.f = float("inf")
        self.parent = None


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.grid = [[Node(r, c) for c in range(cols)] for r in range(rows)]

        self.start = None
        self.goal = None

    def set_start(self, row, col):
        node = self.grid[row][col]
        node.is_start = True
        self.start = node

    def set_goal(self, row, col):
        node = self.grid[row][col]
        node.is_goal = True
        self.goal = node

    def toggle_wall(self, row, col):
        node = self.grid[row][col]
        if not node.is_start and not node.is_goal:
            node.is_wall = not node.is_wall

    def get_neighbors(self, node):
        neighbors = []
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for dr, dc in directions:
            r = node.row + dr
            c = node.col + dc

            if 0 <= r < self.rows and 0 <= c < self.cols:
                if not self.grid[r][c].is_wall:
                    neighbors.append(self.grid[r][c])

        return neighbors