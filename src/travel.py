import json 
import telegram
import requests

class Travel:
    
    def __init__(self, date, departure, arrival, travel):
        self.url = ""
        self.date = date
        self.travel_config = travel
        self.travel_json = ""
        self.departure = departure
        self.arrival = arrival
        self.seats = 1
        self.list_departures = []
        self.p = 0

    def set_url(self):
        self.date.replace("/", "%2F")

        url = "https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&lang=FR&rows=1000&facet=date&facet=origine&facet=destination&facet=od_happy_card&refine.origine={}+(intramuros)&refine.destination={}+(gares+intramuros)&refine.date={}&refine.od_happy_card=OUI&timezone=Europe%2FParis".format(
        self.departure, self.arrival, self.date)

        self.url = url
    
    def set_seat(self, new_seats):
        self.seats = new_seats

    def set_travel(self,travel):
        self.travel = travel

    def read_data(self, i, isFistTimeInLoop):
        with open('data/travel{}.json'.format(i)) as f:
            data = json.load(f)
        
        new_seats = data['nhits']

        if new_seats != 0:

            start = data['records'][0]['fields']['origine']
            end = data['records'][0]['fields']['destination']

            self.set_travel("{} --> {}".format(start, end))
            seats_available = "Places TGVMAX disponibles : {}\n 📅 Date: {}\n 📍 Trajet: {}".format(new_seats, self.date, self.travel_json)

            train_list = []

            for train in data['records']:

                train_id = train['fields']['train_no']
                time = train['fields']['heure_depart']
        
                train_list.append(time)

                messanger_train_data = "Depart : {}\n Numero de train : {}\n".format(
                    time, train_id)

            if self.seats != new_seats:
                self.set_seat(new_seats)
                seats_available = "Places TGVMAX disponibles : {}\n 📅 Date: {}\n 📍 Trajet: {}".format(self.seats, self.date, self.travel_json)
                self.send_alert(""+seats_available+ "\n 🕑 "+ str(train_list) +"")

        else:
            if isFistTimeInLoop == True:
                no_train_data = "Dsl, Auncun train pour le moment pour :\n📅 Date: {}\n 📍 Trajet: {} \n Nous vous informerons des qu'une place est disponible !".format(self.date, self.travel_config)
                self.send_alert(no_train_data)

            if self.seats > new_seats:
                no_train_data = "Oupsss... places ne sont plus disponible pour :\n📅 Date: {}\n 📍 Trajet: {} \n Nous vous informerons des qu'une place est disponible !".format(self.date, self.travel_config)
                self.send_alert(no_train_data)



        self.seats = new_seats
        self.p+=1
        print(self.p,self.seats, new_seats)
       
    def send_alert(self, message):
        with open('data/keys.json', 'r') as keys_file:
            k = json.load(keys_file)
            token = k['telegram_token']
            chat_id = k['telegram_chat_id']
        bot = telegram.Bot(token=token)
        bot.sendMessage(chat_id=chat_id, text=message)

    def get_data(self, i):
        request = requests.get(self.url).text
        json_data = json.loads(request)

        with open('data/travel{}.json'.format(i), 'w') as f:
            json.dump(json_data, f)

        if json_data is None:
            print("Update failed !")
            return False
        else:
            print("Update completed !")
            return True
