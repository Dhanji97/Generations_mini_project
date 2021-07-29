def delete_product(list_dict):
    for i, product in enumerate(list_dict):
        print(i, product)
    
    delete_index = input('select product number to delete or C to cancel: ')
    if delete_index == 'C':
        return
    
    valid_inputs = [str(i) for i in range(len(list_dict))]
    if delete_index not in valid_inputs:
        print('Sorry that option was not recognized')
        return delete_product(list_dict)
    
    delete_index = int(delete_index)
    deleted_product = list_dict[delete_index]
    list_dict.pop(delete_index)
    print(f'product {deleted_product["name"]} was deleted.')
    return
