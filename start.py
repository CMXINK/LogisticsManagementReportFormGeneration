import os
import sys
from mysql import Mysql
from register_on import Register
from logon_on import Logon
from PyQt5.QtWidgets import *
from mian_auto_replace import Main_auto
from user_jizhuang_on import User_jizhuang
from user_operation_on import User_operation
from tips_on import Tips_on_sanhuo
from tips_on import Tips_on_jizhuangxiang
import ctypes  # 需要用到的库
import myopne_icon_rc

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

old_user = ""
check_user_no_conn = True
check_db_no_conn = True
g_User = ''
g_Pw = ''
g_Port = 3306
g_Ip = ''
username = ''
password = ''


def start_main():
    global reply, check_db_no_conn, check_user_no_conn, username, password
    logon_auto_logon_state = logon.logon_autologon_checkbox.checkState()
    logon_rememberpassword_sate = logon.logon_rememberpassword_checkbox.checkState()
    username = logon.logon_username_lineedit.text()
    password = logon.logon_password_lineedit.text()

    def write_data():

        if logon_rememberpassword_sate:
            path = os.path.abspath(".") + "\\resource\\check\\User.txt.txt"
            with open(path, 'wb') as fw_user:
                fw_user.write(username.encode('utf-8'))
            path = os.path.abspath(".") + "\\resource\\check\\Pw.txt"
            with open(path, 'wb') as fw_pw:
                fw_pw.write(password.encode('utf-8'))
            if logon_auto_logon_state:
                path = os.path.abspath(".") + "\\resource\\check\\Mode.txt"
                with open(path, 'wb') as fw_pw:
                    fw_pw.write("auto".encode('utf-8'))
            elif logon_rememberpassword_sate:
                path = os.path.abspath(".") + "\\resource\\check\\Mode.txt"
                with open(path, 'wb') as fw_pw:
                    fw_pw.write("remember".encode('utf-8'))
        else:
            path = os.path.abspath(".") + "\\resource\\check\\User.txt.txt"
            with open(path, 'wb') as fw_user:
                fw_user.write("".encode('utf-8'))
            path = os.path.abspath(".") + "\\resource\\check\\Pw.txt"
            with open(path, 'wb') as fw_pw:
                fw_pw.write("".encode('utf-8'))
            path = os.path.abspath(".") + "\\resource\\check\\Mode.txt"
            with open(path, 'wb') as fw_pw:
                fw_pw.write("No".encode('utf-8'))

    try:
        reply = -1
        reply = Mysql(g_User, g_Pw, g_Port, g_Ip).user_password_table(username, password)
    except:

        get_button = QMessageBox.warning(logon, "警告", "当前数据库未连接,是否进行离线操作(不能操作有关数据库的部分)",
                                         QMessageBox.Yes | QMessageBox.No)
        check_user_no_conn = True
        check_user_no_conn = True
        if get_button == QMessageBox.Yes:
            main.if_sql_init(check_db_no_conn, check_user_no_conn, username, password, g_User, g_Pw, g_Port, g_Ip, )
            main.show()
            logon.hide()
            reply = '-1'  # 为了区分于下面的对grade的检测,以免过grade检测
    if int(reply) > 0:
        # 这里的reply是从mysql中拿到的用户的grade
        write_data()

        check_db_no_conn = False
        check_user_no_conn = False
        main.if_sql_init(check_db_no_conn, check_user_no_conn, username, password, g_User, g_Pw, g_Port, g_Ip)
        main.show()
        logon.hide()
    elif int(reply) == 0:
        get_button = QMessageBox.warning(logon, '警告', '请输入正确的用户名和密码,是否启用离线模式(无法操作数据库内容)',
                                         QMessageBox.Yes | QMessageBox.No)
        check_user_no_conn = True
        check_db_no_conn = False
        if get_button == QMessageBox.Yes:
            write_data()
            main.if_sql_init(check_db_no_conn, check_user_no_conn, username, password, g_User, g_Pw, g_Port, g_Ip)
            main.show()
            logon.hide()


def start_register():
    register.show()


def real_tips_show(grade):
    if grade == 2:
        pass
    # QMessageBox.information(main, "通知", information_data)


def init_mysql(user, password, ip, port):
    try:
        global g_User, g_Pw, g_Port, g_Ip
        g_User = user
        g_Pw = password
        g_Port = port
        g_Ip = ip
        if Mysql(user, password, port, ip).check_db():
            QMessageBox.information(register, '通知', '连接数据库<strong>成功</strong>!')
            path = os.path.abspath(".") + "\\resource\\" + "check\\init_sql.txt"
            with open(path, 'w', encoding='utf-8') as fw_initSQL:
                fw_initSQL.write(user + '\n' + password + '\n' + port + '\n' + ip)
    except:
        QMessageBox.information(register, '通知', '连接数据库失败,请检查您的参数')


def start_main_to_logon():
    logon.show()
    main.hide()


