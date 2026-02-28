# main.py

import pygame
from grid import Grid

pygame.init()

ROWS = 20
COLS = 20
CELL_SIZE = 30

WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dynamic Pathfinding Agent")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (200, 200, 200)


grid = Grid(ROWS, COLS)
grid.set_start(0, 0)
grid.set_goal(ROWS - 1, COLS - 1)


def draw():
    WIN.fill(WHITE)

    for row in grid.grid:
        for node in row:
            x = node.col * CELL_SIZE
            y = node.row * CELL_SIZE

            color = WHITE

            if node.is_wall:
                color = BLACK
            elif node.is_start:
                color = GREEN
            elif node.is_goal:
                color = RED

            pygame.draw.rect(WIN, color, (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(WIN, GREY, (x, y, CELL_SIZE, CELL_SIZE), 1)

    pygame.display.update()


def get_clicked_pos(pos):
    x, y = pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    return row, col


def main():
    running = True

    while running:
        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if pygame.mouse.get_pressed()[0]:  # Left click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)
                grid.toggle_wall(row, col)

    pygame.quit()


if __name__ == "__main__":
    main()