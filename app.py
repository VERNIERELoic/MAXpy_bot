from aquisition import *
from  output import *
import time

def main():
    
    url = request_custo()
    old_train_list = []
    new_train_list= []

    old_train_list.append(set_output_file(old_train_list))

    while(1):
        if download_json(url):
            new_train_list.append(set_output_file(old_train_list))
            time.sleep(5)
        else:
            time.sleep(5)



if __name__ == "__main__":
    main()
