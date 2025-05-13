# leaderboard/leaderboard_view.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QPushButton
)
from leaderboard.db_manager import DBManager
from PyQt5.QtCore import Qt

class LeaderboardView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Leaderboard")
        self.setGeometry(300, 200, 600, 400)
        self.db = DBManager()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("Top Maze Solvers")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Player", "Score", "Mode", "Width", "Height", "Date"
        ])
        layout.addWidget(self.table)

        self.refresh_leaderboard()

        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

        self.setLayout(layout)

    def refresh_leaderboard(self):
        entries = self.db.get_top_entries(10)
        self.table.setRowCount(len(entries))
        for row_idx, entry in enumerate(entries):
            self.table.setItem(row_idx, 0, QTableWidgetItem(entry.player_name))
            self.table.setItem(row_idx, 1, QTableWidgetItem(str(entry.score)))
            self.table.setItem(row_idx, 2, QTableWidgetItem(entry.mode))
            self.table.setItem(row_idx, 3, QTableWidgetItem(str(entry.width)))
            self.table.setItem(row_idx, 4, QTableWidgetItem(str(entry.height)))
            self.table.setItem(row_idx, 5, QTableWidgetItem(entry.date.strftime("%Y-%m-%d %H:%M")))
