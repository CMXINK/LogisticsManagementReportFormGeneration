import sys
from resource.ui.logon import Ui_Form
from PyQt5.Qt import *
import ctypes#需要用到的库
import myopne_icon_rc
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class Logon(QMainWindow, Ui_Form):
    logon_register_btn_signal = pyqtSignal()
    logon_safelogon_btn_signal = pyqtSignal(bool, bool)
    """
    logon_safelogon_btn_signal:
        int : 登录账号的grade
        bool: 第一个， 用来检测自动登录按钮的状态
        bool: 第二个， 用来检测记住密码按钮的状态
    """

    def __init__(self, parent=None, *args, **kwargs):
        super(Logon, self).__init__(parent)
        self.setWindowIcon(QIcon(":/open.ico"))
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.logon_rememberpassword_state = False
        self.logon_autologon_state = False
        self.setupUi(self)
        self.setWindowTitle("物流管理系统")
        self.logon_username_lineedit.setFocus()

    def logon_safelogon_btn_lk(self):
        self.logon_safelogon_btn_signal.emit(self.logon_autologon_state, self.logon_rememberpassword_state)

    def logon_autologon_checkbox_lk(self, state):
        self.logon_autologon_state = state
        if state:
            self.logon_rememberpassword_checkbox.setChecked(True)
            self.logon_rememberpassword_state = state
        else:
            self.logon_rememberpassword_checkbox.setChecked(False)
        print(self.logon_autologon_state, self.logon_rememberpassword_state)

    def logon_rememberpassword_checkbox_lk(self, state):
        self.logon_rememberpassword_state = state

    def logon_register_btn_lk(self):
        self.logon_register_btn_signal.emit()
        print("跳转到配置界面")

    def logon_username_password_lineedit_lk(self):
        if len(self.logon_username_lineedit.text()) > 0 and len(self.logon_password_lineedit.text()) > 0:
            self.logon_safelogon_btn.setEnabled(True)
        else:
            self.logon_safelogon_btn.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    logon = Logon()

    logon.show()
    logon.timerEvent(QTimerEvent(3))
    QMessageBox.warning(logon, '警告', '请输入正确的用户名和密码')
    sys.exit(app.exec_())
