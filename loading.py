import time

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie, QIcon
import sys


class Loading(QWidget):
    def __init__(self):
        super(Loading, self).__init__()
        self.setWindowIcon(QIcon("resource/image/img.png"))
        self.resize(350, 150)
        self.setWindowTitle("通知")
        # self.setWindowModality(Qt.ApplicationModal)

        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.my_ui()

    def my_ui(self):
        self.movie = QMovie("resource/image/loading.gif")
        label = QLabel()
        label.setMovie(self.movie)

        layout = QVBoxLayout()
        layout.addWidget(label)


        self.layout = QVBoxLayout()
        self.setLayout(layout)
        label.setToolTip("加载中")
        self.movie.start()

    def stop_movie(self):
        self.movie.stop()

    def start_movie(self):
        self.movie.start()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Loading()
    main.show()
    app.exit(app.exec_())