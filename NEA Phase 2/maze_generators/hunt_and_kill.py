# maze_generators/hunt_and_kill.py
import random
from maze_generators.base import MazeGenerator

class HuntAndKillGenerator(MazeGenerator):
    def generate(self):
        # Start at a random point
        x, y = 1, 1
        self.grid[y][x] = 0
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

        def is_valid(nx, ny):
            return 1 <= nx < self.width - 1 and 1 <= ny < self.height - 1 and self.grid[ny][nx] == 1

        def hunt():
            for cy in range(1, self.height, 2):
                for cx in range(1, self.width, 2):
                    if self.grid[cy][cx] == 1:
                        # Check for adjacent paths
                        for dx, dy in directions:
                            nx, ny = cx + dx, cy + dy
                            if 1 <= nx < self.width and 1 <= ny < self.height and self.grid[ny][nx] == 0:
                                self.grid[cy][cx] = 0
                                self.grid[(cy + ny) // 2][(cx + nx) // 2] = 0
                                return True
            return False

        while hunt():
            pass
