import json
from notify import *

def check_new_seats(old, new):
    return list(set(old) - set(new))


def get_seats(old_seats):
    # Open json file
    with open('../data/train.json') as f:
        data = json.load(f)
        seats = data['nhits']

    # set headr with number of seats availables
    seats_available = "Places TGVMAX disponibles : {}\n".format(seats)

    train_list = []

    for train in data['records']:

        # Get value from json keys
        train_id = train['fields']['train_no']
        time = train['fields']['heure_depart']
        
        train_list.append(time)

        # Setup the output email_file
        messanger_train_data = "Depart : {}\n Numero de train : {}\n".format(
            time, train_id)
        

    if old_seats < seats:
        send_alert(seats_available)
        send_alert(str(train_list))

    return seats
