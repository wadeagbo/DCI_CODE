import datetime
d1 = datetime.datetime.today()   # this shows current date and time
d2 = datetime.datetime(2022, 1, 1, 1 , 1 , 30)   # this convert the numbers to the datetime object (with time)
d3 = datetime.datetime.strptime('January 15, 2005', '%B %d, %Y') # presents our date and time in datetime object
d4 = d3.strftime('%Y-%d-%B %H:%M:%S')   # format the datetime object according to our formatting
d5 = datetime.date(2022,1,1)     # this convert the numbers to the datetime object (without time)
d6 = datetime.date.today()     # this just shows the current date
d7 = datetime.date.fromisoformat('2005-01-01')     # creates date time object
d8 = datetime.date(year=2000, month=1, day=1)     # datetime instance, (year, month and day are 'keys')
d9 = d3.year              # takes out the year from a datetime object as 'int' value
d10= d3.month             # takes out the month from a datetime object as 'int' value
d11= d3.hour             # takes out the hour from a datetime object as 'int' value
d12= d2 + datetime.timedelta(days=366) # timedelta method is used for calculating the differences in dates (uses days, seconds, weeks)
d13= dir(datetime)     # shows the list of methods for datetime module
print("d1", d1,"\nd2", d2,"\nd3",d3,"\nd4",d4,"\nd5",d5,"\nd6",d6,"\nd7",d7,"\nd8",d8,"\nd9",d9,"\nd10",d10,"\nd11",d11,"\nd12",d12,"\nd13",d13)
