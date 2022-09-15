import time
import datetime

#datetime.strftime()
#datetime.strptime()

#pytz.timezone()

#IANA
#ISO 8601

for i in range(3):
    print( datetime.datetime.today() )     #  2022-09-15 10:21:49.834275
    print( datetime.date.today() )         #  2022-09-15
    time.sleep(1)



#datetime.date.fromisoformat()

#print(datetime.date())
print(dir(datetime))

#valentines_day = datetime(2021, 2, 14, 8, 20, 30)
#print(valentines_day)


#birth_date = "2005-01-01"
#date.fromisoformat(birth_date)

#datetime.now().strftime("%H:%M:%S")


#german_meeting = "1 January, 2005"  
#datetime.strptime(meeting, "%d %B, %Y")


#usa_meeting = "January 1, 2005"
#datetime.strptime(usa_meeting, "%B %d, %Y")


current_date = datetime.now()
print(current_date)

