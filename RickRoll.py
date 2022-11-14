#Author ERik Wright

import datetime
import time
import os
import webbrowser

#mehtod to check time if time and date match trigger launch app
def check_time():
    
    tick = False
    count = 0
    while(tick is False):
    
        cur_time = datetime.datetime.now()

        month = cur_time.month
        day = cur_time.day
        hour = cur_time.hour
        minute = cur_time.minute

        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        

        if month == 11 and day == 14 and hour == 1:  
            if count == 0:
                webbrowser.open(url)
                count += 1
        else:
            print("sleep")
            time.sleep(30)
#main method
if __name__ == '__main__':
    check_time()
