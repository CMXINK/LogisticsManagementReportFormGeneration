import pymysql
def sujuquchong(str1, str2, regular, res_list=False, res_str=False):
    t1 = str1.split(regular)
    t2 = str2.split(regular)
    for i in t2:
        if i in t1:
            pass
        else:
            t1.append(i)
    if res_str:
        temp = ""
        for i in t1:
            temp += i+","
        temp = temp[:-1]
        return temp
    else:
        return t1

class Mysql:
    def __init__(self):
        super(Mysql, self).__init__()
        self.conn = pymysql.connect(user="root", password="root", port=int(3306),
                                    charset='utf8', host="127.0.0.1", db = "transport_db")
        self.cursor = self.conn.cursor()
if __name__ == "__main__":
    # str1 = "船名	航次	提单号	IMO号	国籍	启运港	目的港	起运港ETA	起运港ATB	起运港ATD	目的港ETA	货物类型	客户名称	船代公司	提单	保函	签单要求	快递单号	作业公司	报关公司	地面公司	绑扎公司	通关单号	到货时间	到期到齐	发货状态	船东名称	出单方式	海运条款	货名	件数	重量	体积	计费吨	发货人	收货人	通知人	唛头	货描	保险	递载费	报关费	改单费	分票费	电放费	熏蒸费	其他	user1"
    # str2 = "船名	航次	提单号	IMO号	启运港	目的港	起运港ETA	起运港ATB	起运港ATD	目的港ETA	货物类型	客户名称	船代公司	联系人	报关公司	地面公司	绑扎公司	船东名称	发货状态	出单方式	海运条款	货名	件数	重量	体积	计费吨	发货人	收货人	通知人	唛头	货描	预计开船日	装货港	卸货港	目的地	箱型	箱量	箱号	品名	发票抬头	填制日期	铅封号	委托单位	业务员	代理电话	user1	user2	user3"
    # regular = "\t"
    # str3 = ""
    # print(sujuquchong(str1, str3, regular, res_str=True))
    # print(str1.split("\t"))
    # sql =  "insert into transport_billing_sanhuo_data_table({}) values (%s)".format()
    t = "船名,航次,提单号,IMO号,启运港,目的港,起运港ETA,起运港ATB,起运港ATD,目的港ETA,货物类型,客户名称,船代公司,报关公司,地面公司,绑扎公司,船东名称,发货状态,出单方式,海运条款,货名,件数,重量,体积,计费吨,发货人,收货人,通知人,唛头,货描"
    t = t.split(",")
    a = ""
    for i in t:
        a+='"'+i+'"' + ","
    print(a)

