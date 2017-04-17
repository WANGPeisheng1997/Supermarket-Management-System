import pymysql

ifudan_host = '10.221.137.167'
dom_host = '192.168.1.4'

class Connection(object):
    def connect_database(self):
        self.connection = pymysql.connect(host=dom_host,
                                          user='root',
                                          db='supermarket',
                                          passwd='a887400',
                                          port=3306,
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
    sql = "SELECT * FROM memberacc WHERE mem_id='%s' AND mem_psw='%s'"
    data = (username, password)
    database.exec_query(sql % data)
    values = database.fetch_cursor()
    database.disconnect_database()
    if values:
        return True
    else:
        return False


def exec_register_customer(username, password, email):
    database.connect_database()
    sql = "INSERT INTO memberacc VALUES(1,'%s','%s','123213123','%s','2018-2-8',0,true,' ')"
    data = (username, password, email)
    database.exec_update(sql % data)
    database.disconnect_database()


def exec_show_items():
    database.connect_database()
    sql = "SELECT * FROM item"
    database.exec_query(sql)
    values = database.fetch_cursor()
    database.disconnect_database()
    return values
