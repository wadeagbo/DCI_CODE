from datetime import datetime , timedelta
import calendar

current_datetime = datetime.now()

print("Current date:  ", current_datetime.strftime("%a, %Y,%B,%d"))

print()
print()

print(dir(current_datetime))

print()
print()
print()

## Task 1
print("Task 1")
print("current year:  ",current_datetime.year)




print()
print()
print()

########################################################
## Task 2

print("Task 2")
some_date = datetime(2021, 7, 14)
print("weekday:  ", some_date.weekday() )



print()
print()
print()



#############################################
## Task 3
print("Task 3")

w = input("Enter the date in format day/month/year:  ")
converted_date =  datetime.strptime(w, "%d/%m/%Y")
Year= converted_date.year

if calendar.isleap(Year):
    print(f"{Year} in {converted_date} date   is a leap year")
else:
    print(f"{Year} in {converted_date} date  is NOT a leap year")




print()
print()
print()

## Task 4
print("Task 4  (practice)")

#w = input("imput the date in year/month/day     ")

print("input the date in year/month/day     ")

w = "2022/2/14"

date_time = w



converted_date =  datetime.strptime(date_time, "%Y/%m/%d")
print("converted_date :" , date_time , "=",   converted_date)
print("converted_date :" , date_time , "=",   converted_date.strftime("%Y-%m-%d"))



print()
print()
print()




## Task 4
#################################################

## Task 4
print("Task 4")



from dateutil.parser import parse

date_as_string = "Feb 14 2021 8:30AM"


parse_date_string = parse(date_as_string)

#date_as_string = "Feb 14 2021 8:30AM"
#converted_t1 =  t1.datetime

print('Parse', date_as_string, ':    ', parse_date_string)

