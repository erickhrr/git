import sys
from PyQt6.QtWidgets import QApplication
from ui import MainWin



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())