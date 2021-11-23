import sys
import random
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Желтые окружности')

        self.btn_spawn = QPushButton('Press to spawn circle', self)
        self.btn_spawn.resize(125, 125)
        self.btn_spawn.move(200, 350)
        self.btn_spawn.clicked.connect(self.spawn)

    def spawn(self):
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        x = random.randint(10, 100)
        xx = random.randint(x + 1, 499 - x)
        yy = random.randint(x + 1, 299 - x)
        qp.drawEllipse(QPoint(xx, yy), x, x)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
