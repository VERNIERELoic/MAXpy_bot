from aquisition import *
from  analysis import *
import time

def main():
    
    url = request_custo()
    seats = get_seats(0)

    while(1):
        if download_json(url):
            seats = get_seats(seats)
            time.sleep(5)
        else:
            time.sleep(5)


if __name__ == "__main__":
    main()
