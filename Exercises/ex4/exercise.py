# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn
'''
heavy_plus_sign Task 1 - comparison operators
Your task is to write a program which asks the user three times about two integer numbers to compare.

Hint: Use while loop to perform the same operation more than once!

Use both comparison and logical operators, for example use logical comparison between two or more comparion operators:

Example:

result = None
if (expression1) and (expression2):
    print(information)
'''

'''
Create at least ten comparisons!

Some of your results could look like this:
Enter first number: 1234
Enter second number: 5432
Numbers are not equal
Second number is greater than first number
Second number is greater than or equal to first number
Both numbers are big!
big_numbers is set to  True

Enter first number: 23
Enter second number: 4567
Numbers are not equal
Second number is greater than first number
Second number is greater than or equal to first number
Both numbers are not big!
big_numbers is set to  False

'''





Bigg= 1000

i=1
while i <=3:

    a = int(input("Enter first number:           " ))
    b = int(input("Enter second number:           " ))
    cbg = max(a,b)
    
    if a!=b:
        print(f"{a!=b} Numbers are not equal")
        print(f"{cbg} Numbers is bigger")
        if b>a:
            print( f"{b>a} Second number is greater than first number")
        if b>=a:
            print( f"{b>=a} Second number is greater than or equal to first number")
        if b< Bigg and a<  Bigg:
            print( f"{b< Bigg and a<  Bigg} Both numbers are not big!")
        if b>Bigg and a >  Bigg:
        #    Bigg== False
            print( f"{ b>Bigg and a >  Bigg} Big_numbers is not big {max(a,b)}  is bigger than {Bigg}")
        if a >Bigg or b> Bigg:
            print(f" {max(a,b)} is bigger than {Bigg}" )
    
    print(i)
    i +=1




##############



#print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")



# month_name = input("Input the name of Month:   ")

# if month_name == "February":
#     print("No. of days: 28/29 days")
# elif month_name in ("April", "June", "September", "November"):
#     print("No. of days: 30 days")
# elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
#     print("No. of days: 31 day")
# else:
# 	print("Wrong month name")






# user_month  = input("Input the name of Month:   ").capitalize()
# months_28= "February"
# months_30= ["April", "June", "September", "November"]
# months_31=[ "January", "March", "May", "July", "August", "October", "December"]


# if user_month in months_28:
#     print(f"{user_month} has 28 days")
# elif user_month in months_31:
#     print(f"{user_month} has 31 days")
# elif user_month in months_30:
#     print(f"{user_month} has 30 days") 










