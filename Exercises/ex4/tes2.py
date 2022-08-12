print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
#month_name = input("Input the name of Month:   ")

# if month_name == "February":
#     print("No. of days: 28/29 days")
# elif month_name in ("April", "June", "September", "November"):
#     print("No. of days: 30 days")
# elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
#     print("No. of days: 31 day")
# else:
#         print("Wrong month name")


user_month  = input("Input the name of Month:   ").capitalize()
months_28= "February"
months_30= ["April", "June", "September", "November"]
months_31=[ "January", "March", "May", "July", "August", "October", "December"]


if user_month in months_28:
    print(f"{user_month} has 28 days")
elif user_month in months_31:
    print(f"{user_month} has 31 days")
elif user_month in months_30:
    print(f"{user_month} has 30 days") 