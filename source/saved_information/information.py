import csv

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
                    'Status': 'out for delivery'
                    }]
order_status_list = ['preparing', 'out for delivery']

try:
    with open('source/saved_information/products.csv', 'r') as products_csv:
        list_of_products_dicts = []
        reader = csv.DictReader(products_csv, delimiter=',')
        for row in reader:
            list_of_products_dicts.append(row)
except Exception as e:
    print(e)

try:
    with open('source/saved_information/couriers.csv', 'r') as couriers_csv:
        list_of_couriers_dicts = []
        reader = csv.DictReader(couriers_csv, delimiter=',')
        for row in reader:
            list_of_couriers_dicts.append(row)
except Exception as e:
    print(e)

try:
    with open('source/saved_information/orders.csv', 'r') as orders_csv:
        list_of_orders_dicts = []
        reader = csv.DictReader(orders_csv, delimiter=',')
        for row in reader:
            list_of_orders_dicts.append(row)
except Exception as e:
    print(e)