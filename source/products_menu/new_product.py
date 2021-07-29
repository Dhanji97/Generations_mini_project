
def create_new_product(list_dict):
    product_name = input("Please enter new product's name or C to cancel: ")
    if product_name == "C":
        return
    product_price = input("Please enter prodcut's price or C to cancel: ")
    if product_price == "C":
        return
    
    new_product_dict = {}
    new_product_dict['name'] = product_name
    new_product_dict['price'] = product_price
    list_dict.append(new_product_dict)
    return

