def update_courier(list_dict):
    '''update the name and number of an existing courier'''
    for i, courier in enumerate(list_dict):
        print(i, courier)
    
    courier_index = input('select the courier\'s index to update or C to cancel: ')
    if courier_index == 'C':
        return
    
    valid_inputs = [str(i) for i in range(len(list_dict))]
    if courier_index not in valid_inputs:
        print('Sorry that option was not recognized')
        update_courier(list_dict)
    
    courier_index = int(courier_index)
    print(list_dict[courier_index])
    
    updated_name = input('Please enter the updated courier\'s name or press enter to skip: ')
    if updated_name != '':
        list_dict[courier_index]['name'] = updated_name
        print(f'courier\'s name changed to {updated_name}')
    
    updated_number = input('Please enter the courier\'s updated number or press enter to skip: ')
    if updated_number != '':
        list_dict[courier_index]['number'] = updated_number
        print(f'courier\'s number changed to {updated_number}')
    return