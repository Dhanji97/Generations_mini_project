from main_menu import main_menu
from saved_information import information
from products_menu.new_product import create_new_product
from products_menu.update_product import update_product

def products_menu():
    '''Runs the product menu in the UI'''
    products_menu_input = input('''Please select from the following options:
    0: main menu
    1: products list
    2: New product
    3: Update product
    4: Delete product\n''')
    
    valid_product_inputs = [str(i) for i in range(5)]
    
    if products_menu_input not in valid_product_inputs:
        print('Sorry that option was not recognized\n')
        return products_menu()
    
    products_menu_input = int(products_menu_input)
    
    if products_menu_input == 0:
        main_menu.main_menu()

    elif products_menu_input == 1:
        print(information.list_of_products_dicts)
        products_menu()

    elif products_menu_input == 2:
        create_new_product(information.list_of_products_dicts)
        products_menu()
    
    elif products_menu_input == 3:
        update_product()
    
    elif products_menu_input == 4:
        delete_product()


def delete_product():
    '''deletes a product in the products list'''
    for i, product in enumerate(information.products_list):
        print(i, product)
    
    valid_delete_inputs = [str(i) for i in range(len(information.products_list))]
    # C added to valid inputs to allow user to cancel selection and return to previous menu
    valid_delete_inputs.append('C') 
    delete_index = input('select product number to delete or C to cancel: ')
    if delete_index not in valid_delete_inputs:
        print('Sorry that option was not recognized')
        return delete_product()
    elif delete_index == 'C':
        return products_menu()
    
    delete_index = int(delete_index)
    delete_item = information.products_list[delete_index]
    information.products_list.pop(delete_index)
    print(f'Product "{delete_item}" was removed from products list.')
    return products_menu()