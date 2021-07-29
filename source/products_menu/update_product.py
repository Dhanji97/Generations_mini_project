def update_product(list_dict):
    '''update the name and price of an existing product'''
    for i, product in enumerate(list_dict):
        print(i, product)
    
    product_index = input('select product number to update or C to cancel: ')
    if product_index == 'C':
        return
    
    valid_inputs = [str(i) for i in range(len(list_dict))]
    if product_index not in valid_inputs:
        print('Sorry that option was not recognized')
        return update_product(list_dict)
    
    product_index = int(product_index)
    print(list_dict[product_index])
    
    updated_name = input('Please enter updated product name or press enter to skip:' )
    if updated_name != '':
        list_dict[product_index]['name'] = updated_name
    
    updated_price = input('Please enter updated product price or press enter to skip: £')
    if updated_price != '':
        list_dict[product_index]['price'] = '£' + updated_price
    return