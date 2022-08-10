# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


print()
print("Task 1 - basic math operations")

''''''
'''Your task is to write a program which asks the user three times for a number. If number is even print ‘Even number’, else print ‘Odd number’.

Hint: you can use for or while loop to perform the same operation more than once!

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

# I want the range of numbers from 1 to 3

def range1(start,end):
    return range(start,end+1)

#  For each number from 1 to 3
nr = int(input("Enter number of arguments in range() function:   "))
for n in range1(1,nr):
    if n==1:
        n1=input("Enter number of arguments in range() function:   ")
        st=int(n1)
        lst1 ={x  for x in range1(1,st)}
        print("task for n=1 in the 1 to 10:   ",   list(lst1))
    elif n==2:
        n2a = input("1st of the two numbers ")
        n2b = input("2nd of the two numbers ")
        lst2a, lst2b = int(n2a), int(n2b)
        lst2n ={x1  for x1 in range1(lst2a,lst2b)}
        print(f"task for n=2 in the range {lst2a,lst2b}:   ",   lst2n)
    elif n==3:
        n3a = input("1st of the two numbers to begin")
        n3b = input("2nd of the two numbers to end ")
        n3c = input("Number to use as interval")
        lst3a, lst3b, lst3c = int(n3a), int(n3b), int(n3c)
        lst3n ={x2  for x2 in range(lst3a,lst3b, lst3c)}
        print(f"task for n=3 in the range {lst3a,lst3b,lst3c}:   ",   lst3n)