# 散货/集装箱/财务 的显示
def check_oper_on(text, grade, user):
    data = Mysql(g_User, g_Pw, g_Port, g_Ip).check_oper(text, grade)
    if int(grade) == 2:
        data = Mysql(g_User, g_Pw, g_Port, g_Ip).sanhuo_data(text)
    try:
        data = data[0]
    except:
        data = False
    if data:
        if int(grade) == 1:
            pass
        if int(grade) == 2:
            if user_sanhuo.isVisible():
                pass
            else:
                user_sanhuo.create_nwe(text, data)
                user_sanhuo.show()
        if int(grade) == 3:
            if user_jizhuangxiang.isVisible():
                pass
            else:
                user_jizhuangxiang.creat_new(text, data)
                user_jizhuangxiang.show()
        if int(grade) == 4:
            pass


def get_auto_logon_or_rememberpassword_data():
    global check_db_no_conn
    global check_user_no_conn
    path = os.path.abspath(".") + "\\resource\\check\\User.txt.txt"
    with open(path, 'rb') as fr_user:
        logon.logon_username_lineedit.setText(fr_user.read().decode('utf-8'))

    path = os.path.abspath(".") + "\\resource\\check\\Pw.txt"
    with open(path, 'rb') as fr_pw:
        logon.logon_password_lineedit.setText(fr_pw.read().decode('utf-8'))
    path = os.path.abspath(".") + "\\resource\\check\\Mode.txt"
    with open(path, 'rb') as fr_mode:
        mode = fr_mode.read().decode('utf-8')
        if mode == "auto":
            username = logon.logon_username_lineedit.text()
            password = logon.logon_password_lineedit.text()
            try:
                reply = -1

                reply = Mysql(g_User, g_Pw, int(g_Port), g_Ip).user_password_table(username, password)

                logon.logon_rememberpassword_checkbox.setChecked(True)
                logon.logon_autologon_checkbox.setChecked(True)
                # auto下的正常登录:
                if int(reply) > 0:
                    check_db_no_conn = False
                    check_user_no_conn = False
                    return True
            except:
                QMessageBox.warning(logon, '警告', '连接数据库失败,请先配置数据库')
                check_db_no_conn = True
                check_user_no_conn = True

            if int(reply) == 0:
                QMessageBox.warning(logon, '警告', '请输入正确的用户名和密码')

                check_db_no_conn = False
                check_user_no_conn = True
                return False

        elif mode == "remember":
            logon.logon_rememberpassword_checkbox.setChecked(True)


def insert_data_tips(t, grade, shipname, tidanhao,newtidanhao, combobox, data):

    global old_user
    main.insert_time_date(shipname, tidanhao, newtidanhao,combobox, data)
    if int(grade) == 2:
        if old_user:
            if old_user == username:
                sanhuo_tips.insert_data(shipname, tidanhao, combobox, data)
        else:
            old_user = username
            sanhuo_tips.reset_data()
            sanhuo_tips.insert_data(shipname, tidanhao, combobox, data)
    if int(grade) == 3:
        if old_user:
            if old_user == username:
                jizhuangxiang_tips.insert_data(shipname, tidanhao, combobox, data)
        else:
            old_user = username
            jizhuangxiang_tips.reset_data()
            jizhuangxiang_tips.insert_data(shipname, tidanhao, combobox, data)


def show_tips(grade):
    if int(grade) == 2:
        sanhuo_tips.show()
    elif int(grade) == 3:
        jizhuangxiang_tips.show()
    elif int(grade) == 4:
        pass
    else:
        pass


if __name__ == "__main__":
    try:
        with open(os.path.abspath(".") + "\\resource\\check\\init_sql.txt", "r") as fr:
            init_sql_dict = {key: i.strip("\n") for key, i in zip(["user", "password", "port", "ip"], fr)}
            g_User = user = init_sql_dict.get('user')
            g_Pw = password = init_sql_dict.get('password')
            g_Port = port = int(init_sql_dict.get("port"))
            g_Ip = ip = init_sql_dict.get('ip')
    except:
        pass
    app = QApplication(sys.argv)
    logon = Logon()
    app.setApplicationName("物流管理系统")
    user_sanhuo = User_operation(g_User, g_Pw, g_Port, g_Ip, username, password)
    user_jizhuangxiang = User_jizhuang(g_User, g_Pw, g_Port, g_Ip, username, password)
    logon.show()

    sanhuo_tips = Tips_on_sanhuo()
    jizhuangxiang_tips = Tips_on_jizhuangxiang()

    register = Register(logon)
    try:
        t = get_auto_logon_or_rememberpassword_data()
    except:
        pass
    main = Main_auto(g_User, g_Pw, g_Port, g_Ip, sanhuo_tips, jizhuangxiang_tips,user_sanhuo, user_jizhuangxiang,check_db_no_conn, check_user_no_conn)
    try:
        if t:
            start_main()
    except:
        pass
    main.main_change_account_number_signal.connect(start_main_to_logon)
    main.oper_signal.connect(check_oper_on)
    logon.logon_safelogon_btn_signal.connect(start_main)
    logon.logon_register_btn_signal.connect(start_register)
    register.register_signal.connect(init_mysql)
    # main.tips_real_signal.connect(real_tips_show)
    main.tips_signal.connect(show_tips)
    user_jizhuangxiang.remember_history.connect(insert_data_tips)
    user_sanhuo.remember_history.connect(insert_data_tips)
    app.exit(app.exec_())
    """
    目前构思:
        通过把main_auto的mysql提取出来,不能让他初始化数据时从数据库建表，这里可以想办法给一个选择，让他从本地那数据，
        显示main_auto界面上时给出选择从数据库里面调入数据
    """
