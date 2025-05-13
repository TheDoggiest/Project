# display/maze_renderer.py
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor
from display.config import get_tile_size
from display.tile import get_tile_color

class MazeRenderer(QWidget):
    def __init__(self, maze_grid):
        super().__init__()
        self.maze = maze_grid  # 2D list of integers (tile types)
        self.tile_size = get_tile_size(len(maze_grid[0]), len(maze_grid))
        self.setFixedSize(
            self.tile_size * len(maze_grid[0]),
            self.tile_size * len(maze_grid)
        )

    def paintEvent(self, event):
        painter = QPainter(self)
        for y, row in enumerate(self.maze):
            for x, tile in enumerate(row):
                color = get_tile_color(tile)
                painter.fillRect(
                    x * self.tile_size,
                    y * self.tile_size,
                    self.tile_size,
                    self.tile_size,
                    QColor(*color)
                )
