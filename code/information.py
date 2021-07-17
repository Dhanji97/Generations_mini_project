try:
    with open('products.txt', 'r') as products_file:      
        products_list = [product.strip() for product in products_file.readlines()]
except Exception as e:
    print("File 'products.txt' could not be opened\n" + str(e))

try:
    with open('couriers.txt', 'r') as couriers_file:
        couriers_list = [courier.strip() for courier in couriers_file.readlines()]
except Exception as e:
    print("File 'couriers.txt' could not be opened\n" + str(e))

Orders_list = []
Order_status_list = ['Preparing', 'Out for divlivery']