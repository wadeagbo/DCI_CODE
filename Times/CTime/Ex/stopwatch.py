#EXERCISE:
#Create a program that
#- saves current time and prints it
#- saves another time moment and prints it
#- prints the time that has passed in between


import datetime
import time
from time import sleep


print("Starting time           %s"   %time.ctime() )
dt_started = datetime.datetime.utcnow()
dt_startedx = datetime.datetime.now()
dt_startedx1 = time.time()

for i in range(1,6):
    sleep(1)
    print(i ," sec.  after" )
print("After 5s:              ",         time.ctime())
for i in range(6,11):
    sleep(1)
    print(i ," sec.  after" )
print("Ending time after 10s   %s "   %time.ctime() )



dt_ended = datetime.datetime.utcnow()
dt_endedx = datetime.datetime.now()
dt_endedx1 =time.time()

# Difference between the starting and dt_endedxng times

print(( "Difference between the starting and dt_endedxng times:  ", (dt_ended - dt_started).total_seconds() ))
print(( "Difference between the starting and dt_endedxng times:  ", (dt_endedx - dt_startedx).total_seconds() ))
print(( "Difference between the starting and dt_endedxng times:  ", (dt_endedx1 - dt_startedx1) ))




print(datetime.datetime.now())
print(datetime.datetime.utcnow())
print (datetime.datetime.now() - datetime.timedelta(minutes=10))

