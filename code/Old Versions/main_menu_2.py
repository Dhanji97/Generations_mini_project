import products_menu
import couriers_menu

products_file = None
try:
    products_file = open('mini_project_app/products.txt', 'r')
    products_list = [product.strip() for product in products_file.readlines()]
except Exception as e:
    print("File 'products.txt' could not be opened" + str(e))
finally:
    products_file.close()

couriers_file = None
try:
    couriers_file = open('mini_project_app/couriers.txt', 'r')
    couriers_list = [courier.strip() for courier in couriers_file.readlines()]
except Exception as e:
    print("File 'couriers.txt' could not be opened" + str(e))
finally:
    couriers_file.close()

def main_menu():
    main_menu_input = input('''Please select from the following options:
    0: Exit 
    1: Products Menu
    2: Couriers Menu\n''')
    
    valid_main_inputs = [str(i) for i in range(3)]
    
    if main_menu_input not in valid_main_inputs:
        print('Sorry that option was not recognized')
        return None
    
    main_menu_input = int(main_menu_input)
    
    if main_menu_input == 0:
        try:
            products_file = open('mini_project_app/products.txt', 'w')
            for product in products_list:
                products_file.write(product + '\n')
        except Exception as e:
            print("File 'products.txt' could not be opened" + str(e))
        finally:
            products_file.close()
        
        try:
            couriers_file = open('mini_project_app/couriers.txt', 'w')
            for courier in couriers_list:
                couriers_file.write(courier + '\n')
        except Exception as e:
            print("File 'couriers.txt' could not be opened" + str(e))
        finally:
            couriers_file.close()
        
        print('Thank you for visiting *app*')
        
    elif main_menu_input == 1:
        products_menu.products_menu()
        
    elif main_menu_input == 2:
        couriers_menu.couriers_menu()
