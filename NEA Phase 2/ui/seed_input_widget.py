# ui/seed_input_widget.py
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout

class SeedInputWidget(QWidget):
    def __init__(self, editable=True):
        super().__init__()
        self.label = QLabel("Enter Seed:" if editable else "Generated Seed:")
        self.seed_input = QLineEdit()
        self.seed_input.setReadOnly(not editable)

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.seed_input)
        self.setLayout(layout)

    def set_seed(self, seed):
        self.seed_input.setText(str(seed))

    def get_seed(self):
        return self.seed_input.text()

    def set_editable(self, editable):
        self.seed_input.setReadOnly(not editable)
        self.label.setText("Enter Seed:" if editable else "Generated Seed:")
