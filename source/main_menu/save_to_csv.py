import csv

def save_products(list_of_dict, file_name):
    field_names = list_of_dict[0].keys()
    try:
        with open(file_name,'w', newline="") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            writer.writerows(list_of_dict)
            print('Prodcts saved successfully')
    except Exception as e:
        print(e)

def save_couriers(list_of_dict, file_name):
    field_names = list_of_dict[0].keys()
    try:
        with open(file_name,'w', newline="") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            writer.writerows(list_of_dict)
            print('Couriers saved successfully')
    except Exception as e:
        print(e)

def save_orders(list_of_dict, file_name):
    field_names = list_of_dict[0].keys()
    try:
        with open(file_name,'w', newline="") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            writer.writerows(list_of_dict)
            print('Orders saved successfully')
    except Exception as e:
        print(e)
