#import datetime
#print( datetime.datetime.today() )
#print( datetime.date.today() )



from datetime import datetime, date 

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

date1 = datetime(2022, 1, 26, 10, 12)
print(date1)

# Create a datetime object with just the  date
date2 = date(2022, 1, 26)
print(date2)

