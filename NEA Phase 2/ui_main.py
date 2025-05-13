# ui_main.py
"""
Main UI Menu using PyQt5.
"""
from PyQt5.QtWidgets import (
    QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
)
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Maze Generator and Pathfinder")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        font = QFont("Arial", 14)

        # Buttons
        self.manual_btn = QPushButton("Manual Maze")
        self.seed_btn = QPushButton("Seed Maze")
        self.computer_btn = QPushButton("Computer-based Maze")

        for btn in [self.manual_btn, self.seed_btn, self.computer_btn]:
            btn.setFont(font)
            layout.addWidget(btn)

        # Bind buttons
        self.manual_btn.clicked.connect(self.manual_maze)
        self.seed_btn.clicked.connect(self.seed_maze)
        self.computer_btn.clicked.connect(self.computer_maze)

        # Central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def manual_maze(self):
        QMessageBox.information(self, "Manual Maze", "Manual Maze creation will launch here.")

    def seed_maze(self):
        QMessageBox.information(self, "Seed Maze", "Seeded Maze input screen will launch here.")

    def computer_maze(self):
        QMessageBox.information(self, "Computer Maze", "Maze generator screen will launch here.")
