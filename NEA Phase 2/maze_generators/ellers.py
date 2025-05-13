# maze_generators/ellers.py
import random
from maze_generators.base import MazeGenerator

class EllerGenerator(MazeGenerator):
    def generate(self):
        # Step 1: Create a set of disjoint sets
        sets = {y: [y] for y in range(1, self.height, 2)}
        for y in range(1, self.height, 2):
            self.grid[y][1] = 0

        # Step 2: For each row, create vertical connections
        for y in range(1, self.height - 1, 2):
            for x in range(1, self.width, 2):
                if random.random() < 0.5:
                    self.grid[y][x + 1] = 0
                    sets[y].append(sets.get(x, []))
            sets[y] = list(set(sets[y]))

        # Step 3: Connect random cells
        for y in range(1, self.height - 1, 2):
            for x in range(1, self.width - 1, 2):
                self.grid[y][x] = 0
