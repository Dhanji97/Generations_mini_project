from main_menu import main_menu
from saved_information import information
from orders_menu.new_order import new_order
from orders_menu.update_status import update_status
from orders_menu.update.update_order import update_order
from orders_menu.delete_order import delete_order

def orders_menu():
    '''Runs the order menu in the UI'''
    orders_menu_input = input('''Please select from the following options:
    0: main menu
    1: Orders list
    2: New order
    3: Update order status
    4: Update order
    5: Delete order\n''')
    
    valid_order_inputs = [str(i) for i in range(6)]
    
    if orders_menu_input not in valid_order_inputs:
        print('Sorry that option was not recognized\n')
        return orders_menu()
    
    orders_menu_input = int(orders_menu_input)
    
    if orders_menu_input == 0:
        main_menu.main_menu()

    elif orders_menu_input == 1:
        print(information.list_of_orders_dicts)
        orders_menu()

    elif orders_menu_input == 2:
        new_order(information.list_of_orders_dicts, information.list_of_products_dicts, information.list_of_couriers_dicts)
        orders_menu()
    
    elif orders_menu_input == 3:
        update_status(information.list_of_orders_dicts, information.order_status_list)
        orders_menu()
    
    elif orders_menu_input == 4:
        update_order(information.list_of_orders_dicts, information.list_of_products_dicts, information.list_of_couriers_dicts, information.order_status_list)
        orders_menu()
        
    elif orders_menu_input == 5:
        delete_order(information.list_of_orders_dicts)
        orders_menu()
