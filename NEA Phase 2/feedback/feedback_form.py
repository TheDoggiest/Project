# feedback/feedback_form.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit, QLineEdit,
    QPushButton, QComboBox, QMessageBox
)
from PyQt5.QtCore import Qt
from feedback.feedback_model import FeedbackEntry
from feedback.feedback_db import FeedbackDB
from datetime import datetime

class FeedbackForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Leave Feedback")
        self.setGeometry(300, 200, 400, 300)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Your Name (optional):"))
        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)

        layout.addWidget(QLabel("Feedback Category:"))
        self.category_dropdown = QComboBox()
        self.category_dropdown.addItems(["Bug", "Suggestion", "Praise", "Other"])
        layout.addWidget(self.category_dropdown)

        layout.addWidget(QLabel("Your Message:"))
        self.message_input = QTextEdit()
        layout.addWidget(self.message_input)

        submit_btn = QPushButton("Submit Feedback")
        submit_btn.clicked.connect(self.submit_feedback)
        layout.addWidget(submit_btn)

        self.setLayout(layout)

    def submit_feedback(self):
        username = self.name_input.text().strip()
        message = self.message_input.toPlainText().strip()
        category = self.category_dropdown.currentText()

        if not message:
            QMessageBox.warning(self, "Input Error", "Message cannot be empty.")
            return

        entry = FeedbackEntry(
            username=username or "Anonymous",
            message=message,
            category=category,
            timestamp=datetime.now()
        )

        db = FeedbackDB()
        db.add_feedback(entry)
        db.close()

        QMessageBox.information(self, "Thank You", "Your feedback has been submitted.")
        self.name_input.clear()
        self.message_input.clear()
        self.category_dropdown.setCurrentIndex(0)
