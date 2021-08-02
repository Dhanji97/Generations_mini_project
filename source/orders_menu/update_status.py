def update_status(list_orders, status_list):
    for i, order in enumerate(list_orders):
        print(i, order)
    
    order_index = input('Please select which order\'s status to update or C to cancel: ')
    if order_index == 'C':
        return
    
    valid_order_inputs = [str(i) for i in range(len(list_orders))]
    
    if order_index not in valid_order_inputs:
        print('Sorry that option was not recognized')
        return
    
    order_index = int(order_index)
    order_dict_update = list_orders[order_index]
    
    for i, status in enumerate(status_list):
        print(i, status)
    
    status_index = input('Please select a status to update the order\'s status to or C to cancel: ')
    if status_index == 'C':
        return
    
    valid_status_inputs = [str(i) for i in range(len(status_list))]
    if status_index not in valid_status_inputs:
        print('Sorry that option was not recognized')
        update_status(list_orders, status_list)
    
    status_index = int(status_index)
    updated_status = status_list[status_index]
    order_dict_update['status'] = updated_status
    print(f'order\'s status successfully updated to {updated_status}')
    return