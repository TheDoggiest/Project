from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSpinBox
from ui.maze_editor import MazeEditor

class MazeCreationView(QWidget):
    def __init__(self, maze_type):
        super().__init__()
        self.setWindowTitle(f"{maze_type} Maze Creation")
        self.setGeometry(300, 200, 400, 300)
        self.maze_type = maze_type
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel(f"Create a {self.maze_type} Maze")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Width and Height input (limited to 64 and over 3)
        dimensions_layout = QHBoxLayout()
        width_label = QLabel("Width: ")
        self.width_input = QSpinBox()
        self.width_input.setRange(4, 64)
        self.width_input.setValue(10)

        height_label = QLabel("Height: ")
        self.height_input = QSpinBox()
        self.height_input.setRange(4, 64)
        self.height_input.setValue(10)

        dimensions_layout.addWidget(width_label)
        dimensions_layout.addWidget(self.width_input)
        dimensions_layout.addWidget(height_label)
        dimensions_layout.addWidget(self.height_input)

        layout.addLayout(dimensions_layout)

        create_btn = QPushButton(f"Create {self.maze_type} Maze")
        create_btn.clicked.connect(self.create_maze)
        back_btn = QPushButton("Back to Main Menu")
        back_btn.clicked.connect(self.back_to_main)

        layout.addWidget(create_btn)
        layout.addWidget(back_btn)

        self.setLayout(layout)

    def create_maze(self):
        width = self.width_input.value()
        height = self.height_input.value()
        
        self.editor_window = MazeEditor(self.maze_type, width, height)
        self.editor_window.show()
        self.close()

    def back_to_main(self):
        self.main_menu = MainMenu()
        self.main_menu.show()
        self.close()
