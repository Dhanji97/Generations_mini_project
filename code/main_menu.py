import products_menu
import couriers_menu
import information

def main_menu():
    '''Runs the main menu in the UI'''
    main_menu_input = input('''Please select from the following options:
    0: Exit 
    1: Products Menu
    2: Couriers Menu\n''')
    
    valid_main_inputs = [str(i) for i in range(3)]
    
    if main_menu_input not in valid_main_inputs:
        print('Sorry that option was not recognized')
        return main_menu()
    
    main_menu_input = int(main_menu_input)
    
    if main_menu_input == 0:
        try:
            with open('mini_project_app/products.txt', 'w') as products_file:
                for product in information.products_list:
                    products_file.write(product + '\n')
        except Exception as e:
            print("File 'products.txt' could not be opened" + str(e))
        
        try:
            with open('mini_project_app/couriers.txt', 'w') as couriers_file:
                for courier in information.couriers_list:
                    couriers_file.write(courier + '\n')
        except Exception as e:
            print("File 'couriers.txt' could not be opened" + str(e))
        
        print('Thank you for visiting *app*')
        
    elif main_menu_input == 1:
        products_menu.products_menu()
        
    elif main_menu_input == 2:
        couriers_menu.couriers_menu()