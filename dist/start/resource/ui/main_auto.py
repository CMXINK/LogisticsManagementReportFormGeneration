# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_auto.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1121, 814)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(23, 133, 175);\n"
"color: rgb(252, 254, 19);\n"
"font: 35pt \"微软雅黑\";\n"
"border:none")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setStyleSheet("font: 10pt \"微软雅黑\";\n"
"color:rgb(236, 236, 236);\n"
"background-color: rgb(16, 155, 149);\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(19)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treewidget = QtWidgets.QTreeWidget(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setUnderline(False)
        self.treewidget.setFont(font)
        self.treewidget.setStyleSheet("QTreeWidget{\n"
"    border:1px solid gray;\n"
"}\n"
"QTreeWidget QScroll::handle:horizontal{\n"
"    border:1px solid gray;\n"
"}")
        self.treewidget.setObjectName("treewidget")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treewidget.headerItem().setFont(0, font)
        self.verticalLayout_2.addWidget(self.treewidget)
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setStyleSheet("border:none;")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.widget_5)
        self.listWidget.setStyleSheet("\n"
"QListWidget *{\n"
"     none;\n"
"    }\n"
"QListWidget{\n"
"     background-color:#f2f2f2;\n"
"    font-size:18px;\n"
"    }\n"
"\n"
"QListWidget::item\n"
"    {\n"
"    height:40px;\n"
"    \n"
"    padding-left:40px;\n"
"    padding-right:40px;\n"
"    border:none;\n"
"    \n"
" }\n"
"QListWidget::item::hover\n"
"    {\n"
"    background-color:#91c9f7;\n"
"    border:2px solid #f2f2f2;\n"
"    text-border:none;\n"
" }\n"
"QListWidget::item::text\n"
"    {\n"
"    color:black;\n"
" }\n"
"")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout_3.addWidget(self.listWidget)
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(106, 153, 171);\n"
"font: 11pt \"微软雅黑\";\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setStyleSheet("border:none;")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_7 = QtWidgets.QWidget(self.widget_6)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mainauto_result_label = QtWidgets.QLabel(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainauto_result_label.sizePolicy().hasHeightForWidth())
        self.mainauto_result_label.setSizePolicy(sizePolicy)
        self.mainauto_result_label.setMinimumSize(QtCore.QSize(80, 42))
        self.mainauto_result_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainauto_result_label.setStyleSheet("font: 15pt \"微软雅黑\";\n"
"border-radius:12px;\n"
"border:none;")
        self.mainauto_result_label.setFrameShape(QtWidgets.QFrame.Box)
        self.mainauto_result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mainauto_result_label.setObjectName("mainauto_result_label")
        self.horizontalLayout_4.addWidget(self.mainauto_result_label)
        self.mainauto_add_btn = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainauto_add_btn.sizePolicy().hasHeightForWidth())
        self.mainauto_add_btn.setSizePolicy(sizePolicy)
        self.mainauto_add_btn.setMinimumSize(QtCore.QSize(80, 40))
        self.mainauto_add_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";    \n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(31, 117, 213);\n"
"}")
        self.mainauto_add_btn.setObjectName("mainauto_add_btn")
        self.horizontalLayout_4.addWidget(self.mainauto_add_btn)
        self.mainauto_match_btn = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.mainauto_match_btn.sizePolicy().hasHeightForWidth())
        self.mainauto_match_btn.setSizePolicy(sizePolicy)
        self.mainauto_match_btn.setMinimumSize(QtCore.QSize(80, 40))
        self.mainauto_match_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";    \n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(31, 117, 213);\n"
"}")
        self.mainauto_match_btn.setObjectName("mainauto_match_btn")
        self.horizontalLayout_4.addWidget(self.mainauto_match_btn)
        self.mainauto_edit_btn = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainauto_edit_btn.sizePolicy().hasHeightForWidth())
        self.mainauto_edit_btn.setSizePolicy(sizePolicy)
        self.mainauto_edit_btn.setMinimumSize(QtCore.QSize(80, 40))
        self.mainauto_edit_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";    \n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(31, 117, 213);\n"
"}")
        self.mainauto_edit_btn.setObjectName("mainauto_edit_btn")
        self.horizontalLayout_4.addWidget(self.mainauto_edit_btn)
        self.mainauto_del_btn = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainauto_del_btn.sizePolicy().hasHeightForWidth())
        self.mainauto_del_btn.setSizePolicy(sizePolicy)
        self.mainauto_del_btn.setMinimumSize(QtCore.QSize(80, 40))
        self.mainauto_del_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";    \n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(31, 117, 213);\n"
"}")
        self.mainauto_del_btn.setObjectName("mainauto_del_btn")
        self.horizontalLayout_4.addWidget(self.mainauto_del_btn)
        self.mainauto_saving_btn_2 = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainauto_saving_btn_2.sizePolicy().hasHeightForWidth())
        self.mainauto_saving_btn_2.setSizePolicy(sizePolicy)
        self.mainauto_saving_btn_2.setMinimumSize(QtCore.QSize(80, 40))
        self.mainauto_saving_btn_2.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";    \n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(31, 117, 213);\n"
"}")
        self.mainauto_saving_btn_2.setObjectName("mainauto_saving_btn_2")
        self.horizontalLayout_4.addWidget(self.mainauto_saving_btn_2)
        self.mainauto_saving_btn = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainauto_saving_btn.sizePolicy().hasHeightForWidth())
        self.mainauto_saving_btn.setSizePolicy(sizePolicy)
        self.mainauto_saving_btn.setMinimumSize(QtCore.QSize(80, 40))
        self.mainauto_saving_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";    \n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(31, 117, 213);\n"
