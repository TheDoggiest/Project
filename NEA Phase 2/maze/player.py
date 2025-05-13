# maze/player.py

class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, direction, maze_grid):
        dx, dy = {'W': -1, 'E': 1, 'N': 0, 'S': 0}, {'N': -1, 'S': 1, 'E': 0, 'W': 0}
        new_x = self.x + dx[direction]
        new_y = self.y + dy[direction]

        # Check bounds
        if not (0 <= new_x < maze_grid.width and 0 <= new_y < maze_grid.height):
            return False

        # Check for wall
        if maze_grid.has_wall(self.x, self.y, direction):
            return False

        # Move
        self.x = new_x
        self.y = new_y
        return True
