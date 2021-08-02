def update_order_courier(list_courier_dict):
    courier_index = input('select the courier index or press enter to skip: ')
    if courier_index == '':
        return None
    
    valid_inputs = [str(i) for i in range(len(list_courier_dict))]
    if courier_index not in valid_inputs:
        print('Sorry that option was not recognized')
        update_order_courier(list_courier_dict)
    
    return courier_index