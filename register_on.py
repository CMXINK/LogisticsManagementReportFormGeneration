import sys
from PyQt5.Qt import *
from resource.ui.register import Ui_Form
import myopne_icon_rc

class Register(QWidget, Ui_Form):
    exit_signal = pyqtSignal()
    register_signal = pyqtSignal(str, str, str, str)

    def __init__(self, parents=None, *args, **kwargs):
        super(Register, self).__init__(parents)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowIcon(QIcon(":/open.ico"))
        self.registert_about_btn.hide()
        self.register_logon_btn.hide()
        self.register_reset_btn.hide()
        self.setWindowTitle("物流管理系统")
    def show_hide_menu(self):
        print('显示和隐藏')
        if self.register_menu_btn.isChecked():
            self.register_logon_btn.show()
            self.register_reset_btn.show()
            self.registert_about_btn.show()
        else:
            self.registert_about_btn.hide()
            self.register_logon_btn.hide()
            self.register_reset_btn.hide()

    def about_lk(self):
        print(1)
        QMessageBox.about(self, '关于', '请输入<strong>用户名</strong>和<strong>密码</strong>以及<strong>服务器的ip地址</strong>和<strong>开放的端口</strong>(默认3306)以连接到服务器')

    def reset_lk(self):
        self.register_username_lineedit.setText("")
        self.register_password_lineedit.setText("")
        self.register_port_lineedit.setText("")
        self.register_ip_lineedit.setText("")

    def logon_lk(self):
        self.exit_signal.emit()

    def register_lk(self):
        username = self.register_username_lineedit.text()
        password = self.register_password_lineedit.text()
        ip = self.register_ip_lineedit.text()
        port = self.register_port_lineedit.text()

        if username == '' or password == '' or ip == '' or port == '':
            QMessageBox.critical(self, '错误', '账户，密码，端口 和 IP 都不能为空', QMessageBox.Ok)
        else:
            self.register_signal.emit(username, password, ip, port)

    def register_username_password_repassword_lineedit_lk(self):
        if len(self.register_username_lineedit.text()) > 0 and len(self.register_password_lineedit.text()) > 0 and len(self.register_ip_lineedit.text()) and len(self.register_port_lineedit.text())> 0:
            self.register_register_btn.setEnabled(True)
        else:
            self.register_register_btn.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Register()
    window.show()
    sys.exit(app.exec_())
