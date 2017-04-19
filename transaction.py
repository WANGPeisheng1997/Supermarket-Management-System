# -*-coding:utf-8-*-
import DatabaseConnection


def show_all_items_for_customer():
    items = DatabaseConnection.exec_show_items()
    return items


def process_purchase(user_id, order_list):
    pass
    # TODO 没额外说明的就没有返回值
    # TODO DatabaseConnection.add_new_purchase_record_to_table_purchlist(user_id, order_list)
    # TODO DatabaseConnection.add_new_purchase_record_to_table_purchase(user_id, order_list)
    # TODO DatabaseConnection.change_the_credit_customer_in_table_memberacc(user_id, order_list)
    # TODO DatabaseConnection.change_the_number_of_items_in_table_shelf_list(order_list)


def process_complain(user_id, complain_type, complain_content):
    DatabaseConnection.exec_add_new_complain_to_complain_list(user_id, complain_type, complain_content)


def process_edit_customer_info(user_id, telephone, email, notes):
    pass
    # TODO 注意用户自己不能编辑ID，用户名和用户密码，所以new_customer_info是不含user_id， 用户名，用户密码的列表
    # TODO DatabaseConnection.change_user_information_in_table_memberacc(user_id, telephone, email, notes)


def process_search_itmes_for_customer(search_string):
    pass
    # TODO 返回给我满足商品名称与search_string部分匹配的items的二维数组
    # TODO DatabaseConnection.match_items = DatabaseConnection.search_matched_from_table_items(search_string)
    # return match_items

def show_all_information_of_customer(user_id):
    pass
    # TODO 返回编号为user_id的用户的所有信息，二维数组
    # TODO user_info = DatabaseConnection.fetch_all_customer_information_from_table(user_id)
    # return user_info

def show_all_purchase_history_of_customer(user_id):
    pass
    # TODO 返回编号为user_id的用户的购买历史，格式为商品名，购买时间，单价格，(先不考虑商品数量的事情) 联合purchlist，item和purchase表搜索
    # TODO history = fetch_all_records_from_table(user_id)
    # TODO return history_