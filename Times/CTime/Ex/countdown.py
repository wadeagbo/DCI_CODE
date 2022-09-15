#EXERCISE:
#Create a program that
#- takes an  int as input
#- uses this int as a countdown
#- visibly counts down
#- prints begin time, end time and countdown int

import time
from time import sleep
import math
#input the  number of seconds 

w = input("Give an integer number:   ")  #input the  number
n =int(w)


for ij in range(1,n+1):   ## 
    ii =n+1-ij            ##  start counting from n
    if ii==n:
        dt_startedx1 = time.time()
        print("%s I begin counting down at: %s "   %( ii, time.ctime() ))
        sleep(1)
    elif ii==1:
        dt_endedx1 =time.time()
        print("%s        I end counting at: %s "   %( ii, time.ctime() ))
        sleep(1)
    else:
        print("%s       counting continues: %s "   %( ii, time.ctime() ))
        sleep(1)

print("Ending time -Starting time", round((dt_endedx1 - dt_startedx1),1 ),'seconds')

