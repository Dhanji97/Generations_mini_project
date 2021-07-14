products_list = ['Coke zero', 'Coffee', 'Tea', 'Hot Chocolate']

def products_menu():
    products_menu_input = input('''Please select from the following options:
    0: main menu
    1: products list
    2: New product
    3: Update product
    4: Delete product\n''')
    
    products_menu_input = int(products_menu_input)
    
    if products_menu_input == 0:
        main_menu()
    elif products_menu_input == 1:
        print(products_list)
    elif products_menu_input == 2:
        new_product = input("Please enter new product's name: ")
        products_list.append(new_product)
        print(f'Product "{new_product}" successfully added.')
        # Want to add a print statement of the new list, then rerun product menu
    elif products_menu_input == 3:
        for i, product in enumerate(products_list):
            print(i, product)
        update_index = int(input('select product number to update: '))
        updated_product_name = input('Please enter new product name: ')
        products_list[update_index] = updated_product_name
        print(f'Product updated to "{updated_product_name}".')
    elif products_menu_input == 4:
        for i, product in enumerate(products_list):
            print(i, product)
        delete_index = int(input('select produnt number to delete: '))
        delete_item = products_list[delete_index]
        products_list.pop(delete_index)
        print(f'Product "{delete_item}" was removed.')
    else:
        print('Sorry that option was not recognized')
        products_menu()



#main menu
def main_menu():
    main_menu_input = int(input('''Please select from the following options:
    0: Exit 
    1: Menu\n'''))   

    if main_menu_input == 0:
        print('Thank you for visiting *app*')
    elif main_menu_input == 1:
        products_menu()
    else:
        print('Sorry that option was not recognized')
        main_menu()

main_menu()
