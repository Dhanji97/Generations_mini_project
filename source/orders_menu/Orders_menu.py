from orders_menu.update_order import update_order
from orders_menu.update_status import update_status
from main_menu import main_menu
from saved_information import information
from orders_menu.new_order import new_order

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
        delete_order()

def delete_order():
    '''deletes an order in the orders list'''
    for i, order in enumerate(information.orders_list):
        print(i, order)
    
    valid_delete_inputs = [str(i) for i in range(len(information.orders_list))]
    # C added to valid inputs to allow user to cancel selection and return to previous menu
    valid_delete_inputs.append('C') 
    delete_index = input('select order number to delete or C to cancel: ')
    if delete_index not in valid_delete_inputs:
        print('Sorry that option was not recognized')
        return delete_order()
    elif delete_index == 'C':
        return orders_menu()
    
    delete_index = int(delete_index)
    delete_item = information.orders_list[delete_index]
    information.orders_list.pop(delete_index)
    print('The order was removed from orders list.')
    return orders_menu()

def update_order_courier_option(current_courier_option):
    for i, courier in enumerate(information.couriers_list):
        print(i, courier)
    
    valid_courier_inputs = [str(i) for i in range(len(information.couriers_list))]
    # 'blank' added to valid inputs to allow user to skip selection and continue updating order
    valid_courier_inputs.append('')
    
    courier_index = input('Please select a courier with its indicated number or press enter to skip: ')
    
    if courier_index not in valid_courier_inputs:
        print('Sorry that option was not recognized')
        return update_order_courier_option(current_courier_option)
    elif courier_index == '':
        return current_courier_option
    else:
        return int(courier_index)

def update_order_status_option(current_status_option):
    for i, status in enumerate(information.order_status_list):
        print(i, status)
    
    valid_status_inputs = [str(i) for i in range(len(information.order_status_list))]
    # 'blank' added to valid inputs to allow user to skip selection and continue updating order
    valid_status_inputs.append('')
    
    status_index = input('Please select a status with its indicated number or press enter to skip: ')
    
    if status_index not in valid_status_inputs:
        print('Sorry that option was not recognized')
        return update_order_status_option(current_status_option)
    elif status_index == '':
        return current_status_option
    else:
        status_index = int(status_index)
        return information.order_status_list[status_index]