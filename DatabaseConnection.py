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
                                          db='test2',
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
    sql = "SELECT * FROM staffacc WHERE staff_id='%s' AND staff_psw='%s'"
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
    sql = "SELECT supp_id FROM supplieracc WHERE supp_name='%s' AND supp_psw='%s'"
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
        sql = "INSERT INTO memberacc(mem_name, mem_psw, mem_mail, mem_regtime, mem_point) VALUES('%s','%s','%s','%s',0)"
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

def exec_add_a_new_purchase(supplier_id, staff_id, purchase_note):
    database.connect_database()
    time = str(datetime.now())
    # add a new purchase
    sql = "INSERT INTO purchase(supp_id, staff_id, purchase_time, purchase_note) VALUES('%d','%d','%s','%s')"
    data = (supplier_id, staff_id, time, purchase_note)
    database.exec_update(sql % data)
    database.disconnect_database()

def exec_show_purchase(supplier_id):
    database.connect_database()
    sql = "SELECT * FROM purchase WHERE supp_id='%d'"
    database.exec_query(sql % supplier_id)
    purchases = database.fetch_cursor()
    database.disconnect_database()
    return purchases

def exec_show_purchase_list(purchase_id):
    database.connect_database()
    sql = "SELECT * FROM purchlist WHERE purchase_id='%d'"
    database.exec_query(sql % purchase_id)
    purchase_list = database.fetch_cursor()
    database.disconnect_database()
    return purchase_list

def exec_show_storage_imformation(store_id):
    database.connect_database()
    sql = "SELECT * FROM storage WHERE store_id='%d'"
    database.exec_query(sql % store_id)
    storage = database.fetch_cursor()
    database.disconnect_database()
    return storage

def exec_show_store_list(store_id):
    database.connect_database()
    sql = "SELECT item_id, number FROM storelist WHERE store_id='%d'"
    database.exec_query(sql % store_id)
    storage = database.fetch_cursor()
    database.disconnect_database()
    return storage

def exec_find_item_in_storage(item_id):
    database.connect_database()
    sql = "SELECT * number FROM storelist WHERE item_id='%d'"
    database.exec_query(sql % item_id)
    storage = database.fetch_cursor()
    database.disconnect_database()
    return storage

def exec_change_the_information_supplier(id, password, contact, phone, email, address, note):
    database.connect_database()
    sql = "UPDATE supplieracc SET supp_psw ='%s',supp_contact='%s',supp_phone='%s',supp_mail='%s',supp_addr='%s',supp_note='%s' WHERE supp_id='%d'"
    data = (password, contact, phone, email, address, note, id)
    database.exec_update(sql % data)
    database.disconnect_database()

def exec_change_the_information_customor(user_id, password, phone, email, note):
    database.connect_database()
    sql = "UPDATE memberacc SET mem_psw ='%s', mem_phone='%s', mem_mail='%s', mem_note='%s' WHERE mem_id='%d'"
    data = (password, phone, email, note, user_id)
    database.exec_update(sql % data)
    database.disconnect_database()

def exec_add_new_complain_to_complain_list(mem_id, comp_type, comp_content):
    database.connect_database()
    time = str(datetime.now())  # insert a new complaint
    sql = "INSERT INTO complaint(mem_id, comp_type, comp_content, comp_time) VALUES('%d','%d','%s','%s')"
    data = (mem_id, comp_type, comp_content, time)
    database.exec_update(sql % data)
    database.disconnect_database()

def exec_add_new_shopping_record(mem_id):
    database.connect_database()
    time = str(datetime.now())
    # insert a new shopping record
    sql = "INSERT INTO shopping(mem_id, shop_time) VALUES('%d','%s')"
    data = (mem_id,time)
    database.exec_update(sql % data)
    # return the shop_id
    sql = "SELECT max(shop_id) FROM shopping"
    database.exec_query(sql)
    shop_id = database.fetch_cursor()
    database.disconnect_database()
    return shop_id

def exec_add_new_shopping_list(shop_id, order_list):
    database.connect_database()
    time = str(datetime.now())
    # insert a new shopping list
    for current_item in order_list:
        item_id = current_item[0]
        item_quantity = current_item[1]
        sql = "SELECT item_price FROM item WHERE item_id = '%d'"
        database.exec_query(sql % item_id)
        item_price = database.fetch_cursor()[0][0]
        sql = "INSERT INTO shoplist VALUES('%d','%d','%.2f','%d')"
        data = (item_id, shop_id, item_price, item_quantity)
        database.exec_update(sql % data)
    database.disconnect_database()


