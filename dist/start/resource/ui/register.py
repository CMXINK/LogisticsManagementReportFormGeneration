# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(930, 500)
        Form.setMinimumSize(QtCore.QSize(930, 500))
        Form.setMaximumSize(QtCore.QSize(928, 498))
        Form.setStyleSheet("QWidget#Form{\n"
"    border-image: url(:/register/register.jpg);\n"
"}\n"
"")
        self.register_menu_btn = QtWidgets.QPushButton(Form)
        self.register_menu_btn.setGeometry(QtCore.QRect(10, 30, 71, 71))
        self.register_menu_btn.setStyleSheet("QPushButton{\n"
"border-radius:35px;\n"
"background-color:transparent;\n"
"color:rgb(255, 170, 0);\n"
"font: 14pt \"隶书\";}\n"
"QPushButton:hover{\n"
"border-radius:35px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 14pt \"隶书\";}\n"
"QPushButton:pressed{\n"
"border-radius:35px;\n"
"background-color:rgb(255, 255, 255);\n"
"color:rgb(112, 112, 112);\n"
"font: 14pt \"隶书\";}\n"
"QPushButton:checked{\n"
"border-radius:35px;\n"
"background-color:transparent;\n"
"color: rgb(170, 255, 127);\n"
"font: 14pt \"隶书\";}\n"
"")
        self.register_menu_btn.setCheckable(True)
        self.register_menu_btn.setObjectName("register_menu_btn")
        self.registert_about_btn = QtWidgets.QPushButton(Form)
        self.registert_about_btn.setGeometry(QtCore.QRect(100, 20, 71, 71))
        self.registert_about_btn.setStyleSheet("QPushButton{\n"
"border-radius:35px;\n"
"background-color:transparent;\n"
"color:rgb(255, 170, 0);\n"
"font: 14pt \"隶书\";}\n"
"QPushButton:hover{\n"
"border-radius:35px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 14pt \"隶书\";}\n"
"QPushButton:pressed{\n"
"border-radius:35px;\n"
"background-color:transparent;\n"
"color:rgb(255, 0, 0);\n"
"font: 14pt \"隶书\";}")
        self.registert_about_btn.setObjectName("registert_about_btn")
        self.register_reset_btn = QtWidgets.QPushButton(Form)
        self.register_reset_btn.setGeometry(QtCore.QRect(100, 100, 71, 71))
        self.register_reset_btn.setStyleSheet("QPushButton{\n"
"border-radius:35px;\n"
"background-color:transparent;\n"
"color:rgb(255, 170, 0);\n"
"font: 14pt \"隶书\";}\n"
"QPushButton:hover{\n"
"border-radius:35px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 14pt \"隶书\";}\n"
"QPushButton:pressed{\n"
"border-radius:35px;\n"
"background-color:transparent;\n"
"color:rgb(255, 0, 0);\n"
"font: 14pt \"隶书\";}")
        self.register_reset_btn.setObjectName("register_reset_btn")
        self.register_logon_btn = QtWidgets.QPushButton(Form)
        self.register_logon_btn.setGeometry(QtCore.QRect(20, 120, 71, 71))
        self.register_logon_btn.setStyleSheet("QPushButton{\n"
"border-radius:35px;\n"
"background-color:transparent;\n"
"color:rgb(255, 170, 0);\n"
"font: 14pt \"隶书\";}\n"
"QPushButton:hover{\n"
"border-radius:35px;\n"
"background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 14pt \"隶书\";}\n"
"QPushButton:pressed{\n"
"border-radius:35px;\n"
"background-color:transparent;\n"
"color:rgb(255, 0, 0);\n"
"font: 14pt \"隶书\";}")
        self.register_logon_btn.setObjectName("register_logon_btn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(260, 171, 481, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("color: rgb(27, 27, 27);\n"
"font: 14pt \"隶书\";\n"
"border:none")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("color: rgb(27, 27, 27);\n"
"font: 14pt \"隶书\";\n"
"border:none")
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.register_password_lineedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.register_password_lineedit.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"border-bottom:1px solid rgb(127, 127, 127);\n"
"color:rgb(0, 0, 0);\n"
"font: 14pt \"黑体\";\n"
"")
        self.register_password_lineedit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.register_password_lineedit.setObjectName("register_password_lineedit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.register_password_lineedit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("color: rgb(27, 27, 27);\n"
"font: 14pt \"隶书\";\n"
"border:none")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.register_port_lineedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.register_port_lineedit.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"border-bottom:1px solid rgb(127, 127, 127);\n"
"color:rgb(0, 0, 0);\n"
"font: 14pt \"黑体\";\n"
"")
        self.register_port_lineedit.setObjectName("register_port_lineedit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.register_port_lineedit)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color: rgb(27, 27, 27);\n"
"font: 14pt \"隶书\";\n"
"border:none")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.register_register_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.register_register_btn.setEnabled(False)
        self.register_register_btn.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color:transparent;\n"
