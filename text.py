from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys
from mainauto_read_wite_file import Write_file
import openpyxl
import os


class my_UI(QWidget):
    def __init__(self):

        super(my_UI, self).__init__()

        self.my_ui()

        # self.setWindowIcon(QIcon())

    def my_ui(self):

        self.tablewidget = QTableWidget(3, 3)
        self.tablewidget.setHorizontalHeaderLabels(["one", "two", "three"])
        layout = QVBoxLayout()
        self.btn_add = QPushButton("add")
        self.btn_del = QPushButton("del")
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.btn_del)
        layout.addWidget(self.tablewidget)
        layout.addLayout(self.layout)
        self.setLayout(layout)
        for i in range(0, 3):
            for j in range(0, 3):
                self.tablewidget.setItem(i, j, QTableWidgetItem(str(i + 1) + str(j + 1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("resource/image/logon.ico"))
    main = my_UI()
    main.show()

    app.exit(app.exec_())
