# metrics.py

import time


class Metrics:
    def __init__(self):
        self.nodes_visited = 0
        self.path_cost = 0
        self.execution_time = 0

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.execution_time = (time.time() - self.start_time) * 1000

    def update(self, visited, path):
        self.nodes_visited = len(visited)
        self.path_cost = len(path) if path else 0