# To force range starting from 1 and end at 3.
#from sys import 


from fileinput import close


def range1(start,end):
    return range(start,end+1)


numb   = input("Enter number:    ")
nn  =   int(numb)
ncount1=0
for i in range1(1,nn):
    if nn%i==0:
        ncount1 +=1
        if ncount1 > 2:
            print(f"{nn} is not a prime number")
        elif ncount1 ==2:
            print(f"{nn} is a prime number")


lst = [x for x in range1(2,nn) if nn%x==0 ]
print(lst)

#################

for x in range(1,101):
    if x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    elif x%3==0 & x%5==0:
        print("FizzBuzz")
    else:
        print(x)





        ######################

print()
print()


for y in range(1000,2001):
    if y%7==0 and y%5 !=0:
        print(y)
#lis = [ y for y in range(1000,20001) if y%7==0 and  y%5!=0 ]
#print(lis)