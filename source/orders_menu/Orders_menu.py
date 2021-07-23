from main_menu import main_menu
from saved_information import information

def Orders_menu():
    '''Runs the Order menu in the UI'''
    Orders_menu_input = input('''Please select from the following options:
    0: main menu
    1: Orders list
    2: New Order
    3: Update order status
    4: Update Order
    5: Delete Order\n''')
    
    valid_Order_inputs = [str(i) for i in range(6)]
    
    if Orders_menu_input not in valid_Order_inputs:
        print('Sorry that option was not recognized\n')
        return Orders_menu()
    
    Orders_menu_input = int(Orders_menu_input)
    
    if Orders_menu_input == 0:
        main_menu.main_menu()

    elif Orders_menu_input == 1:
        print(information.Orders_list)
        Orders_menu()

    elif Orders_menu_input == 2:
        new_Order()
    
    elif Orders_menu_input == 3:
        update_Order_status()
    
    elif Orders_menu_input == 4:
        update_Order()
    
    elif Orders_menu_input == 5:
        delete_Order()

def new_Order():
    '''Adds a new Order to the list of Orders'''
    customer_name = input("Please enter your name or C to cancel: ")
    customer_house_num = input("Please enter your house number or C to cancel: ")
    customer_postcode = input("Please enter your postcode or C to cancel: ")
    customer_address = customer_house_num + ', ' + customer_postcode
    customer_phone_num = input("Please enter your contact number or C to cancel: ")
    if customer_name == 'C' or customer_house_num == 'C' or customer_postcode == 'C' or customer_phone_num == 'C':
        return Orders_menu()
    else:
        for i, courier in enumerate(information.couriers_list):
            print(i, courier)
            
    valid_courier_inputs = [str(i) for i in range(len(information.couriers_list))]
    # C added to valid inputs to allow user to cancel selection and return to previous menu
    valid_courier_inputs.append('C')
    
    courier_index = input('Please select a courier with its indicated number or C to cancel: ')
    
    if courier_index not in valid_courier_inputs:
        print('Sorry that option was not recognized')
        return new_Order()
    elif courier_index == 'C':
        return Orders_menu()
    
    courier_index = int(courier_index)
    
    order_dict =    {
                    'Customer name': customer_name,
                    'Customer address': customer_address,
                    'Customer phone number': customer_phone_num,
                    'Courier': courier_index,
                    'Status': 'preparing'
                    }
    
    information.Orders_list.append(order_dict)
    print(f'Order successfully added.\n')
    return Orders_menu()

def update_Order_status():
    '''Updates the status of an order in the order's list'''
    for i, order in enumerate(information.Orders_list):
        print(i, order)
        
    valid_Order_inputs = [str(i) for i in range(len(information.Orders_list))]
    # C added to valid inputs to allow user to cancel selection and return to previous menu
    valid_Order_inputs.append('C')
    
    Order_index = input('Please select which order\'s status to update or C to cancel: ')
    if Order_index not in valid_Order_inputs:
        print('Sorry that option was not recognized')
        return update_Order_status()
    elif Order_index == 'C':
        return Orders_menu()
    Order_index = int(Order_index)
    order_dict_update = information.Orders_list[Order_index]
    
    for i, status in enumerate(information.Order_status_list):
        print(i, status)

    valid_status_inputs = [str(i) for i in range(len(information.Order_status_list))]
    # C added to valid inputs to allow user to cancel selection and return to previous menu
    valid_status_inputs.append('C')
    
    status_index = input('Please select a status to update the order\'s status too or C to cancel: ')
    if status_index not in valid_status_inputs:
        print('Sorry that option was not recognized')
        return update_Order_status()
    elif status_index == 'C':
        return Orders_menu()
    status_index = int(status_index)
    updated_status = information.Order_status_list[status_index]
    order_dict_update['status'] = updated_status
    print(f'Order\'s status successfully updated to {updated_status}')
    return Orders_menu()

def update_Order():
    '''updates the entires of an existing Order in the Order list'''
    for i, Order in enumerate(information.Orders_list):
        print(i, Order)
    
    valid_update_inputs = [str(i) for i in range(len(information.Orders_list))]
    # C added to valid inputs to allow user to cancel selection and return to previous menu
    valid_update_inputs.append('C')
    update_index = input('select Order number to update or C to cancel: ')
    if update_index not in valid_update_inputs:
        print('Sorry that option was not recognized\n')
        return update_Order()
    elif update_index == 'C':
        return Orders_menu()
    
    update_index = int(update_index)
    Order_dict_to_update = information.Orders_list[update_index]
    print(Order_dict_to_update)
    
    update_customer_name = input('Update customer name, press enter to skip:\n')
    if update_customer_name == '':
        pass
    else:
        Order_dict_to_update['Customer name'] = update_customer_name
    
    update_customer_house_number = input('Update customer house number, press enter to skip:\n')
    update_customer_postcode = input('Update customer postcode, press enter to skip:\n')
    original_address = Order_dict_to_update['Customer address'].split(', ')
    if update_customer_house_number == '':
        update_customer_house_number = original_address[0]
    if update_customer_postcode == '':
        update_customer_postcode = original_address[1]
    updated_address = update_customer_house_number + ', ' + update_customer_postcode
    Order_dict_to_update['Customer address'] = updated_address
    
    update_customer_phone_number = input('Update customer phone number, press enter to skip:\n')
    if update_customer_phone_number == '':
        pass
    else:
        Order_dict_to_update['Customer phone number'] = update_customer_phone_number
    
    current_courier = Order_dict_to_update['Courier']
    updated_courier = update_order_courier_option(current_courier)
    Order_dict_to_update['Courier'] = updated_courier
    
    current_status = Order_dict_to_update['Status']
    updated_status = update_order_status_option(current_status)
    Order_dict_to_update['Status'] = updated_status
    print(f'Order updated too:\n {Order_dict_to_update}\n')
    return Orders_menu()

def delete_Order():
    '''deletes an Order in the Orders list'''
    for i, Order in enumerate(information.Orders_list):
        print(i, Order)
    
    valid_delete_inputs = [str(i) for i in range(len(information.Orders_list))]
    # C added to valid inputs to allow user to cancel selection and return to previous menu
    valid_delete_inputs.append('C') 
    delete_index = input('select Order number to delete or C to cancel: ')
    if delete_index not in valid_delete_inputs:
        print('Sorry that option was not recognized')
        return delete_Order()
    elif delete_index == 'C':
        return Orders_menu()
    
    delete_index = int(delete_index)
    delete_item = information.Orders_list[delete_index]
    information.Orders_list.pop(delete_index)
    print('The order was removed from orders list.')
    return Orders_menu()

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
    for i, status in enumerate(information.Order_status_list):
        print(i, status)
    
    valid_status_inputs = [str(i) for i in range(len(information.Order_status_list))]
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
        return information.Order_status_list[status_index]