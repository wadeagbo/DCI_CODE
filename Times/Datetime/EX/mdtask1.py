#import datetime
#print( datetime.datetime.today() )
#print( datetime.date.today() )



from datetime import datetime, date, timedelta 

# Get current date  and time
print(datetime.today() )

# Get current date 
print(date.today() )

#ISO 
#MM/DD/YYYY---US
#DD/MM/YYYY---EUR

#date_as_string ="2022-01-26"
date_as_string ="2022-12-06"

print(date_as_string)

print(date.fromisoformat(date_as_string))

###  Easier to put out data from ISO conversion


print(dir(datetime))

##Create some daytime objects


# Create a datetime object with time

#date1 = datetime(2022, 1, 26, 10, 12)
date1 = datetime(year=2022, month=1, day= 26, hour=10, minute=12, second=58)

print(date1)

# Create a datetime object with just the  date
date2 = date(2022, 1, 26)
print(date2)


valentines_day = datetime(2021, 2, 14, 8, 20, 30)
print(valentines_day)


birth_date = "2005-01-01"
print(date.fromisoformat(birth_date))


print(date(2005, 1, 1))

print (date(year=2001, month=10, day=10))
print (date(month=10, year=2001,  day=10))

## Different countries 
#usa_meeting = "January 1, 2005"
usa_meeting = "January 1 2005"
#print("US January 1, 2005:  ", datetime.strptime(usa_meeting, "%B %d, %Y"))
print("US: January 1, 2005:  ", datetime.strptime(usa_meeting, "%B  %d %Y"))

My_meeting = "2007, 1 January"
print("2007, 1 January:  ", datetime.strptime(My_meeting, "%Y,  %d %B"))

#  %B = Full month
#  %d = numerical date
#  %Y = full Year


# converting string to date object

german_meeting = "1 January, 2005"
print("DE   1 January, 2005:  ", datetime.strptime(german_meeting, "%d  %B, %Y"))



# changing the formating of the object


print("valentines_day:  ", datetime.strftime(valentines_day, "%Y %B %d %H  %M %S"))
print("valentines_day:  ", datetime.strftime(valentines_day, "%Y-%m-%d %H:%M:%S"))


print("Time now:", datetime.now().strftime("%H:%M:%S"))


print("US: January 1, 2005:  ", (datetime.strptime(usa_meeting, "%B  %d %Y")).strftime("%H %M %S"))


# Useful when cherrypicking specific parts of the datetime object

print("US: January 1, 2005 (year only):  ", (datetime.strptime(usa_meeting, "%B  %d %Y")).strftime("%Y"))
print("US: January 1, 2005 (month only):  ", (datetime.strptime(usa_meeting, "%B  %d %Y")).strftime("%B"))
print("US: January 1, 2005 (month only):  ", (datetime.strptime(usa_meeting, "%B  %d %Y")).strftime("%m"))
print("US: January 1, 2005 (day only):  ", (datetime.strptime(usa_meeting, "%B  %d %Y")).strftime("%d"))
print("US: January 1, 2005 (day and  @ month):  ", (datetime.strptime(usa_meeting, "%B  %d %Y")).strftime("%d @ %m"))




#strptime --string   strftime---object  (put all in the same format) 




###  Datetime instance properties / methods
current_date = datetime.now()
print('current_date:  ',  current_date )
print('current_date (Hour) :  ',  current_date.strftime("%H")  )

#Instances

date1  = "March 28 2011 16:12:45"

#Convert to datetime object

convert_date1 = datetime.strptime(date1, "%B  %d %Y %H:%M:%S")
print(convert_date1)


##  Cherrypick the year

print(convert_date1.strftime("%Y"))

## Unsing the instance

print(convert_date1.year)


#manipulate the year

year = convert_date1.year
year += 2
print(year)


print(convert_date1.year)
print(convert_date1.month)
print(convert_date1.day)
print(convert_date1.hour)
print(convert_date1.minute)
print(convert_date1.second)
print(convert_date1.microsecond)




#Time delta

#Calculate the difference between two times

time_1  = datetime(day =14, month= 6, year= 2022, hour =9, minute= 0)
time_2  = datetime(day =14, month= 6, year= 2022, hour =16, minute= 15)

difference= time_2-time_1
print(difference)


#Calculate a time in the future

time_3 = datetime(day= 14, month=6, year= 2022)


## Only days montth mininute microseconds
print(time_3 +  timedelta(days=7))




#### Can
