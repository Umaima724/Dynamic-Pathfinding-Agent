# main.py

import pygame
import time
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
ORANGE = (255,165,0)

grid = Grid(ROWS, COLS)
metrics = Metrics()

algorithm_type = "A*"
heuristic_type = "Manhattan"
dynamic_mode = False

agent = grid.start
current_path = []
moving = False


def draw():
    WIN.fill(WHITE)

    for row in grid.grid:
        for node in row:
            x = node.col * CELL_SIZE
            y = node.row * CELL_SIZE

            color = WHITE
            if node == agent:
                color = ORANGE
            elif node.is_start:
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


def calculate_path(start_node):
    grid.reset_algorithm()
    metrics.start_timer()

    heuristic = manhattan if heuristic_type == "Manhattan" else euclidean
    use_g = True if algorithm_type == "A*" else False

    path, visited = search(grid, start_node, grid.goal, heuristic, use_g)

    metrics.stop_timer()
    metrics.update(visited, path)

    if path:
        for node in path:
            if not node.is_start and not node.is_goal:
                node.is_path = True

    return path


def main():
    global dynamic_mode, algorithm_type, heuristic_type
    global agent, current_path, moving

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)

        if moving and current_path:
            next_node = current_path.pop(0)

            # If obstacle spawned on next step → replan
            if next_node.is_wall:
                current_path = calculate_path(agent)
                continue

            agent = next_node
            pygame.time.delay(80)

            # Dynamic spawning
            if dynamic_mode:
                spawned = spawn_obstacle(grid, 0.05)
                if spawned and spawned in current_path:
                    current_path = calculate_path(agent)

            if agent == grid.goal:
                moving = False

        draw()

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
                    agent = grid.start
                    current_path = calculate_path(agent)
                    if current_path:
                        current_path.pop()  # remove goal duplication
                        current_path.reverse()
                        moving = True

                if event.key == pygame.K_r:
                    grid.clear_walls()
                    grid.generate_random_obstacles(0.3)

                if event.key == pygame.K_c:
                    grid.clear_walls()
                    grid.reset_algorithm()
                    agent = grid.start
                    moving = False

                if event.key == pygame.K_a:
                    algorithm_type = "A*" if algorithm_type == "GBFS" else "GBFS"

                if event.key == pygame.K_h:
                    heuristic_type = "Euclidean" if heuristic_type == "Manhattan" else "Manhattan"

                if event.key == pygame.K_d:
                    dynamic_mode = not dynamic_mode

    pygame.quit()


if __name__ == "__main__":
    main()