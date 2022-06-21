import pymysql


#  关于pysqml 占位与传参:
#  数据库本身有的数据或者名称统一用format方法传参, 自己所给的字符串如查询时的values统一通过%s进行占位, 在execute中通过列表形式传参
#  当涉及到from某个位置时由于表名或者库名需要占位, 此时占位符{}要加飘点,即`{}`
class Mysql:
    def __init__(self, user, password, port, ip):
        self.conn = pymysql.connect(user=user, password=password, port=int(port),
                                    charset='utf8', host=ip)
        self.cursor = self.conn.cursor()
        super(Mysql, self).__init__()
        self.create_db()

    def check_db(self):
        sql = 'use transport_db'
        self.cursor.execute(sql)
        sql = 'show tables;'
        reply = self.cursor.execute(sql)
        self.cursor.close()
        self.conn.close()
        return reply

    def create_db(self):
        sql = 'create database if not exists transport_db'
        self.cursor.execute(sql)

        sql = 'use transport_db'
        self.cursor.execute(sql)
        # 船名 varchar(255), 航次 varchar(255)," \
        #               "提单号 varchar(255),IMO号 varchar(255), 启运港 varchar(255), 目的港 varchar(255), 起运港ETA varchar(255), " \
        #               "起运港ATB varchar(255), 起运港ATD varchar(255), 目的港ETA varchar(255), 货物类型 varchar(255), 客户名称 varchar(255)," \
        #               " 船代公司 varchar(255), 联系人 varchar(255), 报关公司 varchar(255), 地面公司 varchar(255), 绑扎公司 varchar(255)," \
        #               " 船东名称 varchar(255), 发货状态 varchar(255), 出单方式 varchar(255), 海运条款 varchar(255), 货名 varchar(255)," \
        #               " 件数 varchar(255), 重量 varchar(255), 体积 varchar(255), 计费吨 varchar(255)," \
        #               " 发货人 varchar(255), 收货人 varchar(255), 通知人 varchar(255), 唛头 varchar(255)," \
        #               "货描 varchar(255), 预计开船日 varchar(255), 装货港 varchar(255), 卸货港 varchar(255), 目的地 varchar(255), 箱型 varchar(255)," \
        #               "箱量 varchar(255), 箱号 varchar(255), 品名 varchar(255), 发票抬头 varchar(255), 填制日期 varchar (255),铅封号 varchar(255), 委托单位 varchar(255)," \
        #               "业务员 varchar(255), 代理电话 varchar(255), user1 varchar(255), user2 varchar(255), user3 varchar(255)
        sql = "create table if not exists transport_billing_data_table(船名 varchar(255),航次 varchar(255),提单号 varchar(255),IMO号 varchar(255),国籍 varchar(255),启运港 varchar(255),目的港 varchar(255),起运港ETA varchar(255),起运港ATB varchar(255),起运港ATD varchar(255),目的港ETA varchar(255),货物类型 varchar(255),客户名称 varchar(255),船代公司 varchar(255),提单 varchar(255),保函 varchar(255),签单要求 varchar(255),快递单号 varchar(255),作业公司 varchar(255),报关公司 varchar(255),地面公司 varchar(255),绑扎公司 varchar(255),通关单号 varchar(255),到货时间 varchar(255),到期到齐 varchar(255),发货状态 varchar(255),船东名称 varchar(255),出单方式 varchar(255),海运条款 varchar(255),货名 varchar(255),件数 varchar(255),重量 varchar(255),体积 varchar(255),计费吨 varchar(255),发货人 varchar(255),收货人 varchar(255),通知人 varchar(255),唛头 varchar(255),货描 varchar(255),保险 varchar(255),递载费 varchar(255),报关费 varchar(255),改单费 varchar(255),分票费 varchar(255),电放费 varchar(255),熏蒸费 varchar(255),其他 varchar(255),预计开船日 varchar(255),装货港 varchar(255),卸货港 varchar(255),目的地 varchar(255),箱型 varchar(255),箱量 varchar(255),箱号 varchar(255),品名 varchar(255),发票抬头 varchar(255),填制日期 varchar(255),铅封号 varchar(255),委托单位 varchar(255),业务员 varchar(255),代理电话 varchar(255),下货纸 varchar(255),散货结算单 varchar(255),散货确认单 varchar(255),产装通知 varchar(255), 集装结算单 varchar(255), 集装确认单 varchar(255),集港通知 varchar(255), 提单样本 varchar(255), 装箱委托书 varchar(255),user1 varchar(255),user2 varchar(255),user3 varchar(255));"
        self.cursor.execute(sql)

        sql = "create table if not exists transport_billing_sanhuo_data_table as select 船名,航次,提单号,IMO号,国籍,启运港,目的港,起运港ETA,起运港ATB,起运港ATD,目的港ETA,货物类型,客户名称,船代公司,提单,保函,签单要求,快递单号,作业公司,报关公司,地面公司,绑扎公司,通关单号,到货时间,到期到齐,发货状态,船东名称,出单方式,海运条款,货名,件数,重量,体积,计费吨,发货人,收货人,通知人,唛头,货描,保险,递载费,报关费,改单费,分票费,电放费,熏蒸费,其他,下货纸,散货结算单,散货确认单,user1 from transport_billing_data_table;"
        # "船名,航次," \
        # "提单号,IMO号,启运港,目的港,起运港ETA," \
        # "起运港ATB,起运港ATD,目的港ETA,货物类型,客户名称," \
        # "船代公司, 联系人, 报关公司, 地面公司, 绑扎公司," \
        # " 船东名称, 发货状态, 出单方式, 海运条款, 货名," \
        # " 件数, 重量, 体积, 计费吨," \
        # " 发货人, 收货人, 通知人, 唛头," \
        # "货描, user1 " \

        self.cursor.execute(sql)
        sql = "create table if not exists transport_billing_jizhuangxiang_data_table as select 船名,航次," \
              "提单号,预计开船日,启运港,装货港,卸货港,目的地,箱型,箱量,箱号,品名,发票抬头,填制日期," \
              "铅封号,委托单位," \
              "业务员, 代理电话," \
              "发货状态, 出单方式,货名," \
              " 件数, 重量, 体积, 计费吨," \
              " 发货人, 收货人, 通知人, 唛头," \
              "货描," \
              "产装通知,集装结算单,集装确认单,集港通知,提单样本,装箱委托书,user2 from transport_billing_data_table"
        self.cursor.execute(sql)
        sql = 'create table if not exists user_password_table(user varchar(255) unique, password varchar(255), grade varchar(255))'
        self.cursor.execute(sql)
        sql = 'select 客户名称 from transport_billing_data_table;'
        reply = self.cursor.execute(sql)
        self.cursor.fetchall()
        if not reply:
            sql = 'insert into transport_billing_data_table(客户名称) values("test")'
            self.conn.commit()
            self.cursor.execute(sql)

    def select_if_complate_data(self, selectdata: list, grade: str):
        res_data = ""
        if grade == "2":
            num = '0'
            for index, i in enumerate(selectdata[1:]):
                if i in ["确认单", "结算单"]:
                    i = "散货" + i
                sql = "select {} from transport_billing_sanhuo_data_table where 提单号=%s;".format(i)
                res = self.cursor.execute(sql, [selectdata[0].get("tidanhao_num"), ])
                if res:
                    num = str(int(num) + 1)
                    data = list(self.cursor.fetchall())
                    if data[0][0]:
                        num = str(int(num) - 1)  # 表示已经已经保存过了
                    else:
                        res_data += "{}: ".format(num) + i.replace('散货', '') + "<br>"  # 表示还没有保存过
                else:
                    return False

        if grade == "3":
            num = '0'
            for index, i in enumerate(selectdata[1:]):
                if i in ["费用确认单", "费用结算单"]:
                    i = "集装" + i[2:]
                sql = "select {} from transport_billing_jizhuangxiang_data_table where 提单号=%s;".format(i)
                res = self.cursor.execute(sql, [selectdata[0].get("tidanhao_num"), ])
                if res:
                    num = str(int(num) + 1)
                    data = list(self.cursor.fetchall())
                    if data[0][0]:
                        print("data[0][0]============>", data[0][0])
                        num = str(int(num) - 1)  # 表示已经已经保存过了
                    else:
                        res_data += "{}: ".format(num) + i.replace('集装', '费用') + "<br>"  # 表示还没有保存过
                else:
                    return False

        return res_data if res_data else "all_exists"  # all_exists表示所有的都存在了

    # 检测operation表是否显示(散货已经单独拿出不在这个函数中处理)
    def check_oper(self, text, grade):
        global table
        sql = 'select 提单号 from transport_billing_data_table where 提单号=%s;'
        reply = self.cursor.execute(sql, [text, ])
        if reply:
            if int(grade) == 1:
                table = 'transport_billing_data_table'
            elif int(grade) == 2:
                table = 'transport_billing_sanhuo_data_table'
            elif int(grade) == 3:
                table = 'transport_billing_jizhuangxiang_data_table'
            elif int(grade) == 4:
                table = 'transport_billing_caiwu_data_table'
            sql = "select COlUMN_NAME from information_schema.COLUMNS where table_name= %s; "
            self.cursor.execute(sql, [table, ])
            table_column = self.cursor.fetchall()
            temp = []
            for i in table_column:
                temp.append(i[0])
            table_column = temp
            temp = ""
            for i in table_column:
                temp += i + ","
            temp = temp[:-1]
            table_column = temp
            sql = 'select {} from transport_billing_data_table where 提单号=%s'.format(table_column)

            self.cursor.execute(sql, [text, ])
            data = self.cursor.fetchall()
            self.cursor.close()
            return data
        else:
            return False

    def sanhuo_data(self, tidanhao):  # 散货拿取数据到operation表中
        print("--------------------------------"
              "------------------------", tidanhao)
        sql = "select 船名,航次,提单号,IMO号,启运港,目的港,起运港ETA,起运港ATB,起运港ATD,目的港ETA,货物类型,客户名称,船代公司,报关公司,地面公司,绑扎公司,船东名称,发货状态,出单方式,海运条款,货名,件数,重量,体积,计费吨,发货人,收货人,通知人,唛头,货描 from transport_billing_sanhuo_data_table where 提单号 = %s;"
        res = self.cursor.execute(sql, [tidanhao, ])
        if res:
            t = self.cursor.fetchall()
            return t
        else:
            return False

    # 得到同部门的的所有数据
    def get_level_data(self, grade):
        """

        :param grade: 等级, int
        :return: sql
        """
        if int(grade) == 2:
            sql2 = "select COlUMN_NAME from information_schema.COLUMNS where table_name= 'transport_billing_sanhuo_data_table';"
            res = self.cursor.execute(sql2)
            t2 = self.cursor.fetchall()
            t_column = []
            for i in t2:
                t_column.append(i[0])
            sql = "select * from transport_billing_sanhuo_data_table order by 1 asc, 2 asc, 3 asc;"
            res = self.cursor.execute(sql)
            t = self.cursor.fetchall()
            res = [t_column, [i for i in t if i[0]]]

        elif int(grade) == 3:
            sql3 = "select COlUMN_NAME from information_schema.COLUMNS where table_name= 'transport_billing_jizhuangxiang_data_table';"
            res = self.cursor.execute(sql3)
            t3 = self.cursor.fetchall()
            sql = "select * from transport_billing_jizhuangxiang_data_table order by 1 asc, 2 asc, 3 asc;"
            res = self.cursor.execute(sql)
            t_column = []
            for i in t3:
                t_column.append(i[0])
            t = self.cursor.fetchall()
            res = [t_column, [i for i in t if i[0]]]
        elif int(grade) == 4:
            # 财务没写
            # sql4 = "select COlUMN_NAME from information_schema.COLUMNS where table_name= '';"
            sql = "select * from transport_billing_sanhuo_data_table;"
            res = self.cursor.execute(sql)
        if res:
            return res
        else:
            return False

    def get_transport_billing_data_table(self):
        # sql = 'select * from transport_billing_data_table;'
        # self.cursor.execute(sql)
        # transport_data = self.cursor.fetchall()
        # return transport_data
        sql = "select COlUMN_NAME from information_schema.COLUMNS where table_name= 'transport_billing_data_table'; "
        self.cursor.execute(sql)
        table_columns = self.cursor.fetchall()
        sql = 'select * from transport_billing_data_table order by 1 asc, 2 asc, 3 asc;'
        reply = self.cursor.execute(sql)
        if reply:
            data = self.cursor.fetchall()
            self.cursor.close()
            return table_columns, data

    def modify_transport_billing_data_table(self, modify_index, modify_column, modify_data):
        sql = 'update transport_billing_data_table set %s = %s where index= %s'
        self.cursor.execute(sql, [modify_index, modify_data, modify_index])

    # 散货得到数据
    def get_sanhuo_data(self, user):
        sql = "select COlUMN_NAME from information_schema.COLUMNS where table_name= 'transport_billing_sanhuo_data_table'; "
        self.cursor.execute(sql)
        table_columns = self.cursor.fetchall()
        sql = 'select * from transport_billing_sanhuo_data_table where user1= %s order by 1 asc, 2 asc, 3 asc;'
        reply = self.cursor.execute(sql, [str(user), ])
        if reply:
            data = self.cursor.fetchall()

            self.cursor.close()
            return table_columns, data

    # 集装箱得到数据
    def get_jizhuangxiang_data(self, user):
        sql = "select COlUMN_NAME from information_schema.COLUMNS where table_name= 'transport_billing_jizhuangxiang_data_table'; "
        self.cursor.execute(sql)
        table_columns = self.cursor.fetchall()
        sql = 'select * from transport_billing_jizhuangxiang_data_table where user2= %s order by 1 asc, 2 asc, 3 asc;'
        reply = self.cursor.execute(sql, [str(user), ])
        if reply:
            data = self.cursor.fetchall()
            self.cursor.close()
            return table_columns, data

    # mian_auto_replace_on 保存数据
    def save_transport_billing_data_table(self, data, grade, user):
        try:
            global reply, sql, tabelname
            if int(grade) == 1:
                tabelname = "transport_billing_data_table"
                sql = "select COlUMN_NAME from information_schema.COLUMNS where table_name= 'transport_billing_data_table'; "

            elif int(grade) == 2:
                tabelname = "transport_billing_sanhuo_data_table"
                sql = "select COlUMN_NAME from information_schema.COLUMNS where table_name= 'transport_billing_sanhuo_data_table'; "
            elif int(grade) == 3:
                tabelname = "transport_billing_jizhuangxiang_data_table"
                sql = "select COlUMN_NAME from information_schema.COLUMNS where table_name= 'transport_billing_jizhuangxiang_data_table'; "
            elif int(grade) == 4:
                tabelname = "transport_billing_caiwu_data_table"
                sql = "select COlUMN_NAME from information_schema.COLUMNS where table_name= 'transport_billing_caiwu_data_table'; "
            self.cursor.execute(sql)
            reply = self.cursor.fetchall()
            temp = []
            for i in reply:
                temp.append(i[0])
            reply = temp
            t = "%s," * len(reply)
            t_right = t[:-1]
            if grade > 1:
                sql = "delete from `{}` where {} = %s".format(tabelname, reply[-1])
                self.cursor.execute(sql, [user])
                self.conn.commit()
                for i in range(len(data)):
                    data[i][-1] = user
                    sql = 'insert into `{}` values({}) '.format(tabelname, t_right)
                    self.cursor.execute(sql, data[i])
                self.conn.commit()
                for i in range(0, len(data)):
                    sql = "select 提单号 from transport_billing_data_table where 提单号=%s;"
                    exit_table = self.cursor.execute(sql, [data[i][2], ])
                    if exit_table:
                        for j in range(0, len(reply)):
                            sql = "update transport_billing_data_table set {} = %s where 提单号=%s".format(reply[j])

                            self.cursor.execute(sql, [data[i][j], data[i][2]])
                    else:
                        reply_str = reply[0]
                        for k in range(1, len(reply)):
                            reply_str += ',' + reply[k]
                        sql = "insert into transport_billing_data_table({}) values({})".format(reply_str, t_right)
                        self.cursor.execute(sql, data[i])
                        self.conn.commit()
            else:
                sql = "truncate table transport_billing_data_table"
                self.cursor.execute(sql)
                for i in range(0, len(data)):
                    sql = "insert into transport_billing_data_table values({})".format(t_right)
                    self.cursor.execute(sql, data[i])
            self.conn.commit()
            self.cursor.close()
            return True
            # for i in reply:
            #     tabelname = "transport_billing_data_table"
            #     sql = "update `%s` set {} = %s where {} = %s".format(i, reply[-1])
            #     self.cursor.execute(sql, [tabelname, user])
        except:
            return False

    # main_auto_place恢复数据
    def recover_transport_data_table(self, grade, user):
        global table_name, sql
        if int(grade) == 1:
            pass
        elif int(grade) == 2:
            table_name = "transport_billing_sanhuo_data_table"
            sql = "select COlUMN_NAME from information_schema.COLUMNS where table_name= 'transport_billing_sanhuo_data_table'; "
        elif int(grade) == 3:
            table_name = "transport_billing_jizhuangxiang_data_table"
            sql = "select COlUMN_NAME from information_schema.COLUMNS where table_name= 'transport_billing_jizhuangxiang_data_table'; "
        elif int(grade) == 4:
            table_name = "transport_billing_caiwu_data_table"
            pass
        if grade > 1:
            self.cursor.execute(sql)
            table_column = self.cursor.fetchall()
            temp = []
            for i in table_column:
                temp.append(i[0])
            table_column_list = temp
            temp = ""
            for i in table_column_list:
                temp += i + ","
            temp = temp[:-1]
            table_column = temp
            sql = "delete from `{}` where {} = %s".format(table_name, table_column_list[-1])
            self.cursor.execute(sql, [user, ])
            sql = "insert into `{}` select {} from transport_billing_data_table where {} = %s".format(table_name,
                                                                                                      table_column,
                                                                                                      table_column_list[
                                                                                                          -1])
            self.cursor.execute(sql, [user, ])
            self.cursor.close()
            self.conn.close()

    # 拿去船名和提单号
    def get_sheeps_data(self, type_user, user, grade):
        global table_name
        if int(grade) == 1:
            table_name = "transport_billing_data_table"
        elif int(grade) == 2:
            table_name = "transport_billing_sanhuo_data_table"
        elif int(grade) == 3:
            table_name = "transport_billing_jizhuangxiang_data_table"
        elif int(grade) == 4:
            pass
        sql = 'select 船名, 航次 from `{}` where {} = %s order by 1 asc, 2 asc;'.format(table_name, type_user)
        self.cursor.execute(sql, user)
        data = self.cursor.fetchall()
        return data

    # 得到每个表字段
    def check_coumn(self):
        sql = "select COlUMN_NAME from information_schema.COLUMNS where table_name= 'transport_billing_data_table';"
        self.cursor.execute(sql)
        reply_all = self.cursor.fetchall()
        temp = []
        for i in reply_all:
            temp.append(i[0])
        reply_all = temp

        sql = "select COlUMN_NAME from information_schema.COLUMNS where table_name= 'transport_billing_sanhuo_data_table';"
        self.cursor.execute(sql)
        reply_sanhuo = self.cursor.fetchall()
        temp = []
        for i in reply_sanhuo:
            temp.append(i[0])
        reply_sanhuo = temp

        sql = "select COlUMN_NAME from information_schema.COLUMNS where table_name= 'transport_billing_jizhuangxiang_data_table';"
        self.cursor.execute(sql)
        reply_jizhuangxiang = self.cursor.fetchall()
        temp = []
        for i in reply_jizhuangxiang:
            temp.append(i[0])
        reply_jizhuangxiang = temp
        check_table_column = [reply_all, reply_sanhuo, reply_jizhuangxiang]
        return check_table_column

    def get_tidanhao_data(self, sheep_name, sheep_num, type_user, user, grade):
        global table_name
        if int(grade) == 1:
            table_name = "transport_billing_data_table"
        elif int(grade) == 2:
            table_name = "transport_billing_sanhuo_data_table"
        elif int(grade) == 3:
            table_name = "transport_billing_jizhuangxiang_data_table"
        elif int(grade) == 4:
            pass
        sql = 'select 提单号 from `{}` where 船名 = %s and 航次 = %s and {} = %s order by 提单号;'.format(table_name, type_user)
        self.cursor.execute(sql, [sheep_name, sheep_num, user, ])
        data = self.cursor.fetchall()
        list_data = []
        for i in data:
            list_data.append(i[0])
        return list_data

    def user_password_table(self, username, password):
        sql = "select  grade  from user_password_table where user = %s and password = %s;"
        reply = self.cursor.execute(sql, (username, password))
        if reply:
            select_result = self.cursor.fetchone()
            self.cursor.close()
            self.conn.close()
            return int(select_result[0])
        else:
            return 0

    def get_staff_user(self, grade):
        sql = 'select user from user_password_table where grade=%s;'
        reply = self.cursor.execute(sql, [str(grade), ])
        if reply:
            data = self.cursor.fetchall()
            list_data = []
            for i in data:
                list_data.append(i[0])
            self.cursor.close()
            return list_data

    # 保存oper操作表
    def save_oper_table(self, data, user, grade):
        global sql, table
        if int(grade) == 2:
            table = 'transport_billing_sanhuo_data_table'
            sql = "select COlUMN_NAME from information_schema.COLUMNS where table_name= 'transport_billing_sanhuo_data_table' ;"
        if int(grade) == 3:
            table = 'transport_billing_jizhuangxiang_data_table'
            sql = "select COlUMN_NAME from information_schema.COLUMNS where table_name= 'transport_billing_jizhuangxiang_data_table' ;"
        if int(grade) == 4:
            pass
        self.cursor.execute(sql)
        reply_oper = self.cursor.fetchall()
        sql = "select 提单号 from `{}` where {} = %s ;".format(table, reply_oper[-1][0])
        check = self.cursor.execute(sql, user)
        if not check:
            return False
        sql = "delete from `{}` where 提单号=%s and {}=%s".format(table, reply_oper[-1][0])
        self.cursor.execute(sql, [data[2], user])
        placeholder = ""
        for i in range(0, len(reply_oper)):
            placeholder += "%s,"
        placeholder = placeholder[:-1]
        sql = "insert into `{}` values({})".format(table, placeholder)
        print("===============================data=====================================================", data)
        print("len(data)=", len(data), "len(columns)=", len(reply_oper), "reply_oper=", reply_oper)
        self.cursor.execute(sql, data)
        temp = []
        for i in reply_oper:
            temp.append(i[0])
        reply_oper = temp
        for i in range(len(reply_oper)):
            sql = "update transport_billing_data_table set {} = %s where 提单号=%s".format(reply_oper[i])
            self.cursor.execute(sql, [data[i], data[2]])
        self.conn.commit()
        self.cursor.close()
        return True

    def save_sanhuo_oper(self, tidanhao, data):
        sql = "select user1 from transport_billing_sanhuo_data_table where 提单号 = %s"
        self.cursor.execute(sql, [tidanhao, ])
        user = self.cursor.fetchall()[0][0]

        data = data[:-1]
        oper_sanhuo_ui_template = ["船名", "航次", "提单号", "IMO号", "启运港", "目的港", "起运港ETA", "起运港ATB", "起运港ATD", "目的港ETA",
                                   "货物类型", "客户名称", "船代公司", "报关公司", "地面公司", "绑扎公司", "船东名称", "发货状态", "出单方式", "海运条款", "货名",
                                   "件数", "重量", "体积", "计费吨", "发货人", "收货人", "通知人", "唛头", "货描"]
        if data[2] != tidanhao:
            tidanhao = data[2]
            sql = "select 提单号 from transport_billing_data_table where 提单号 = %s"
            if not self.cursor.execute(sql, [data[2], ]):
                sql = "insert into transport_billing_data_table(提单号, user1) values(%s, %s)"
                self.cursor.execute(sql, [tidanhao, user])
            sql = "select 提单号 from transport_billing_sanhuo_data_table where 提单号 = %s"
            if not self.cursor.execute(sql, [data[2], ]):
                sql = "insert into transport_billing_sanhuo_data_table(提单号, user1) values(%s, %s)"
                self.cursor.execute(sql, [tidanhao, user])

        for i, j in zip(data, oper_sanhuo_ui_template):
            sql = "update transport_billing_data_table set {} = %s where 提单号=%s".format(j)
            self.cursor.execute(sql, [i, tidanhao])
            sql = "update transport_billing_sanhuo_data_table set {} = %s where 提单号=%s".format(j)
            self.cursor.execute(sql, [i, tidanhao])

    def save_sanhuo_oper(self, tidanhao, data):
        sql = "select user1 from transport_billing_sanhuo_data_table where 提单号 = %s"
        self.cursor.execute(sql, [tidanhao, ])
        user = self.cursor.fetchall()[0][0]

        data = data[:-1]
        oper_sanhuo_ui_template = ["船名", "航次", "提单号", "IMO号", "启运港", "目的港", "起运港ETA", "起运港ATB", "起运港ATD", "目的港ETA",
                                   "货物类型", "客户名称", "船代公司", "报关公司", "地面公司", "绑扎公司", "船东名称", "发货状态", "出单方式", "海运条款",
                                   "货名",
                                   "件数", "重量", "体积", "计费吨", "发货人", "收货人", "通知人", "唛头", "货描"]
        if data[2] != tidanhao:
            tidanhao = data[2]
            sql = "select 提单号 from transport_billing_data_table where 提单号 = %s"
            if not self.cursor.execute(sql, [data[2], ]):
                sql = "insert into transport_billing_data_table(提单号, user1) values(%s, %s)"
                self.cursor.execute(sql, [tidanhao, user])
            sql = "select 提单号 from transport_billing_sanhuo_data_table where 提单号 = %s"
            if not self.cursor.execute(sql, [data[2], ]):
                sql = "insert into transport_billing_sanhuo_data_table(提单号, user1) values(%s, %s)"
                self.cursor.execute(sql, [tidanhao, user])

        for i, j in zip(data, oper_sanhuo_ui_template):
            sql = "update transport_billing_data_table set {} = %s where 提单号=%s".format(j)
            self.cursor.execute(sql, [i, tidanhao])
            sql = "update transport_billing_sanhuo_data_table set {} = %s where 提单号=%s".format(j)
            self.cursor.execute(sql, [i, tidanhao])

    def save_jizhuangxiang_oper(self, tidanhao, data):
        sql = "select user2 from transport_billing_jizhuangxiang_data_table where 提单号 = %s"
        self.cursor.execute(sql, [tidanhao, ])
        user = self.cursor.fetchall()[0][0]

        data = data[:-1]
        """
            self.chuanming_lineedit, self.hangci_lineedit, self.tidanhao_lineedit,
             self.yujikaichuanri_lineedit, self.zhuanghuogang_lineedit, self.xiehuogang_lineedit,
             self.mudidi_lineedit, self.xiangxing_lineedit, self.xiangliang_lineedit,
             self.xianghao_lineedit, self.pinming_lineedit, self.fapiaotaitou_lineedit,
             self.zhibiaoriqi_lineedit, self.qianfenghao_lineedit, self.weituodanwei_lineedit,
             self.yewuyuan_lineedit, self.dailidianhua_lineedit,
             self.huoming_lineedit, self.jianshu_lineedit, self.zhongliang_lineedit,
             self.tiji_lineedit_2, self.jifeidun_lineedit, self.fahuoren_textedit,
             self.shouhuoren_textedit, self.tongzhiren_textedit, self.maitou_textedit,
             self.huomiao_textedit
        """
        oper_sanhuo_ui_template = ["船名", "航次", "提单号", "预计开船日", "装货港", "卸货港", "目的地", "箱型", "箱量", "箱号",
                                   "品名", "发票抬头", "填制日期", "铅封号", "委托单位", "业务员", "代理电话", "发货状态", "出单方式",
                                   "货名",
                                   "件数", "重量", "体积", "计费吨", "发货人", "收货人", "通知人", "唛头", "货描"]
        if data[2] != tidanhao:
            tidanhao = data[2]
            sql = "select 提单号 from transport_billing_data_table where 提单号 = %s"
            if not self.cursor.execute(sql, [data[2], ]):
                sql = "insert into transport_billing_data_table(提单号, user2) values(%s, %s)"
                self.cursor.execute(sql, [tidanhao, user])
            sql = "select 提单号 from transport_billing_jizhuangxiang_data_table where 提单号 = %s"
            if not self.cursor.execute(sql, [data[2], ]):
                sql = "insert into transport_billing_jizhuangxiang_data_table(提单号, user2) values(%s, %s)"
                self.cursor.execute(sql, [tidanhao, user])

        for i, j in zip(data, oper_sanhuo_ui_template):
            sql = "update transport_billing_data_table set {} = %s where 提单号=%s".format(j)
            self.cursor.execute(sql, [i, tidanhao])
            sql = "update transport_billing_jizhuangxiang_data_table set {} = %s where 提单号=%s".format(j)
            self.cursor.execute(sql, [i, tidanhao])

    def get_user_password_data(self, user=False, user_password=False, user_password_grade=False):
        """

        :param user: Bool
        :param user_password: Bool
        :param user_password_grade: Bool
        :return: list/tuple
        """
        sql = "select  * from user_password_table;"
        reply = self.cursor.execute(sql)
        if reply:
            select_result = self.cursor.fetchall()
            self.cursor.close()

            if user:
                return [i[0] for i in select_result]
            if user_password:
                return [i[0] + "--" + i[1] for i in select_result]
            if user_password_grade:
                return select_result

    # 管理员添加新成员
    def add_user(self, user, password, grade):
        sql = "insert into user_password_table values(%s, %s, %s);"
        reply = self.cursor.execute(sql, [user, password, grade])
        if int(grade) == 2:
            sql = "insert into transport_billing_sanhuo_data_table(user1) values (%s);"
            reply = self.cursor.execute(sql, [user, ])
        elif int(grade) == 3:
            sql = "insert into transport_billing_jizhuangxiang_data_table(user2) values (%s);"
            reply = self.cursor.execute(sql, [user, ])
        self.conn.commit()
        self.cursor.close()
        return reply

    # 管理和更新用户
    def manager_staff(self, user, password, newuser, newpassword):
        """
        :param user: 旧用户名
        :param password: 新用户名
        :param newuser: 旧密码
        :param newpassword: 新密码
        :return: bool,Ture-->存在该用户, False-->旧用户不存在
        """
        sql = "select grade from user_password_table where user=%s and password=%s;"
        self.cursor.execute(sql, [user, password, ])
        try:
            greade_name = "user"+str(int(self.cursor.fetchone()[0])-1)
        except:
            return False
        sql = "update user_password_table set user = %s, password = %s where user=%s and password = %s"
        self.cursor.execute(sql, [newuser, newpassword, user, password, ])
        sql = "update transport_billing_data_table set {} = %s where {}=%s".format(greade_name, greade_name)
        self.cursor.execute(sql, [newuser, user, ])
        try:
            sql = "update transport_billing_sanhuo_data_table set {} = %s where {}=%s".format(greade_name, greade_name)
            self.cursor.execute(sql, [newuser, user, ])
        except:
            pass
        try:
            sql = "update transport_billing_jizhuangxiang_data_table set {} = %s where {}=%s".format(greade_name,
                                                                                                 greade_name)
            self.cursor.execute(sql, [newuser, user, ])
        except:
            pass
        self.conn.commit()
        self.cursor.close()
        return True

    def history_find(self, user, grade):
        if int(grade) == 2:
            table = "transport_billing_sanhuo_data_table"
            sql = "select 船名,航次,提单号,IMO号,国籍,启运港,目的港,起运港ETA,起运港ATB,起运港ATD,目的港ETA,货物类型,客户名称,船代公司,提单,保函,签单要求,快递单号,作业公司,报关公司,地面公司,绑扎公司,通关单号,到货时间,到期到齐,发货状态,船东名称,出单方式,海运条款,货名,件数,重量,体积,计费吨,发货人,收货人,通知人,唛头,货描,保险,递载费,报关费,改单费,分票费,电放费,熏蒸费,其他,下货纸,散货结算单,散货确认单,user1 from transport_billing_data_table where user1 = %s and 下货纸 !='' and 散货结算单 != '' and 散货确认单 != '';"
        elif int(grade) == 3:
            table = "transport_billing_jizhuangxiang_data_table"
            sql = "select 船名,航次," \
                  "提单号,预计开船日,启运港,装货港,卸货港,目的地,箱型,箱量,箱号,品名,发票抬头,填制日期," \
                  "铅封号,委托单位," \
                  "业务员, 代理电话," \
                  "发货状态, 出单方式,货名," \
                  " 件数, 重量, 体积, 计费吨," \
                  " 发货人, 收货人, 通知人, 唛头," \
                  "货描," \
                  "产装通知,集装结算单,集装确认单,集港通知,提单样本,装箱委托书,user2 from transport_billing_data_table where user2 = %s and 产装通知 != '' and 集装结算单 != '' and 集装确认单 != '' and 集港通知 != '' and 提单样本 != '' and 装箱委托书 != '';"
        self.cursor.execute(sql, [user, ])
        data_data = self.cursor.fetchall()
        sql = "select COlUMN_NAME from information_schema.COLUMNS where table_name= %s ;"
        self.cursor.execute(sql, [table, ])
        data_column = self.cursor.fetchall()
        data = []
        data_list_column = []
        for i in data_column:
            data_list_column.append(i[0])

        data.append(data_list_column)
        data.append(data_data)
        return data

    def save_sanhuo_time(self, tidanhao, new_tidanhao, combobox_data, history_data):
        # 由于前面页面的原因导致最终结算单与确认单出现了数据交换的错误,因此以下将两者交换回来
        history_data["确认单"], history_data["结算单"] = history_data["结算单"], history_data["确认单"]
        if tidanhao == new_tidanhao:
            pass
        else:
            tidanhao = new_tidanhao
        for i in ["下货纸", "散货结算单", "散货确认单"]:
            temp = i
            sql = "update transport_billing_data_table set {} = %s where 提单号=%s".format(temp)
            if i == "散货结算单" or i == "散货确认单":
                i = i[2:]
            if history_data.get(i):
                self.cursor.execute(sql, [history_data.get("time"), tidanhao])

                sql = "update transport_billing_sanhuo_data_table set {} = %s where 提单号=%s".format(temp)
                self.cursor.execute(sql, [history_data.get("time"), tidanhao])
        self.cursor.close()

    def save_jizhuangxiang_time(self, tidanhao, new_tidanhao, combobox_data, history_data):
        print("history_data=", history_data)
        if tidanhao == new_tidanhao:
            pass
        else:
            tidanhao = new_tidanhao
        for i in ["产装通知", "集装结算单", "集装确认单", "集港通知", "提单样本", "装箱委托书"]:
            temp = i
            sql = "update transport_billing_data_table set {} = %s where 提单号=%s".format(temp)
            if i == "集装结算单" or i == "集装确认单":
                i = "费用" + i[2:]
            if history_data.get(i):
                self.cursor.execute(sql, [history_data.get("time"), tidanhao])

                sql = "update transport_billing_jizhuangxiang_data_table set {} = %s where 提单号=%s".format(temp)
                self.cursor.execute(sql, [history_data.get("time"), tidanhao])
        self.cursor.close()


if __name__ == '__main__':
    # Mysql("root", "root", 3306, "127.0.0.1").create_db()
    # print(Mysql("root", "root", 3306, "127.0.0.1").sanhuo_data("num1"))
    # data = Mysql("root", "root", 3306, "127.0.0.1").get_transport_billing_data_table()
    # print(data[1][0])
    # print(Mysql("root", "root", 3306, "127.0.0.1").get_sheeps_data('user1', "a"))
    # print(Mysql("root", "root", 3306, "127.0.0.1").get_staff_user('3'))
    # list_data = []
    # for i in data[0]:
    #     list_data.append(i[0])
    # print(list_data)
    # print(Mysql("root", "root", 3306, "127.0.0.1").user_password_table('cmx', 'hellokitty'))
    # print(Mysql("root", "root", 3306, "127.0.0.1").get_sanhuo_data("b"))
    # print(Mysql("root", "root", 3306, "127.0.0.1").get_level_data(2))
    # print(Mysql("root", "root", 3306, "127.0.0.1").manager_staff(
    #     "hxx", "hxx", "", ""))
    pass
