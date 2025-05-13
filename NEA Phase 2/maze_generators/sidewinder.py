# maze_generators/sidewinder.py
import random
from maze_generators.base import MazeGenerator

class SidewinderGenerator(MazeGenerator):
    def generate(self):
        for y in range(1, self.height, 2):
            run_start = 0
            for x in range(1, self.width, 2):
                self.grid[y][x] = 0
                if x + 2 < self.width and random.random() < 0.5:
                    self.grid[y][x + 2] = 0
                else:
                    # Randomly "close" the run (create a vertical passage)
                    if x - 2 >= 0:
                        self.grid[y - 1][x] = 0
            run_start = x
