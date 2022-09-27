import datetime
import pytz

dt_utcnow0 = datetime.datetime.now()
print('No pytz option:   ', dt_utcnow0)
print()

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print("pytz.UTC set to tz option:    ", dt_utcnow)
print()

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print("Using pytz option with a specific timezone (astimezone) (pytz.time()) :   " , dt_mtn)






# To see all the time zones
print("All the time zones available printed as list or one by one")
#print(pytz.all_timezones)


for tz in pytz.all_timezones:
    country= tz
    dt_country = dt_utcnow.astimezone(pytz.timezone(country))
    print("Timezone of ", country, dt_country )


#country= 'Africa/Lagos'
#dt_country = dt_utcnow.astimezone(pytz.timezone(country)) 
#print("Timezone of ", country, dt_country )

