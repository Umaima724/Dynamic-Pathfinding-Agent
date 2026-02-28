# main.py

import pygame
from grid import Grid
from algorithms import search, manhattan, euclidean
from dynamic import spawn_obstacle
from metrics import Metrics

pygame.init()

ROWS = 20
COLS = 20
CELL_SIZE = 30
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE + 100

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dynamic Pathfinding Agent")

FONT = pygame.font.SysFont("Arial", 20)

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
GREY = (200,200,200)

grid = Grid(ROWS, COLS)
metrics = Metrics()

algorithm_type = "A*"
heuristic_type = "Manhattan"
dynamic_mode = False


def draw():
    WIN.fill(WHITE)

    for row in grid.grid:
        for node in row:
            x = node.col * CELL_SIZE
            y = node.row * CELL_SIZE

            color = WHITE
            if node.is_start:
                color = GREEN
            elif node.is_goal:
                color = RED
            elif node.is_wall:
                color = BLACK
            elif node.is_path:
                color = CYAN
            elif node.is_visited:
                color = BLUE
            elif node.is_frontier:
                color = YELLOW

            pygame.draw.rect(WIN, color, (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(WIN, GREY, (x, y, CELL_SIZE, CELL_SIZE), 1)

    info = f"Algo: {algorithm_type} | Heuristic: {heuristic_type} | Dynamic: {dynamic_mode}"
    stats = f"Visited: {metrics.nodes_visited} | Cost: {metrics.path_cost} | Time(ms): {int(metrics.execution_time)}"

    WIN.blit(FONT.render(info, True, BLACK), (10, HEIGHT - 90))
    WIN.blit(FONT.render(stats, True, BLACK), (10, HEIGHT - 60))

    pygame.display.update()


def run_search():
    grid.reset_algorithm()
    metrics.start_timer()

    heuristic = manhattan if heuristic_type == "Manhattan" else euclidean
    use_g = True if algorithm_type == "A*" else False

    path, visited = search(grid, grid.start, grid.goal, heuristic, use_g)

    metrics.stop_timer()
    metrics.update(visited, path)

    if path:
        for node in path:
            if not node.is_start and not node.is_goal:
                node.is_path = True


def main():
    global grid
    global metrics
    global algorithm_type, heuristic_type, dynamic_mode

    running = True

    while running:
        draw()

        if dynamic_mode:
            spawn_obstacle(grid, 0.02)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if y < ROWS * CELL_SIZE:
                    row = y // CELL_SIZE
                    col = x // CELL_SIZE
                    grid.toggle_wall(row, col)

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    run_search()

                if event.key == pygame.K_r:
                   grid.clear_walls()
                   grid.generate_random_obstacles(0.3)

                if event.key == pygame.K_c:
                   grid.clear_walls()
                   grid.reset_algorithm()

                if event.key == pygame.K_a:
                    algorithm_type = "A*" if algorithm_type == "GBFS" else "GBFS"

                if event.key == pygame.K_h:
                    heuristic_type = "Euclidean" if heuristic_type == "Manhattan" else "Manhattan"

                if event.key == pygame.K_d:
                    dynamic_mode = not dynamic_mode

    pygame.quit()


if __name__ == "__main__":
    main()