import main_menu


def products_menu():
    products_menu_input = input('''Please select from the following options:
    0: main menu
    1: products list
    2: New product
    3: Update product
    4: Delete product\n''')
    
    valid_inputs = [str(i) for i in range(5)]
    
    if products_menu_input not in valid_inputs:
        print('Sorry that option was not recognized')
        return products_menu()
    
    products_menu_input = int(products_menu_input)
    
    if products_menu_input == 0:
        main_menu.main_menu()

    elif products_menu_input == 1:
        print(main_menu.products_list)

    elif products_menu_input == 2:
        new_product = input("Please enter new product's name: ")
        main_menu.products_list.append(new_product)
        print(f'Product "{new_product}" successfully added.')
        return products_menu()

    elif products_menu_input == 3:
        for i, product in enumerate(main_menu.products_list):
            print(i, product)
        
        valid_update_inputs = [str(i) for i in range(len(main_menu.products_list))]
        
        update_index = input('select product number to update: ')
        if products_menu_input not in valid_inputs:
            print('Sorry that option was not recognized')
            return products_menu()
        
        update_index = int(update_index)
        
        updated_product_name = input('Please enter new product name: ')
        main_menu.products_list[update_index] = updated_product_name
        print(f'Product updated to "{updated_product_name}".')
        return products_menu()
    
    elif products_menu_input == 4:
        for i, product in enumerate(main_menu.products_list):
            print(i, product)
        
        valid_delete_inputs = [str(i) for i in range(len(main_menu.products_list))]
        
        delete_index = input('select product number to delete: ')
        if products_menu_input not in valid_inputs:
            print('Sorry that option was not recognized')
            return products_menu()
        
        delete_index = int(delete_index)
        delete_item = main_menu.products_list[delete_index]
        main_menu.products_list.pop(delete_index)
        print(f'Product "{delete_item}" was removed from products list.')
        return products_menu()
    else:
        print('Sorry that option was not recognized')
        return products_menu()
