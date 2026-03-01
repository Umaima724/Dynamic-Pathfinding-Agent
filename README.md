# Dynamic-Pathfinding-Agent
Dynamic Pathfinding Agent implementing A and Greedy Best-First Search on a grid-based environment with real-time obstacle spawning and re-planning. Features GUI visualization, heuristic selection (Manhattan &amp; Euclidean), interactive map editing, and performance metrics tracking.
# Technologies used
Python 3.12

Pygame (for GUI and visualization)

VS Code (development environment)

Git & GitHub (version control)
# Initial Environment Setup
The following steps were performed to set up the development environment:

Installed Python 3.12

Installed Pygame

Installed Python extension in VS Code

Created a virtual environment

Activated the virtual environment (Windows)

Installed required dependencies

Selected the Python interpreter in VS Code

Setup the project structure
# How to Run the Project

Open terminal in the project directory

Activate virtual environment (if created):

venv\Scripts\activate

Install pygame (if not already installed):

pip install pygame

Run the program:

python main.py
# Controls
Key	Action
SPACE	Start search
R	Generate random obstacles
C	Clear grid
A	Toggle between A* and GBFS
H	Toggle heuristic (Manhattan / Euclidean)
D	Toggle Dynamic Mode
Mouse Click	Add/Remove walls
# Features

Grid-based environment with interactive editing

A* Search (f(n) = g(n) + h(n))

Greedy Best-First Search (f(n) = h(n))

Manhattan and Euclidean heuristic selection

Random obstacle generation with adjustable density

Real-time obstacle spawning in Dynamic Mode

Automatic re-planning when path is blocked

# Performance metrics display:

Nodes Visited

Path Cost

Execution Time (ms)

# Project Structure
main.py
grid.py
node.py
algorithms.py
dynamic.py
metrics.py
README.md
# Dynamic Mode Explanation

When Dynamic Mode is enabled:

The agent moves step-by-step toward the goal.

Obstacles spawn randomly during movement.

If a new obstacle blocks the remaining path, the agent recalculates a new path from its current position.

The process continues until the goal is reached or no path exists.

# Performance Metrics

The system measures:

Total number of visited (expanded) nodes

Final path cost

Execution time in milliseconds

These metrics help compare A* and Greedy Best-First Search performance under different grid conditions.

# License

This project was developed as part of an Artificial Intelligence course assignment at National University of Computer & Emerging Sciences