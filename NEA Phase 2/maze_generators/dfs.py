# maze_generators/dfs.py
import random
from maze_generators.base.py import MazeGenerator

class DFSGenerator(MazeGenerator):
    def generate(self):
        stack = [(1, 1)]
        self.grid[1][1] = 0
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

        while stack:
            x, y = stack[-1]
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 1 <= nx < self.height - 1 and 1 <= ny < self.width - 1 and self.grid[nx][ny] == 1:
                    self.grid[nx][ny] = 0
                    self.grid[x + dx // 2][y + dy // 2] = 0
                    stack.append((nx, ny))
                    break
            else:
                stack.pop()
