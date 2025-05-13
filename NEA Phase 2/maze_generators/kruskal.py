# maze_generators/kruskal.py
import random
from maze_generators.base import MazeGenerator

class KruskalGenerator(MazeGenerator):
    def generate(self):
        # Create a list of all walls
        walls = []
        for y in range(1, self.height, 2):
            for x in range(1, self.width, 2):
                if x + 2 < self.width:
                    walls.append(((x, y), (x + 2, y)))
                if y + 2 < self.height:
                    walls.append(((x, y), (x, y + 2)))

        # Shuffle walls
        random.shuffle(walls)

        # Union-Find structure to track sets
        parent = {}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        # Initialize disjoint set for each cell
        for y in range(1, self.height, 2):
            for x in range(1, self.width, 2):
                parent[(x, y)] = (x, y)

        # Iterate over walls and add paths
        for (x1, y1), (x2, y2) in walls:
            if find((x1, y1)) != find((x2, y2)):
                self.grid[y1][x1] = 0
                self.grid[y2][x2] = 0
                union((x1, y1), (x2, y2))
