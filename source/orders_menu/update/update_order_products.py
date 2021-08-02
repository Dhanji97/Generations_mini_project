from orders_menu.product_selection import product_selection


def update_order_products(list_products):
    update_products = input('to update products input "Y" or press enter to skip: ')
    if update_products == '':
        return None
    elif update_products != "Y":
        print('Sorry that option was not recognized')
        update_order_products(list_products)
    
    for i, item in enumerate(list_products):
        print(i, item)
    products_selection = product_selection(list_products)
    if products_selection != None:
        return products_selection