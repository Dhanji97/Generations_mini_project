from products_menu import products_menu
from couriers_menu import couriers_menu
from saved_information import information
from orders_menu import Orders_menu
import save_to_csv

def main_menu():
    '''Runs the main menu in the UI'''
    main_menu_input = input('''Please select from the following options:
    0: Exit 
    1: Products Menu
    2: Couriers Menu
    3: Orders Menu\n''')
    
    valid_main_inputs = [str(i) for i in range(4)]
    
    if main_menu_input not in valid_main_inputs:
        print('Sorry that option was not recognized')
        return main_menu()
    
    main_menu_input = int(main_menu_input)
    
    if main_menu_input == 0:
        save_to_csv.save_csv(information.list_of_products_dicts,'/source/saved_information/products.csv', 'Prodcuts saved successfully')
        
        try:
            with open('couriers.txt', 'w') as couriers_file:
                for courier in information.couriers_list:
                    couriers_file.write(courier + '\n')
        except Exception as e:
            print("File 'couriers.txt' could not be opened" + str(e))
        
        print('Thank you for visiting *app*')
        
    elif main_menu_input == 1:
        products_menu.products_menu()
        
    elif main_menu_input == 2:
        couriers_menu.couriers_menu()
        
    elif main_menu_input == 3:
        Orders_menu.Orders_menu()