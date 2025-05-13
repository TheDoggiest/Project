# maze/grid.py

class MazeGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[{'walls': {'N': True, 'S': True, 'E': True, 'W': True}} for _ in range(width)] for _ in range(height)]

    def has_wall(self, x, y, direction):
        return self.grid[y][x]['walls'].get(direction, True)

    def remove_wall(self, x, y, direction):
        if direction in self.grid[y][x]['walls']:
            self.grid[y][x]['walls'][direction] = False

    def set_walls(self, x, y, walls_dict):
        self.grid[y][x]['walls'] = walls_dict

    def get_walls(self, x, y):
        return self.grid[y][x]['walls']
