import pymysql
from datetime import datetime

ifudan_host = '10.221.137.167'
dom_host = '192.168.1.4'
cloud_host = '123.206.132.235'


class Connection(object):
    def connect_database(self):
        # self.connection = pymysql.connect(host=cloud_host,
        #                                   user='root',
        #                                   db='supermarket',
        #                                   passwd='a887400',
        #                                   port=3306,
        #                                   charset="utf8"
        #                                   )
        self.connection = pymysql.connect(host=cloud_host,
                                          user='root',
                                          db='test1',
                                          passwd='dbpj1008',
                                          port=4040,
                                          charset="utf8"
                                          )
        self.cursor = self.connection.cursor()

    def disconnect_database(self):
        self.cursor.close()
        self.connection.close()

    def exec_query(self, sql):
        self.cursor.execute(sql)

    def exec_update(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def fetch_cursor(self):
        return self.cursor.fetchall()


database = Connection()


def exec_staff_login(username, password):
    database.connect_database()
    sql = "SELECT * FROM staffacc WHERE empl_id='%s' AND staff_psw='%s'"
    data = (username, password)
    database.exec_query(sql % data)
    values = database.fetch_cursor()
    database.disconnect_database()
    if values:
        return True
    else:
        return False


def exec_customer_login(username, password):
    database.connect_database()
    sql = "SELECT mem_id FROM memberacc WHERE mem_name='%s' AND mem_psw='%s'"
    data = (username, password)
    database.exec_query(sql % data)
    values = database.fetch_cursor()
    database.disconnect_database()
    if values:
        return (True, values)
    else:
        return (False, 0)

def exec_supplier_login(username, password):
    database.connect_database()
    sql = "SELECT supp_id FROM supplieracc WHERE supp_usname='%s' AND supp_pswd='%s'"
    data = (username, password)
    database.exec_query(sql % data)
    values = database.fetch_cursor()
    database.disconnect_database()
    if values:
        return (True, values)
    else:
        return (False, 0)

def exec_register_customer(username, password, email):
    database.connect_database()

    sql = "SELECT * FROM memberacc WHERE mem_name='%s'"
    database.exec_query(sql % username)
    values = database.fetch_cursor()
    if values:  # if values is not empty, it indicates that username has been registered
        database.disconnect_database()
        return False
    else:
        time = str(datetime.now())  # insert a new customer
        sql = "INSERT INTO memberacc(mem_name, mem_psw, mem_mail, mem_rtime, mem_point, mem_avai) VALUES('%s','%s','%s','%s',0,true)"
        data = (username, password, email, time)
        database.exec_update(sql % data)
        database.disconnect_database()
        return True

def exec_fetch_all_information_from_customer(user_id):
    database.connect_database()
    sql = "SELECT * FROM memberacc WHERE mem_id='%d'"
    database.exec_query(sql % user_id)
    values = database.fetch_cursor()
    database.disconnect_database()
    return values

def exec_change_the_credit_customer(user_id, credits):
    database.connect_database()
    sql = "UPDATE memberacc SET mem_point = mem_point + '%d' WHERE mem_id='%d'"
    data = (credits, user_id)
    database.exec_update(sql % data)
    database.disconnect_database()

def exec_show_items():
    database.connect_database()
    sql = "SELECT * FROM item"
    database.exec_query(sql)
    values = database.fetch_cursor()
    database.disconnect_database()
    return values

def exec_change_the_information_supplier(id, password, contact, phone, email, address, note):
    database.connect_database()
    sql = "UPDATE supplieracc SET supp_pswd ='%s',supp_cname='%s',supp_mobinum='%s',supp_email='%s',supp_addr='%s',supp_note='%s' WHERE supp_id='%d'"
    data = (password, contact, phone, email, address, note, id)
    database.exec_update(sql % data)
    database.disconnect_database()

def exec_add_new_complain_to_complain_list(mem_id, comp_type, comp_content):
    database.connect_database()
    time = str(datetime.now())  # insert a new complaint
    sql = "INSERT INTO complaint(mem_id, comp_type, comp_content, comp_time) VALUES('%d','%d','%s','%s')"
    data = (mem_id, comp_type, comp_content, time)
    database.exec_update(sql % data)
    database.disconnect_database()
