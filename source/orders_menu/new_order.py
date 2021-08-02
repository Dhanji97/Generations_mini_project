

from orders_menu.select_courier import select_courier
from orders_menu.product_selection import product_selection


def new_order(list_orders_dict, list_products_dict,list_courier_dict):
    name = input("Please enter customer\'s name or C to cancel: ")
    if name == "C":
        return
    address  = input("Please enter customer\'s address or C to cancel: ")
    if address == "C":
        return
    number  = input("Please enter customer\'s number or C to cancel: ")
    if number == "C":
        return
    for i, courier in enumerate(list_courier_dict):
        print(i, courier)
    courier = select_courier(list_courier_dict)
    if courier == None:
        return
    for i, item in enumerate(list_products_dict):
        print(i, item)
    products = product_selection(list_products_dict)
    if products == None:
        return
    
    new_order_dict = {}
    new_order_dict['customer name'] = name
    new_order_dict['customer address'] = address
    new_order_dict['customer number'] = number
    new_order_dict['courier'] = courier
    new_order_dict['status'] = 'preparing'
    new_order_dict['products'] = products
    list_orders_dict.append(new_order_dict)
    print(f'{new_order_dict} added to list of orders')
    return
