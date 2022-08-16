# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn
import  math 

print()
print("Task 1 - calculate sum ")
print()
print()
'''
Your task is to write a Python program to calculate the sum of three integers given (prompted) by user.
If the values are equal then calculate triple value of their sum.
Print out an appropriate message to the user.
'''
#####################################
print("Your task is to write a Python program to calculate the sum of three integers given (prompted) by user.")
i = 0
sum = 0
while i < 3:
    
    i +=1 
    if i==1:
        a = int(input( "First number:     "))
        a1st = a
    elif i==2:
        a = int(input( "Second number:     "))
        a2nd = a
    elif i==3:
        a = int(input( "Third number:     "))
        a3rd =a 


    sum =sum +a

 #   print(i)
if a1st!=a2nd and  a1st!=a3rd   and  a2nd!=a3rd:
    print("The sum is:  ",  sum)
    print("The numbers are not equal, sum is calculated ")

else:
    print("The triple sum is:  ",  sum*3)
    print("The values are equal, the  triple value of their sum is calculated. ")


##########################################



print()
print("Task 2 - get the difference")
print()



i = 0
sum = 0
while i < 2:

    i +=1
    if i==1:
        a = int(input( "First number:     "))
        a1st = a
    elif i==2:
        a = int(input( "Second number:     "))
        a2nd = a

diff1 =  a1st - a2nd

#    print("The result of calculated difference is:    ", diff1)

# If the first number is greater than second then calculate double difference between numbers.
if  a1st > a2nd:
    print("The result of calculation is:    ", diff1*2)
    print("The  double difference calculated.  The first number is greater than second.")
else:
# The first number is NOT  greater than second 
    print("The result of calculation is:    ", abs(diff1))
    print("The abs  difference calculated. The first number is NOT  greater than second")

#############################




print()
print("Task 3 -  odd or even number")
print()



num1 = int(input( " Number to check: "))
if  num1%2==0:
    print ( f"{num1} is an even number!")
else:
    print ( f"{num1} is an odd number!")


##########################################



print()
print("Task 4 - circle area")
print()

r  = input( " Input the radius of the circle: ")
radius = float(r)
Area = math.pi*radius**2
print(f" The area of the circle with radius {radius} is:      {round(Area,2)}" )




#########################

print()
print("Task 5 - guess a number")
print()
#########Your task is to write a Python program to guess a number between 1 to 9.  ##

import random
target_num, guess_num = random.randint(1, 10), 0

while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')
~
