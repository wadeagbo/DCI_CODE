## time base object stored in human readable objects aparat from python
#portable 
# send time to backend server
# timestamps == recorded time   ==start and finish (span)
# also known as unix time time 
# measures the time in milliseconds since jan 1 1970


from datetime  import datetime

time_1  = datetime(day =14, month= 6, year= 2022, hour =9, minute= 0)


print(time_1)
print(datetime.timestamp(time_1))

## can be stored in database
## the request, portable can be sent to the server
#portable representation of data object (float)

times_stamp= datetime.timestamp(time_1)
print("Timestamp:   ", times_stamp)

# convert back to the object

time_2 = datetime.fromtimestamp(times_stamp)
print("Daytime from Timestamp:  " ,  time_2)

print(time_2.year, time_2.month, time_2.day)


