from PyQt6.QtWidgets import QWidget, QPushButton, QMainWindow
from PyQt6.QtGui import QPainter, QColor
import random
from PyQt6.QtCore import Qt, QRect

class Circle(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for circle in self.circles:
            r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            painter.setBrush(QColor(r, g, b))
            painter.drawEllipse(circle)

    def add_circle(self):
        d = random.randint(20, 100)
        x = random.randint(0, self.width() - d)
        y = random.randint(0, self.height() - d)
        self.circles.append(QRect(x, y, d, d))
        self.update()

class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Желтые кружочки')
        self.setGeometry(300, 300, 500, 500)

        self.circle_widget = Circle()
        self.setCentralWidget(self.circle_widget)

        self.click_but = QPushButton('Клик', self)
        self.click_but.resize(100, 30)
        self.click_but.move(200, 400)
        self.click_but.clicked.connect(self.circle_widget.add_circle)