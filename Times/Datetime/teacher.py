import datetime

# specified 
t1 = datetime.datetime(2022, 9, 21, 10, 54, 34)
print(t1)
#


# 
print(datetime.date.today())

print(datetime.datetime.today())

test_date = "2001-01-11"  ## string
test_date1 = "2001,01,11"  ## string

print(datetime.date.fromisoformat(test_date))
print(datetime.date(2001,1,11))
print(datetime.date(test_date1)
