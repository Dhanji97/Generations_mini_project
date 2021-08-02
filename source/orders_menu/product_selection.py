def product_selection(list_product_dict):
    selection = None
    list_products_index = []
    valid_inputs = [str(i) for i in range(len(list_product_dict))]
    while selection != '':
        selection = input('Please select product index to add to order. press enter to confirm or C to cancel: ')
        if selection == 'C':
            list_products_index = None
            break
        if selection == '':
            break
        elif selection not in valid_inputs:
            print('Sorry that option was not recognized\n')
            continue
        else:
            index = int(selection)
            list_products_index.append(index)
    
    return list_products_index