from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage
import numpy as np
import sys


def print_img():
    app = QApplication(sys.argv)

    win = QWidget()
    label = QLabel()
    label.setPixmap(QPixmap("data/beach.jpg"))

    vbox = QVBoxLayout()
    vbox.addWidget(label)
    win.setLayout(vbox)
    win.show()

    sys.exit(app.exec_())


def print_np():
    app = QApplication(sys.argv)

    win = QWidget()
    label = QLabel()

    img = np.zeros((500, 500), dtype=np.uint8)
    img[250:, :] = 255

    qImg = QPixmap(
        QImage(img.data, img.shape[0], img.shape[1], QImage.Format_Indexed8))
    label.setPixmap(qImg)

    vbox = QVBoxLayout()
    vbox.addWidget(label)
    win.setLayout(vbox)
    win.show()

    sys.exit(app.exec_())


print_np()


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        # position of the window
        self.left = 10
        self.top = 10
        # size of the window
        self.width = 640
        self.height = 480

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        label = QLabel(self)
        img = np.zeros((50, 50, 40))
        image = QPixmap(QImage(img.data, 50, 50, 1, QImage.Format_RGB888))
        PrintImage
        # label.setPixmap(image)

        self.show()


# app = QApplication(sys.argv)
# ex = App()
# sys.exit(app.exec_())
