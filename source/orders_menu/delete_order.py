def delete_order(list_orders):
    '''deletes an order in the orders list'''
    for i, order in enumerate(list_orders):
        print(i, order)
    
    delete_index = input('select order number to delete or C to cancel: ')
    
    if delete_index == 'C':
        return
    
    valid_delete_inputs = [str(i) for i in range(len(list_orders))]
    if delete_index not in valid_delete_inputs:
        print('Sorry that option was not recognized')
        return delete_order(list_orders)
    
    delete_index = int(delete_index)
    list_orders.pop(delete_index)
    print('The order was removed from orders list.')
    return