# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


print()
print("Task 1 - basic math operations")

''''''
'''Your task is to write a program which asks the user three times for a number. If number is even print ‘Even number’, else print ‘Odd number’.

Hint: you can use for or while loop to perform the same operation more than once!
 Task 6 - divisible numbers
Some of your results could look like this:
Enter number: 123
Odd number
Enter number: 32
Even number
Enter number: 121234
Even number'''


print()
print()
for ncount in  range(3):
    num = input("Enter number:   ")
    n = float(num)
    if n%2==0:
        print("Even number")
    else:
        print("Odd number")    

print("program finished n=3 ")

nlist ={56,45,456}
lstcm = {n:"Even number" if n%2==0 else "Odd number" for n in nlist }

print(lstcm)

####################################################################


print()
print()
print()
print("Task 2 - printing numbers with range() function")
print()
print()

'''
Your task is to write a program which asks the user about number of arguments in range() function.
If number is 1 program asks for another number and then prints digits from range() function with given number.
If number is 2 program asks for two numbers and then prints digits from range() function with given range.
If number is 3 program asks for three numbers and then prints digits from range() function with given range and given step.
'''

# To force range starting from 1 and end at 3.
def range1(start,end):
    return range(start,end+1)


#r task is to write a program which asks the user about number of arguments in range() function.

nr = int(input("Enter number of arguments in range() function:   "))


for n in range1(1,nr):
    if n==1:
#If number is 1 program asks for another number and then prints digits from range() function with given number.
        ns   = input("Enter starting number:   ")
        nst  = int(ns)
        for  x in range(nst): 
            print(x)

        lst1 =[x  for x in list(range(nst))]  # list comprehension
        print(lst1)

# If number is 2 program asks for two numbers and then prints digits from range() function with given range.
    elif n==2:
        ns   = input("Enter starting number:   ")
        nst  = int(ns)
        ne   = input("Enter stopping number:   ")
        ned  = int(ne)

        for  x in range(nst,ned): 
            print(x)

        lst2 =[x  for x in list(range(nst,ned))]    # list comprehension
        print(lst2)

# If number is 3 program asks for three numbers and then prints digits from range() function with given range and given step.
    elif n==3:
        ns   = input("Enter starting number:   ")
        nst  = int(ns)
        ne   = input("Enter stopping number:   ")
        ned  = int(ne)
        ste  = input("Enter step:   ")
        step = int(ste)
        for  x in list(range(nst,ned,step)): 
            print(x)   

        lst3 =[x  for x in list(range(nst,ned, step))]  # list comprehension
        print(lst3)



#########################


print()
print()
print()
print( "Task 3 - finding divisors of a number")
print()
print()


numb   = input("Enter number:    ")
nn  =   int(numb)
for i in range1(1,nn):
    if nn%i==0:
        print(i)

lst = [x for x in range1(1,nn) if nn%x==0 ]
print(lst)



#################  Task 4 ################
print()
print()
print( " Task 4 - check prime number")
print()
print()


numb   = input("Enter number:    ")
nn  =   int(numb)
ncount1=0
for i in range1(1,nn):
    if nn%i==0:
        ncount1 +=1
        if ncount1 > 2:
            print(f"{nn} is not a prime number")
    
        elif ncount1 ==2 and i==nn:
            print(f"{nn} is a prime number")


lst = [x for x in range1(1,nn) if nn%x==0 ]
print(lst)





print()
#### Alternative to task 4
print (" Alternative to  task 4     Prime, odd and even numbers finder")
print()



numb   = input("Enter number:    ")
nn  =   int(numb)

prime = True
odd   = True

for i  in range(2,nn):
    if  nn%i==0:
        prime = False

if nn%2==0:
    odd  = False


if prime==True:
    print(f"{nn}  is a prime number")
else:
    print(f"{nn}  is not  prime number")

if odd ==True:
    print(f"{nn}  is odd  number")
else:
    print(f"{nn}  is even  number")


print([x for x in range(1,nn+1) if nn%x==0 ])



#################  Task 5 ################

 








print()
print()
print( "Task 5 - FizzBuzz")
print()
print()


for x in range(1,101):
    if x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    elif x%3==0 & x%5==0:
        print("FizzBuzz")
    else:
        print(x)



############  Task 6  ##################
print()
print()
print( " Task 6 - divisible numbers")
print()
print()



for y in range(1000,2001):
    if y%7==0 and y%5 !=0:
        print(y)
lis = [ y for y in range(1000,20001) if y%7==0 and  y%5!=0 ]
print(lis)




