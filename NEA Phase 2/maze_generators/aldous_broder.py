# maze_generators/aldous_broder.py
import random
from maze_generators.base import MazeGenerator

class AldousBroderGenerator(MazeGenerator):
    def generate(self):
        x, y = random.randint(1, self.width // 2) * 2, random.randint(1, self.height // 2) * 2
        visited = {(x, y)}
        total_cells = (self.width // 2) * (self.height // 2)
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

        while len(visited) < total_cells:
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 1 <= nx < self.width - 1 and 1 <= ny < self.height - 1:
                    if (nx, ny) not in visited:
                        self.grid[ny][nx] = 0
                        self.grid[(y + ny) // 2][(x + nx) // 2] = 0
                        visited.add((nx, ny))
                        x, y = nx, ny
                        break
