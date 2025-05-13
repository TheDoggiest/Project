# main.py
from PyQt5.QtWidgets import QApplication
from ui_main import MainWindow
import sys

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Good default style
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
