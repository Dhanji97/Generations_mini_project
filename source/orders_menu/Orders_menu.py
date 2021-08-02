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
        update_order()
    
    elif orders_menu_input == 5:
        delete_order()

def update_order():
    '''updates the entires of an existing order in the order list'''
    for i, order in enumerate(information.orders_list):
        print(i, order)
    
    valid_update_inputs = [str(i) for i in range(len(information.orders_list))]
    # C added to valid inputs to allow user to cancel selection and return to previous menu
    valid_update_inputs.append('C')
    update_index = input('select order number to update or C to cancel: ')
    if update_index not in valid_update_inputs:
        print('Sorry that option was not recognized\n')
        return update_order()
    elif update_index == 'C':
        return orders_menu()
    
    update_index = int(update_index)
    order_dict_to_update = information.orders_list[update_index]
    print(order_dict_to_update)
    
    update_customer_name = input('Update customer name, press enter to skip:\n')
    if update_customer_name == '':
        pass
    else:
        order_dict_to_update['Customer name'] = update_customer_name
    
    update_customer_house_number = input('Update customer house number, press enter to skip:\n')
    update_customer_postcode = input('Update customer postcode, press enter to skip:\n')
    original_address = order_dict_to_update['Customer address'].split(', ')
    if update_customer_house_number == '':
        update_customer_house_number = original_address[0]
    if update_customer_postcode == '':
        update_customer_postcode = original_address[1]
    updated_address = update_customer_house_number + ', ' + update_customer_postcode
    order_dict_to_update['Customer address'] = updated_address
    
    update_customer_phone_number = input('Update customer phone number, press enter to skip:\n')
    if update_customer_phone_number == '':
        pass
    else:
        order_dict_to_update['Customer phone number'] = update_customer_phone_number
    
    current_courier = order_dict_to_update['Courier']
    updated_courier = update_order_courier_option(current_courier)
    order_dict_to_update['Courier'] = updated_courier
    
    current_status = order_dict_to_update['Status']
    updated_status = update_order_status_option(current_status)
    order_dict_to_update['Status'] = updated_status
    print(f'order updated too:\n {order_dict_to_update}\n')
    return orders_menu()

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