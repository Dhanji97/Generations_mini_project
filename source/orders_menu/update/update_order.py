from orders_menu.update.update_order_products import update_order_products
from orders_menu.update.update_order_status import update_order_status
from orders_menu.update.update_order_courier import update_order_courier


def update_order(list_orders, list_products, list_couriers, status_list):
    for i, order in enumerate(list_orders):
        print(i, order)
    
    order_index = input('Please select which order to update or C to cancel: ')
    if order_index == 'C':
        return 
    
    valid_order_inputs = [str(i) for i in range(len(list_orders))]
    
    if order_index not in valid_order_inputs:
        print('Sorry that option was not recognized')
        return update_order(list_orders, list_products, list_couriers, status_list)
    
    order_index = int(order_index)
    order_updated = list_orders[order_index]
    
    name = input("Please enter customer\'s name or enter to skip: ")
    if name != "":
        order_updated['customer name'] = name
    address  = input("Please enter customer\'s address or enter to skip: ")
    if address != "":
        order_updated['customer address'] = address
    number  = input("Please enter customer\'s number or enter to skip: ")
    if number != "":
        order_updated['customer number'] = number
    
    for i, courier in enumerate(list_couriers):
        print(i, courier)
    courier = update_order_courier(list_couriers)
    if courier != None:
        order_updated['courier'] = courier
    
    for i, status in enumerate(status_list):
        print(i, status)
    status_index  = update_order_status(status_list)
    if status_index != None:
        order_updated['status'] = status_list[status_index]
    
    print(f'current product selection: {order_updated["products"]}')
    products = update_order_products(list_products)
    if products != None:
        order_updated['products'] = products
    
    print(f'order updated to {order_updated}')
    return