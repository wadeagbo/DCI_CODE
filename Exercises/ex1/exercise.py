# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn
# Start the exercise 
#
print() 
print("Hello", "world", sep=" - ")
print(type("Hello"))
print(isinstance(123,int))
print(" ")
print("Task 1 - printing single object")
print(234)
print(float(43.12))
print(3+2j)
print("Hello")
print(True)

if 3>5:
    print(True)   
else:
    print(False)

print(5>3)

"""
You can use triple-quoted strings. When they're not a docstring (the first thing in a class/function/module), they are ignored.
Read aforementioned answer from Stack Overflow!
""" 

print()
print("Task 2 - printing type of given value")
a = 123
print( f"{a} is type of " , type(a))
b = 43.23
print( f"{b} is type of " , type(b))
c = 4-1j
print( f"{c} is type of " , type(c))
greet= "How are you?"
print( f"{greet} is type of " , type(greet))
BOOLT= True
print( f"{BOOLT} is type of " , type(BOOLT))



print()
print("Task 3 - checking type of value")

Berlin= "city"
print(isinstance(Berlin,str))
print(isinstance(Berlin,complex))
numbi= 123
print(isinstance(numbi,int))
numbf= 123.7
print(isinstance(numbf,float))
print(isinstance(numbf,bool))



print()
print("Task 4 - checking type of value (version 2)")


print( f" Is {a} an instance of int?:   " , isinstance(a,int))
print( f" Is {b} an instance of bool?:   " , isinstance(b,bool))
print( f" Is {c} an instance of complex?:   " , isinstance(c,complex))
print( " Is True an instance of bool?:   " , isinstance(True,bool))
print( f" Is '{greet}' an instance of float?:   " , isinstance(greet,float))

print()
print("Task 5 - using comments in code)")

# This is my first comment
# Block comments are indented to the same level as that code

print("Hello")
print("Line with inline code!")  # remember about spacing!

print(type(123.45))  # getting type of number 


"""
You can use triple-quoted strings. When they're not a docstring (the first thing in a class/function/module), they are ignored.
Read aforementioned answer from Stack Overflow!
"""