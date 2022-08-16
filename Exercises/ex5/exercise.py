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


print()
print()
print("  Task 6 - Celsius to Fahrenheit conversion")

'''
Your task is to write a Python program to convert temperatures to and from Celsius, Cahrenheit.

In the centigrade scale, which is also called the Celsius scale, water freezes at 0 degrees and boils at 100 degrees.
In the Fahrenheit scale, water freezes at 32 degrees and boils at 212 degrees.

Note : User should be prompted twice:

to enter a temperature,
to enter a shortcut for given scale (C for Celsius, F for Fahrenheit).
Formula : C/5 = F-32/9, where C = temperature in Celsius and F = temperature in Fahrenheit.

Some of your results could look like this:
Input the scale shortcut you'd like to convert (F - Fahrenheit, C - Celsius: C
Input the value of temperature you'd like to convert  : 60
The temperature in Fahrenheit is 140 degrees.
'''



T1= int(input("Input the scale shortcut you'd like to convert (F - Fahrenheit  1, C - Celsius: C  2:     "))

if T1==1:
    C = float(input("Input the value of temperature you'd like to convert in Celsius  to F:    "))
    TF =  9*C/5.0+32#
    print( f"The temperature in Fahrenheit is {TF}  degrees")
elif T1== 2:
    TF = float(input("Input the value of temperature you'd like to convert in Fahrenheit to C:    "))
    Ct =(TF-32)*5/9.0
    print( f"The temperature in Celcius is {Ct}  degrees")


print()
print()
print("Task 7 - pattern")
print()
print()


''' 
Your task is to write a Python program to construct the following pattern. Upper part should be done in one line of code without using a loop.
Lower part can be done with any kind of loop or also with one line of code and without loops.
'''

T =" * "
for i in range(1,5):
    print( i*T)
for i in range(1,5):
    j = 6-i
    print(j*T)
print(T)




print()
print()
print(" Task 8 - Fibonacci series")
print()
print()

'''
Your task is to write a Python program to get the Fibonacci series between 0 to 50.

Note: The Fibonacci Sequence is the series of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
'''







from PIL import Image
myImage = Image.open("/home/user/Documents/DCI_CODE/Exercises/ex5/fib.png");
myImage.show()




def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return fib(n-1)+fib(n-2)

for i in range(11):
    print(i, fib(i))
