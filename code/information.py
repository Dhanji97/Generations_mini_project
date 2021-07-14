try:
    with open('mini_project_app/products.txt', 'r') as products_file:      
        products_list = [product.strip() for product in products_file.readlines()]
except Exception as e:
    print("File 'products.txt' could not be opened" + str(e))

try:
    with open('mini_project_app/couriers.txt', 'r') as couriers_file:
        couriers_list = [courier.strip() for courier in couriers_file.readlines()]
except Exception as e:
    print("File 'couriers.txt' could not be opened" + str(e))