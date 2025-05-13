from PyQt5.QtWidgets import QWidget, QGridLayout, QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtCore import Qt

class MazeEditor(QWidget):
    def __init__(self, maze_type, width, height):
        super().__init__()
        self.setWindowTitle(f"{maze_type} Maze Editor")
        self.setGeometry(300, 200, 600, 600)
        self.maze_type = maze_type
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.edit_mode = False  # Flag for Edit mode
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()
        self.table = QTableWidget(self.height, self.width)

        # Create maze grid with interactive cells
        for i in range(self.height):
            for j in range(self.width):
                cell = QTableWidgetItem("")
                cell.setBackground(Qt.white)
                cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.table.setItem(i, j, cell)
                self.table.cellClicked.connect(self.toggle_cell)

        layout.addWidget(self.table)

        # Buttons for Edit Mode, Back
        toggle_edit_btn = QPushButton("Toggle Edit Mode")
        toggle_edit_btn.clicked.connect(self.toggle_edit_mode)
        back_btn = QPushButton("Back to Maze Creation")
        back_btn.clicked.connect(self.back_to_creation)

        layout.addWidget(toggle_edit_btn)
        layout.addWidget(back_btn)

        self.setLayout(layout)

    def toggle_cell(self, row, col):
        if self.edit_mode:
            current_item = self.table.item(row, col)
            # Toggle between wall and path
            if current_item.background() == Qt.white:
                current_item.setBackground(Qt.black)  # Wall
            else:
                current_item.setBackground(Qt.white)  # Path

    def toggle_edit_mode(self):
        self.edit_mode = not self.edit_mode
        print(f"Edit Mode {'Enabled' if self.edit_mode else 'Disabled'}")

    def back_to_creation(self):
        self.creation_window = MazeCreationView(self.maze_type)
        self.creation_window.show()
        self.close()
