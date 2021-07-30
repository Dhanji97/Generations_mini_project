from main_menu import main_menu
from saved_information import information
from couriers_menu.new_courier import new_courier
from couriers_menu.update_courier import update_courier


def couriers_menu():
    '''Runs the courier menu in the UI'''
    couriers_menu_input = input('''Please select from the following options:
    0: main menu
    1: couriers list
    2: New courier
    3: Update courier
    4: Delete courier\n''')
    
    valid_courier_inputs = [str(i) for i in range(5)]
    
    if couriers_menu_input not in valid_courier_inputs:
        print('Sorry that option was not recognized')
        couriers_menu()
    
    couriers_menu_input = int(couriers_menu_input)
    
    if couriers_menu_input == 0:
        main_menu.main_menu()

    elif couriers_menu_input == 1:
        print(information.list_of_couriers_dicts)
        couriers_menu()

    elif couriers_menu_input == 2:
        new_courier(information.list_of_couriers_dicts)
        couriers_menu()
    
    elif couriers_menu_input == 3:
        update_courier(information.list_of_couriers_dicts)
        couriers_menu()
    
    elif couriers_menu_input == 4:
        delete_courier()

def delete_courier():
    '''deletes a courier in the couriers list '''
    for i, courier in enumerate(information.couriers_list):
        print(i, courier)
    
    valid_delete_inputs = [str(i) for i in range(len(information.couriers_list))]
    # C added to valid inputs to allow user to cancel selection and return to previous menu
    valid_delete_inputs.append('C')
    delete_index = input('select courier number to delete or C to cancel: ')
    if delete_index not in valid_delete_inputs:
        print('Sorry that option was not recognized')
        return delete_courier()
    elif delete_index == 'C':
        return couriers_menu()
    
    delete_index = int(delete_index)
    delete_item = information.couriers_list[delete_index]
    information.couriers_list.pop(delete_index)
    print(f'courier "{delete_item}" was removed from couriers list.')
    return couriers_menu()