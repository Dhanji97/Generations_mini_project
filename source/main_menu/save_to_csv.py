import csv

random_list_dict = [{
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

random_list_dict_2 = [{'name': 'Dave', 'number': '07123456789'}, {'name': 'Bob', 'number': '07987654321'}]

def save_products(list_of_dict):
    field_names = list_of_dict[0].keys()
    try:
        with open('source/saved_information/products.csv','w', newline="") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            writer.writerows(list_of_dict)
            print('Prodcts saved successfully')
    except Exception as e:
        print(e)

def save_couriers(list_of_dict):
    field_names = ['name', 'number']
    try:
        with open('source/saved_information/couriers.csv','w', newline="") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            writer.writerows(list_of_dict)
            print('Couriers saved successfully')
    except Exception as e:
        print(e)

def save_orders(list_of_dict):
    field_names = list_of_dict[0].keys()
    try:
        with open('source/saved_information/orders.csv','w', newline="") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            writer.writerows(list_of_dict)
            print('Orders saved successfully')
    except Exception as e:
        print(e)
save_couriers(random_list_dict_2)
# save_orders(random_list_dict)