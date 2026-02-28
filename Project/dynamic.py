# dynamic.py

import random


def spawn_obstacle(grid, probability=0.03):
    if random.random() < probability:
        r = random.randint(0, grid.rows - 1)
        c = random.randint(0, grid.cols - 1)
        node = grid.grid[r][c]

        if not node.is_start and not node.is_goal and not node.is_wall:
            node.is_wall = True
            return node

    return None