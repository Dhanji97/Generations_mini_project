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

Orders_list = [{
                    'Customer name': 'Dhanji',
                    'Customer address': '1, AB1 2CD',
                    'Customer phone number': '07147258369',
                    'Courier': 1,
                    'Status': 'preparing'
                    },
                {
                    'Customer name': 'Abbas',
                    'Customer address': '2, EF3 4GH',
                    'Customer phone number': '07963852741',
                    'Courier': 1,
                    'Status': 'Out for delivery'
                    }]
Order_status_list = ['Preparing', 'Out for delivery']