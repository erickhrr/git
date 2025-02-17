from PyQt6.QtWidgets import QWidget, QPushButton

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Желтые кружочки')
        self.setGeometry(300, 300, 500, 500)

        self.click_but = QPushButton('Клик', self)
        self.click_but.resize(100, 30)
        self.click_but.move(200, 400)
        self.click_but.clicked.connect(self.click)

    def click(self):
        print(11)