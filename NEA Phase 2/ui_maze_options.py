# ui_maze_options.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QSpinBox, QPushButton, QComboBox, QMessageBox
)
from PyQt5.QtGui import QFont
from ui_maze_editor import MazeEditorWindow
from utils.validators import validate_dimensions
from utils.difficulty import calculate_difficulty

class MazeOptionsWindow(QWidget):
    def __init__(self, mode):
        super().__init__()
        self.mode = mode  # 'manual', 'seed', 'computer'
        self.setWindowTitle(f"{mode.title()} Maze Options")
        self.setGeometry(200, 200, 400, 300)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setFont(QFont("Arial", 12))

        self.width_input = QSpinBox()
        self.width_input.setRange(4, 64)
        self.width_input.setValue(10)
        layout.addWidget(QLabel("Select Width:"))
        layout.addWidget(self.width_input)

        self.height_input = QSpinBox()
        self.height_input.setRange(4, 64)
        self.height_input.setValue(10)
        layout.addWidget(QLabel("Select Height:"))
        layout.addWidget(self.height_input)

        if self.mode == 'computer':
            self.algorithm_selector = QComboBox()
            self.algorithm_selector.addItems([
                "Prim's", "Eller's", "Hunt-and-Kill", "Binary Tree",
                "Kruskal's", "Sidewinder", "Aldous-Broder", "DFS"
            ])
            layout.addWidget(QLabel("Select Algorithm:"))
            layout.addWidget(self.algorithm_selector)

        # Difficulty dropdown
        self.difficulty_selector = QComboBox()
        self.difficulty_selector.addItems(["Easy", "Medium", "Hard"])
        layout.addWidget(QLabel("Select Difficulty:"))
        layout.addWidget(self.difficulty_selector)

        self.start_btn = QPushButton("Generate Maze")
        self.start_btn.clicked.connect(self.proceed)
        layout.addWidget(self.start_btn)

        self.back_btn = QPushButton("Back")
        self.back_btn.clicked.connect(self.go_back)
        layout.addWidget(self.back_btn)

        self.setLayout(layout)

    def proceed(self):
        width = self.width_input.value()
        height = self.height_input.value()

        if not validate_dimensions(width, height):
            QMessageBox.warning(self, "Invalid Dimensions", "Width and height must be between 4 and 64.")
            return

        # Get difficulty setting
        selected_difficulty = self.difficulty_selector.currentText().lower()

        # Calculate difficulty based on size, algorithm, and random generation
        difficulty = calculate_difficulty(width, height, selected_difficulty)

        # Open the maze editor window with settings
        self.editor = MazeEditorWindow(self.mode, width, height, difficulty)
        self.editor.show()
        self.close()

    def go_back(self):
        from ui_main import MainMenu
        self.menu = MainMenu()
        self.menu.show()
        self.close()