"    color:rgb(0, 0, 0);\n"
"    border-color: rgb(0, 0, 0);\n"
"    font: 16pt \"隶书\";\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius:10px;\n"
"    background-color:rgb(255, 255, 255);\n"
"    color:rgb(0, 0, 0);\n"
"    font: 17pt \"隶书\";\n"
"}\n"
"QPushButton:pressed{\n"
"    border-radius:10px;\n"
"    background-color:transparent;\n"
"    background-color:rgb(255, 255, 255);\n"
"    color:rgb(0, 170, 0);\n"
"    font: 17pt \"隶书\";\n"
"}\n"
"QPushButton:disabled{    \n"
"    background-color:transparent;\n"
"    border:1px solid rgb(127, 127, 127);\n"
"    border-color: rgb(255, 0, 0);\n"
"    font: 16pt \"隶书\";\n"
"}")
        self.register_register_btn.setCheckable(False)
        self.register_register_btn.setObjectName("register_register_btn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.register_register_btn)
        self.register_username_lineedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.register_username_lineedit.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"border-bottom:1px solid rgb(127, 127, 127);\n"
"color:rgb(0, 0, 0);\n"
"font: 14pt \"黑体\";\n"
"")
        self.register_username_lineedit.setText("")
        self.register_username_lineedit.setObjectName("register_username_lineedit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.register_username_lineedit)
        self.register_ip_lineedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.register_ip_lineedit.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"border-bottom:1px solid rgb(127, 127, 127);\n"
"color:rgb(0, 0, 0);\n"
"font: 14pt \"黑体\";\n"
"")
        self.register_ip_lineedit.setText("")
        self.register_ip_lineedit.setObjectName("register_ip_lineedit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.register_ip_lineedit)

        self.retranslateUi(Form)
        self.register_menu_btn.clicked['bool'].connect(Form.show_hide_menu)
        self.registert_about_btn.clicked.connect(Form.about_lk)
        self.register_reset_btn.clicked.connect(Form.reset_lk)
        self.register_logon_btn.clicked.connect(Form.close)
        self.register_register_btn.clicked.connect(Form.register_lk)
        self.register_password_lineedit.textChanged['QString'].connect(Form.register_username_password_repassword_lineedit_lk)
        self.register_username_lineedit.textChanged['QString'].connect(Form.register_username_password_repassword_lineedit_lk)
        self.register_port_lineedit.textChanged['QString'].connect(Form.register_username_password_repassword_lineedit_lk)
        self.register_ip_lineedit.textChanged['QString'].connect(Form.register_username_password_repassword_lineedit_lk)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.register_menu_btn.setText(_translate("Form", "菜单"))
        self.registert_about_btn.setText(_translate("Form", "关于"))
        self.register_reset_btn.setText(_translate("Form", "重置"))
        self.register_logon_btn.setText(_translate("Form", "登录"))
        self.layoutWidget.setStyleSheet(_translate("Form", "background-color:transparent;\n"
"color:rgb(109, 109, 109);\n"
"border:none;\n"
"border-bottom:1px solid lightgray;\n"
""))
        self.label_4.setText(_translate("Form", "账   号："))
        self.label.setText(_translate("Form", "密   码："))
        self.label_2.setText(_translate("Form", "端   口："))
        self.register_port_lineedit.setText(_translate("Form", "3306"))
        self.label_3.setText(_translate("Form", "IP 地址："))
        self.register_register_btn.setText(_translate("Form", "确     定"))
import register_rc