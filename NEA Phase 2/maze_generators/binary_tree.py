# maze_generators/binary_tree.py
import random
from maze_generators.base import MazeGenerator

class BinaryTreeGenerator(MazeGenerator):
    def generate(self):
        directions = [(0, 2), (2, 0)]

        for y in range(1, self.height, 2):
            for x in range(1, self.width, 2):
                if random.random() < 0.5:  # Randomly choose one direction
                    dx, dy = random.choice(directions)
                    nx, ny = x + dx, y + dy
                    if 1 <= nx < self.width and 1 <= ny < self.height:
                        self.grid[ny][nx] = 0
                        self.grid[(ny + y) // 2][(nx + x) // 2] = 0