"}")
        self.mainauto_saving_btn.setObjectName("mainauto_saving_btn")
        self.horizontalLayout_4.addWidget(self.mainauto_saving_btn)
        self.mainauto_fucntion_combobox = QtWidgets.QComboBox(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainauto_fucntion_combobox.sizePolicy().hasHeightForWidth())
        self.mainauto_fucntion_combobox.setSizePolicy(sizePolicy)
        self.mainauto_fucntion_combobox.setMinimumSize(QtCore.QSize(80, 40))
        self.mainauto_fucntion_combobox.setStyleSheet("QComboBox{\n"
"    border:none;\n"
"    border-radius:8px;    \n"
"    font: 14pt \"微软雅黑\";    \n"
"    background-color: rgb(255, 85, 0);\n"
"    color:rgb(255, 255, 255);\n"
"    border-left:none;\n"
"}\n"
"QComboBox:clicked{\n"
"    border:none;\n"
"    border-radius:8px;    \n"
"    font: 14pt \"微软雅黑\";    \n"
"    background-color: rgb(255, 85, 0);\n"
"    color: rgb(255, 85, 0);\n"
"}\n"
"QComboBox::drop-down{\n"
"    width:30px;\n"
"    border-radius:8px;        \n"
"    image: url(:/mainauto/mainauto_function_checkbox_drop-down.png);\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"    background-color:rgb(255, 170, 127);\n"
"}")
        self.mainauto_fucntion_combobox.setObjectName("mainauto_fucntion_combobox")
        self.mainauto_fucntion_combobox.addItem("")
        self.mainauto_fucntion_combobox.addItem("")
        self.mainauto_fucntion_combobox.addItem("")
        self.mainauto_fucntion_combobox.addItem("")
        self.mainauto_fucntion_combobox.addItem("")
        self.mainauto_fucntion_combobox.addItem("")
        self.mainauto_fucntion_combobox.addItem("")
        self.mainauto_fucntion_combobox.addItem("")
        self.mainauto_fucntion_combobox.addItem("")
        self.horizontalLayout_4.addWidget(self.mainauto_fucntion_combobox)
        self.pushButton = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";    \n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(31, 117, 213);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 13pt \"微软雅黑\";    \n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(31, 117, 213);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout_4.addWidget(self.widget_7)
        self.verticalLayout_3.addWidget(self.widget_6)
        self.tableWidget = QtWidgets.QTableWidget(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 15pt \"微软雅黑\";\n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    border:none;\n"
"    border-radius:7px;    \n"
"    font: 15pt \"微软雅黑\";    \n"
"    background-color: rgb(31, 117, 213);\n"
"    color:rgb(31, 117, 213);\n"
"}\n"
"QTableWidget{\n"
"    border:1px solid gray;\n"
"    border-left:none;    \n"
"    font: 9pt \"微软雅黑\";\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(26)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_3.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.widget_3)

        self.retranslateUi(Form)
        self.mainauto_add_btn.clicked['bool'].connect(Form.mainauto_add_btn_lk)
        self.mainauto_match_btn.clicked['bool'].connect(Form.mainauto_match_btn_lk)
        self.mainauto_edit_btn.clicked['bool'].connect(Form.mainauto_edit_btn_lk)
        self.mainauto_del_btn.clicked['bool'].connect(Form.mainauto_del_btn_lk)
        self.mainauto_saving_btn.clicked['bool'].connect(Form.mainauto_saving_btn_lk)
        self.mainauto_fucntion_combobox.currentIndexChanged['int'].connect(Form.mainauto_function_combobox_lk)
        self.pushButton_2.clicked.connect(Form.mainauto_function_btn_2_lk)
        self.pushButton.clicked.connect(Form.mainauto_function_btn_1_lk)
        self.mainauto_saving_btn_2.clicked['bool'].connect(Form.mainauto_fresh_btn_lk)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_6.setText(_translate("Form", "天 津 玺 玖 国 际 物 流 有 限 公 司"))
        self.label_3.setText(_translate("Form", "  急 速 物 流 管 理 系 统 VIP 版"))
        self.treewidget.headerItem().setText(0, _translate("Form", "业务"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "添加"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "删除"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "取消"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("Form", " 客 户 管 理"))
        self.mainauto_result_label.setText(_translate("Form", "0 个结果"))
        self.mainauto_add_btn.setText(_translate("Form", "添加"))
        self.mainauto_match_btn.setText(_translate("Form", "查询"))
        self.mainauto_edit_btn.setText(_translate("Form", "编辑"))
        self.mainauto_del_btn.setText(_translate("Form", "删除"))
        self.mainauto_saving_btn_2.setText(_translate("Form", "刷新"))
        self.mainauto_saving_btn.setText(_translate("Form", "保存"))
        self.mainauto_fucntion_combobox.setItemText(0, _translate("Form", "功能"))
        self.mainauto_fucntion_combobox.setItemText(1, _translate("Form", "打开"))
        self.mainauto_fucntion_combobox.setItemText(2, _translate("Form", "帮助"))
        self.mainauto_fucntion_combobox.setItemText(3, _translate("Form", "换号"))
        self.mainauto_fucntion_combobox.setItemText(4, _translate("Form", "tips"))
        self.mainauto_fucntion_combobox.setItemText(5, _translate("Form", "历史"))
        self.mainauto_fucntion_combobox.setItemText(6, _translate("Form", "部门"))
        self.mainauto_fucntion_combobox.setItemText(7, _translate("Form", "Excel"))
        self.mainauto_fucntion_combobox.setItemText(8, _translate("Form", "退出"))
        self.pushButton.setText(_translate("Form", "上一个"))
        self.pushButton_2.setText(_translate("Form", "下一个"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "new"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "nwe"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "新建列"))
        self.listWidget.setParent(Form)
import mainauto_rc