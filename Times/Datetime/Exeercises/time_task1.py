from datetime import datetime , timedelta

current_datetime = datetime.now()
print ("Current Date time:  ", current_datetime)
print ("15 days before:     ",current_datetime +timedelta(days=-15))
print()
print()
print()


#  Task 1

day_today = "8/07/2021"
d= datetime.strptime(day_today, "%d/%m/%Y")
print("Format 8/07/2021 =  ", d)
td= d +timedelta(days=-15)
print ("15 days before:     ",td)
print ("15 days before:     ",td.strftime("%Y-%m-%d"))


#############



current_datetime = datetime.now()

w = input("Enter the birtdate in format day/month/year:  ")
converted_birthdate =  datetime.strptime(w, "%d/%m/%Y")

date_diff = (current_datetime-converted_birthdate)

difference_in_years = (date_diff.days + date_diff.seconds/86400)/365.2425

print("Birthdate: ", converted_birthdate, " ",  "My years is", int(difference_in_years), "years")
print("Age Time delta: ", date_diff )



############################

from dateutil.relativedelta import relativedelta

myBirthday = converted_birthdate
now = current_datetime



difference = relativedelta(now, myBirthday)
print("My years: "+str(difference.years))
##############################







print()
print()
print()
###############################################################
#  Task 2
current_datetime_n2 = "8/07/2021"
converted_current_datetime_n2 =  datetime.strptime(current_datetime_n2, "%d/%m/%Y")
print("Format 8/07/2021 =  ", d)
td= d +timedelta(days=7)
print ("7 days after:       ",td)
print ("7 days after:       ",td.strftime("%Y-%m-%d"))




print()
print()
print()


########################################################

#  Task 3
#starting_rent = '25 January, 2021'
#converted_starting_rent = datetime.strptime(starting_rent, "%d %B, %Y")
#print("Starting_rent:    "   ,  converted_starting_rent) 




start_date = datetime(year=2020, month=1, day=1)
date_25 = datetime(year=2021,month=1, day=25)  

print("Starting date:    "   ,  start_date.strftime("%d %B, %Y")) 
#print("After 25 days:    "   ,  date_25)
print("Hello Friedrich, your rent of 300 € is due on "   ,  date_25.strftime("%d %B, %Y"))


print()
print()
print()
print()


##########


print("Starting date:    "   ,  start_date.strftime("%d %B, %Y"))

input_list= [2020,1,25,2021,1,25]


y1 = input_list[0]
m1 = input_list[1]
y2 = input_list[3]
m2 = input_list[4]

if y1 > y2:
    raise Error("first date after second")
elif y1 == y2:
    if m1 == m2:
        count = 0
    elif m2 > m1:
        count = m2 - m1
    else:
        raise Error("first date after second")
else:
    count = (12 + m2) - m1
    if count > 12:
        raise Error("more than 12 month difference")

count += 1  # inclusive of the same month
print(count)


import datetime
from dateutil.rrule import rrule, MONTHLY

date_start = start_date+timedelta(days=24)
#datetime.date(y1, m1, 25)

#months1 = [dt.strftime("%d %B %Y") for dt in rrule(MONTHLY, dtstart=date_start, count=count)]

for dt in rrule(MONTHLY, dtstart=date_start, count=count):
    months1 = dt.strftime("%d %B %Y")
    print(f"Hello Friedrich, your rent of 300 € is due on {months1}")

