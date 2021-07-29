import csv

def save_csv(list_of_dict, file_name, print_message):
    '''saves a list of dictionaries to a csv file'''
    field_names = list_of_dict[0].keys()
    try:
        with open(file_name,'w', newline="") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            writer.writerows(list_of_dict)
            print(print_message)
    except Exception as e:
        print(e)