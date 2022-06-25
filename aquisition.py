import json
import requests
from configparser import ConfigParser
import os


def get_config(section, option):

    config_object = ConfigParser()
    config_object.read("config.ini")

    section = config_object[section]
    optn = section[option]

    return optn


def request_custo():

    date = get_config("RESEARCH", "DATE")
    start = get_config("RESEARCH", "FROM")
    to = get_config("RESEARCH", "TO")

    date.replace("/", "%2F")

    url = "https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&lang=FR&rows=1000&facet=date&facet=origine&facet=destination&facet=od_happy_card&refine.origine={}+(intramuros)&refine.destination={}+(gares+intramuros)&refine.date={}&refine.od_happy_card=OUI&timezone=Europe%2FParis".format(
        start, to, date)

    return url


def download_json(url):

    request = requests.get(url).text
    json_data = json.loads(request)

    with open('./data/train.json', 'w') as f:
        json.dump(json_data, f)
        print(json_data)

    if json_data is None:
        return False
    else:
        return True
