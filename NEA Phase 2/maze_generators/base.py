# maze_generators/base.py
from abc import ABC, abstractmethod

class MazeGenerator(ABC):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[1 for _ in range(width)] for _ in range(height)]  # 1 = wall, 0 = path

    @abstractmethod
    def generate(self):
        pass

    def get_maze(self):
        return self.grid
