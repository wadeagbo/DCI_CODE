from datetime import datetime , timedelta
from dateutil.rrule import rrule, MONTHLY

count = 13
start_date = datetime(year=2020, month=1, day=1)
date_start = start_date+timedelta(days=24)

for dt in rrule(MONTHLY, dtstart=date_start, count=13):
    months = dt.strftime("%d %B %Y")
    print(f"Hello Friedrich, your rent of 300 € is due on {months}")





start_date = datetime(2020, 1, 1)+ timedelta(days=24)
for i in  list(rrule(freq=MONTHLY, count=13, dtstart=start_date)):
    print(i.strftime("%d %B %Y"))
#[datetime.datetime(2014, 12, 31, 0, 0), 
# datetime.datetime(2015,  1, 31, 0, 0), 
# datetime.datetime(2015,  3, 31, 0, 0), 
# datetime.datetime(2015,  5, 31, 0, 0)]
