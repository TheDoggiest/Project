# export/png_exporter.py
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPainter, QImage, QColor
from PyQt5.QtCore import Qt

def export_to_png(maze_grid):
    cell_size = 20
    width_px = maze_grid.width * cell_size
    height_px = maze_grid.height * cell_size

    image = QImage(width_px, height_px, QImage.Format_RGB32)
    image.fill(Qt.white)

    painter = QPainter(image)
    painter.setPen(QColor(0, 0, 0))

    for y in range(maze_grid.height):
        for x in range(maze_grid.width):
            cx, cy = x * cell_size, y * cell_size
            walls = maze_grid.get_walls(x, y)

            if walls['N']:
                painter.drawLine(cx, cy, cx + cell_size, cy)
            if walls['S']:
                painter.drawLine(cx, cy + cell_size, cx + cell_size, cy + cell_size)
            if walls['W']:
                painter.drawLine(cx, cy, cx, cy + cell_size)
            if walls['E']:
                painter.drawLine(cx + cell_size, cy, cx + cell_size, cy + cell_size)

    painter.end()

    path, _ = QFileDialog.getSaveFileName(None, "Export Maze as PNG", "", "PNG Files (*.png)")
    if path:
        image.save(path)
