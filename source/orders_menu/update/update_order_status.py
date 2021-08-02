def update_order_status(status_list):
    status_index = input('Please select a status to update to or enter to skip: ')
    if status_index == '':
        return None
    
    valid_status_inputs = [str(i) for i in range(len(status_list))]
    if status_index not in valid_status_inputs:
        print('Sorry that option was not recognized')
        update_order_status(status_list)
    else:
        return int(status_index)