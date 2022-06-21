import sys
import threading
import time

from mysql import Mysql
from PyQt5.QtWidgets import *


class My_test_sql_conn_thread(QMessageBox):
    def __init__(self):
        super(My_test_sql_conn_thread, self).__init__()

    def create_conn_ui(self):
        pass


        # sql_conn_check_thread.join()


if __name__ == '__main__':
    My_test_sql_conn_thread().create_thread(1, "root", 'root', '3306', '127.0.0.1')
    app = QApplication(sys.argv)
    main = My_test_sql_conn_thread()
    main.show()
    app.exit(app.exec_())
