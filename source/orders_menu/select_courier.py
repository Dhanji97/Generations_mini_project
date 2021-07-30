def select_courier(list_courier_dict):
    courier_index = input('select the courier index or C to cancel: ')
    if courier_index == 'C':
        return None
    
    valid_inputs = [str(i) for i in range(len(list_courier_dict))]
    if courier_index not in valid_inputs:
        print('Sorry that option was not recognized')
        select_courier(list_courier_dict)
    
    return courier_index