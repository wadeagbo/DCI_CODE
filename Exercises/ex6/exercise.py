# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn
''' 
Bug fixing

In this exercise, there will be several programs that don't work as they should after running or they even don't start at all..
Your task is to run the program, find the bug and fix it smiley
Read carefully information from the console about errors in the program.
By working through these examples, you should get better at:

--reading errors
--debugging
---reading and editing other people's code
---Googling for specific issues
---solving errors on your own


'''


print(" Task 1 - fix the FizzBuzz ") 




for n in range(1,100):
    if n%3==0 and n%5==0:
        print(" print 'fizzbuzz' for multiples of 3 and 5. ", n) 
    elif n%3==0:
        print(" print 'fizz' for multiples of 3, " , n)
    elif n%5==0: 
        print(" print 'buzz' for multiples of 5, " , n)
   

1 

''' 
three_mul = 'fizz
five_mul = 'buzz'
num1 = 3
num2 = 4 
max_num = 100


for i in range(1,max_number):
    # % or modulo division gives you the remainder 
    
    if i%num1 = 0:
        print(i, three_mul)
    elif i%num2 == 0:
        print(i, five_mul)
    elif i%num1 == 0 and i%num2 == 0:
    print(i, three_mul+five_mul)


Find the 7 bugs and fix them smiley


(1) max_num
(2) elif i%num1 == 0 and i%num2 == 0:

    '''




#Program with exactly 7 bugs:

three_mul = 'fizz'
five_mul = 'buzz'
num1 = 3
num2 = 4 
max_num = 100
   
for i in range(1,max_num):
    # % or modulo division gives you the remainder 
    

    if i%num1 == 0 and i%num2 == 0:
        print(i, three_mul+five_mul)
    elif i%num1 == 0:
        print(i, three_mul)
    elif i%num2 == 0:
        print(i, five_mul)


print()

print("Task 2 - summing integers")

'''
n = 5
number = 1
sum = 0
while number < n + 1:
    sum = sum + 1
    number = number + 1
print("Sum =", sum)
'''



n = 5
number = 1
sum = 0
while number < n + 1:
    sum = sum + number
    number = number + 1
print("Sum =", sum)



print("Task 3 - summing integers with range")

'''
 Your task is to fix program non-working correctly. The problem:

sum integers from 1 to 5 using range() function
calculate what result should be and what you get after running the program
Program with bug:

n = 5
sum = 0
for num in range(n):
    sum += num
print("Sum =", sum)
Find the bug and fix it smiley

Your result could look like this:
Sum = 15
 
'''

n= 5
sum = 0
for num in range(n+1):
    sum += num
print("Sum =", sum)
 

print()

print("Task 4 - printing in loops")


'''
Your task is to fix program non-working correctly. The problem:

there are 4 short programs with loops, that should print some numbers, but they don't work at all!
Program no. 1 with the bug:

for x in range(3)
    print(x)
Find the bug and fix it smiley

Your result could look like this:
0
1
2
Program no. 2 with the bug:

for j in range(5):
    print("This is loop number j")
Find the bug and fix it smiley
'''



for x in range(3): 
    print(x)


for j in range(5):
    print(f"This is loop number {j}")

x=10
while x > 0:
    print(x)
    x -= 1   # x =x-1


print()
print()
print()

countdown = 5
while countdown > 0:
    print(f"{countdown}")
    countdown -= 1
else:
    print("Start!")


print()
print()
print("    Task 5 - summing three integers")


x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x ==y or y == z or x==z:
    result = 0
    print("Calculated sum is ", result)

else:
    sum = x + y + z
    print("Calculated sum is   ", sum)




print()
print()
print(" Task 6 - summing two integers ")


x = int(input("First number: "))
y = int(input("Second number: ")) 

result = x + y

if result >= 15 and result <= 20:
    sum = 20
    print("Calculated sum is ", sum)
else: print("Calculated sum is ", result)






print()
print()
print(" Task 7 - swapping variables  ")

a = input("First value: ")
b = input("Second value: ")



print("Before swapping: a =",  a,  "  b =  ",  b)

temp = a
a = b
b= temp

print("After swapping:  a =",  a, "  b =  ", b)





print()
print()
print(" Task 8 - max and min values")



x = float(input("First number: "))
y = float(input("Second number: "))
z = float(input("Third number: "))

print("The maximum value is ", max(x, y ,z))
print("The minimum value is ", min(x, y ,z))




print()
print()
print("Task 9 - conversion ")

x = input(" Type your value: ")

if x == '0':
    x = False
    print("Your entered value is now ", x)
elif x == '1':
    x = True
    print("Your entered value is now ", x)
else:
    pass
    print("Your entered value is now ", x)



print()
print("Task 10 - divisible number")



'''
Your task is to fix program non-working correctly.
The problem:  
- accept (prompt) two integers values from the user  
- check whether a first number is divisible by second number and vice versa  
- display results  

Program with bugs:  
```python
x = input("First number: ")
y = input("Second number: ")

if x %% y >= 0:
    print("First number is divisible by second number, result =", x // y)
elif y %% y != 0:
    print("Second number is divisible by first number, result =", y // x)
else:
    print("Numbers are non-divisable!")
```

>Find the bug and fix it :smiley:
- Your result could look like this:

```bash
First number: 5
Second number: 55
Second number is divisible by first number, result = 11.0

First number: 3
Second number: 5
Numbers are non-divisable!
```
### 
'''



x = float(input("First number: "))
y = float(input("Second number: "))

if x % y== 0:
    print("First number is divisible by second number, result =", y/x)
elif y % x == 0:
    print("Second number is divisible by first number, result =", y/x)
else:
    print("Numbers are non-divisable!")   
    #