import json
from notify import *
from aquisition import *

def check_new_seats(old, new):
    return list(set(old) - set(new))


def get_seats(old_seats):
    # Open json file
    with open('data/train.json') as f:
        data = json.load(f)
        seats = data['nhits']

    
    date = get_config('RESEARCH', 'DATE')
    trajet = get_config('RESEARCH', 'FROM') + "-->" + get_config('RESEARCH', 'TO')

    # set headr with number of seats availables
    seats_available = "Places TGVMAX disponibles : {}\n 📅 Date: {}\n 📍 Trajet: {}".format(seats, date, trajet)

    train_list = []

    for train in data['records']:

        # Get value from json keys
        train_id = train['fields']['train_no']
        time = train['fields']['heure_depart']
        
        train_list.append(time)

        # Setup the output email_file
        messanger_train_data = "Depart : {}\n Numero de train : {}\n".format(
            time, train_id)

    if old_seats != seats:
        # TODO -> new_seats = check_new_seats(old, new)
        send_alert(""+seats_available+ "\n 🕑 "+ str(train_list) +"")
    

    return seats
