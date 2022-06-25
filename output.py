import json
from notify import *

def search(list, train_no):
    for i in range(len(list)):
        if list[i] == train_no:
            return True
    return False

def set_output_file(old_train_list):
    # Open json file
    with open('./data/train.json') as f:
        data = json.load(f)
        seats = data['nhits']

    # set headr with number of seats availables
    messanger_title = "Places TGVMAX disponibles : {}\n".format(seats)
    messanger_file = open("./output/messanger.txt", 'w+')
    messanger_file.write(messanger_title)

    list_train = []

    for train in data['records']:

        # Get value from json keys
        train_no = train['fields']['train_no']
        train_departure = train['fields']['heure_depart']
        start = train['fields']['origine']
        to = train['fields']['destination']

        list_train.append(train_no)

        # Setup the output email_file
        messanger_train_data = "Depart : {}\n Numero de train : {}\n".format(
            train_departure, train_no)
        if train_no not in messanger_file.read():
            messanger_file.write(messanger_train_data)
            if search(old_train_list, train_no):
                pass
            else:
                send_alert(messanger_train_data)

 
    messanger_file.close()
    return list_train
