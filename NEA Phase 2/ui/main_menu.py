from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from ui.maze_creation import MazeCreationView
from ui.leaderboard_view import LeaderboardView


class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.setGeometry(300, 200, 400, 300)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("Maze Game")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Buttons for menu options
        manual_btn = QPushButton("Manual Maze")
        computer_btn = QPushButton("Computer-based Maze")
        seed_btn = QPushButton("Seed Maze")
        leaderboard_btn = QPushButton("Leaderboard")

        manual_btn.clicked.connect(lambda: self.open_maze_creation("Manual"))
        computer_btn.clicked.connect(lambda: self.open_maze_creation("Computer"))
        seed_btn.clicked.connect(lambda: self.open_maze_creation("Seed"))
        leaderboard_btn.clicked.connect(self.open_leaderboard)

        layout.addWidget(manual_btn)
        layout.addWidget(computer_btn)
        layout.addWidget(seed_btn)
        layout.addWidget(leaderboard_btn)

        self.setLayout(layout)

    def open_maze_creation(self, maze_type):
        self.mazecreation_window = MazeCreationView(maze_type)
        self.mazecreation_window.show()
        self.close()

    def open_leaderboard(self):
        self.leaderboard_window = LeaderboardView()
        self.leaderboard_window.show()
        self.close()
