# export/csv_exporter.py
import csv
from PyQt5.QtWidgets import QFileDialog

def export_to_csv(maze_grid):
    path, _ = QFileDialog.getSaveFileName(None, "Export Maze as CSV", "", "CSV Files (*.csv)")
    if not path:
        return

    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in maze_grid.grid:
            writer.writerow([''.join('1' if wall else '0' for wall in cell['walls'].values()) for cell in row])
