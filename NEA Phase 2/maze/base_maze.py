# maze/base_maze.py
from abc import ABC, abstractmethod

class BaseMaze(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def draw(self, painter):
        """Optional: if using PyQt QPainter"""
        pass
