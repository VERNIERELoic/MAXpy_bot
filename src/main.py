from travel import *
from configparser import ConfigParser
import time
import json
import requests
import os

def get_config():
    
    list_config = []
    list_value = []
    config = ConfigParser()
    config.read("config.ini")

    for each_section in config.sections():
        tab = []
        for (each_key, each_val) in config.items(each_section):
              tab.append(config[each_section][each_key])
        list_config.append(tab)

    return list_config

get_config()



def main():

    list_config = get_config()
    travels_objs = []
    for i in range(len(list_config)):
        travels_objs.append(Travel(list_config[i][0], list_config[i][1], list_config[i][2], ""+list_config[i][1]+"-->"+list_config[i][2]+""))

    isFistTimeInLoop = True
    test = 1
    while(1):
        for i in range(len(travels_objs)):
            travels_objs[i].set_url()
            #if travels_objs[i].get_data(i):
            if test == 1:
                travels_objs[i].read_data(i, isFistTimeInLoop)
                time.sleep(5)
            else:
                time.sleep(5)
        isFistTimeInLoop = False


if __name__ == "__main__":
    main()
