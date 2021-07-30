def delete_courier(list_dict):
    for i, courier in enumerate(list_dict):
        print(i, courier)
    
    delete_index = input('select courier\'s index to delete or C to cancel: ')
    if delete_index == 'C':
        return
    
    valid_inputs = [str(i) for i in range(len(list_dict))]
    if delete_index not in valid_inputs:
        print('Sorry that option was not recognized')
        delete_courier(list_dict)
    
    delete_index = int(delete_index)
    deleted_courier = list_dict[delete_index]
    list_dict.pop(delete_index)
    print(f'courier {deleted_courier["name"]} was deleted.')
    return