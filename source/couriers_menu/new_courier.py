def new_courier(list_dict):
    courier_name = input("Please enter the new courier's name or C to cancel: ")
    if courier_name == "C":
        return
    courier_number = input("Please enter the new courier's number or C to cancel: ")
    if courier_number == "C":
        return
    
    new_courier_dict = {}
    new_courier_dict['name'] = courier_name
    new_courier_dict['number'] = courier_number
    list_dict.append(new_courier_dict)
    print(f'{new_courier_dict} added to list of couriers')
    return