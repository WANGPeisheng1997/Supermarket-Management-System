import DatabaseConnection


def process_purchase(order_list):


# TODO DatabaseConnection.add_new_purchase_record(username, order_id)
# TODO DatabaseConnection.change_the_credit_customer(username, )
# TODO DatabaseConnection.change the_number_of_items_in_warehouse(order_list)


def process_complain(user_id, complain_list):
    comp_type = complain_list[0]
    comp_content = complain_list[1]
    DatabaseConnection.exec_add_new_complain_to_complain_list(user_id, comp_type, comp_content)
