# maze_generator.py
"""
Module for maze generation algorithms.
This uses OOP principles, particularly polymorphism and abstraction, to structure multiple algorithms.
Each algorithm subclass inherits from MazeGenerator.
"""

from abc import ABC, abstractmethod
import random

class MazeGenerator(ABC):
    """Abstract base class for all maze generation algorithms."""

    @abstractmethod
    def generate(self, width: int, height: int, seed=None):
        """
        Generate a maze of given width and height.
        Should return a 2D list of 0s (path) and 1s (walls).
        """
        pass

class DFSMazeGenerator(MazeGenerator):
    """Implements DFS-based maze generation."""

    def generate(self, width: int, height: int, seed=None):
        if width < 4 or height < 4:
            raise ValueError("Maze dimensions must be >= 4")

        if seed is not None:
            random.seed(seed)

        # Defensive programming to initialize grid
        maze = [[1 for _ in range(width)] for _ in range(height)]

        def carve(x, y):
            dirs = [(0, 2), (0, -2), (2, 0), (-2, 0)]
            random.shuffle(dirs)
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 1 <= nx < width-1 and 1 <= ny < height-1 and maze[ny][nx] == 1:
                    maze[ny][nx] = 0
                    maze[y + dy//2][x + dx//2] = 0
                    carve(nx, ny)

        maze[1][1] = 0
        carve(1, 1)
        return maze
