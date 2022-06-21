from PyQt5.Qt import *

from resource.ui.suanhuo_history import Ui_Form as saunhuo_Ui_Form
from resource.ui.jizhuangxiang_history import Ui_Form as jizhuangxiang_Ui_Form
from PyQt5.QtWidgets import *


class Tips_on_sanhuo(saunhuo_Ui_Form, QWidget):
    def __init__(self):

        super(Tips_on_sanhuo, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowIcon(QIcon("resource/image/img.png"))
        self.setWindowTitle("物流管理系统")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color: rgb(160, 160, 160) ;color: rgb(255,255,255); font: 13pt 黑体; border:none;border-right:0.5px dotted rgb(255,255,255);}"
        )

    def insert_data(self, shipname, tidanhao, combobox, history):
        # 由于前面页面的原因导致最终结算单与确认单出现了数据交换的错误,因此以下将两者交换回来
        history["确认单"], history["结算单"] = history["结算单"],  history["确认单"]
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(shipname))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(tidanhao))
        for i in range(len(combobox)):
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2 + i, QTableWidgetItem(history.get(combobox[i])))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, self.tableWidget.columnCount() - 1,
                                 QTableWidgetItem(history.get("time")))
        # for i in range(self.tableWidget.columnCount()):
        #     self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)

    def reset_data(self):
        self.tableWidget.setRowCount(0)


class Tips_on_jizhuangxiang(jizhuangxiang_Ui_Form, QWidget):
    def __init__(self):
        super(Tips_on_jizhuangxiang, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowTitle("物流管理系统")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color: rgb(160, 160, 160) ;color: rgb(255,255,255); font: 13pt 黑体; border:none;border-right:0.5px dotted rgb(255,255,255);}"
            )
        self.tableWidget.horizontalHeader().setFixedHeight(45)

    def insert_data(self, shipname, tidanhao, combobox, history):
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(shipname))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(tidanhao))
        for i in range(len(combobox)):
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2 + i, QTableWidgetItem(history.get(combobox[i])))
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, self.tableWidget.columnCount() - 1,
                                 QTableWidgetItem(history.get("time")))

    def reset_data(self):
        self.tableWidget.setRowCount(0)
