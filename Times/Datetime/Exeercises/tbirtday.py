import math
from datetime import datetime , timedelta

current_datetime = datetime.now()

w = input("Enter the birtdate in format day/month/year:  ")
converted_birthdate =  datetime.strptime(w, "%d/%m/%Y")

date_diff = (current_datetime-converted_birthdate)

difference_in_years = (date_diff.days + date_diff.seconds/86400)/365.2425

print("Birthdate: ", converted_birthdate, " ",  "My years is", int(difference_in_years), "years")




############################

from dateutil.relativedelta import relativedelta

myBirthday = converted_birthdate
now = current_datetime 



difference = relativedelta(now, myBirthday)
print("My years: "+str(difference.years))
