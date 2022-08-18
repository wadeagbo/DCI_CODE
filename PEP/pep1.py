
#Use of  vaviables

# Not recommended
x = 'John Smith'
y, z = x.split()
print(z, y, sep=', ')



print()


# Recommended
name = 'John Smith'
first_name, last_name = name.split()
print(last_name, first_name, sep=', ')



x = 'John Smith'  # Student Name   (bad)
student_name = 'John Smith'

#inline comments such as these are bad practice as they state the obvious and clutter code:





## adding a single space before and after each operator can look confusing.
# Not recommended
if x > 5 and x % 2 == 0:
    print('x is larger than 5 and divisible by 2!')



# Recommended
if x>5 and x%2==0:
    print('x is larger than 5 and divisible by 2!')






# Recommended
y = x**2 + 5
z = (x+y) * (x-y)

# Not Recommended
y = x ** 2 + 5
z = (x + y) * (x - y)




#Here is a block comment explaining the function of a for loop. Note that the sentence wraps to a new line to preserve the 79 character line limit:

for i in range(0, 10):
    # Loop over i ten times and print out the value of i, followed by a
    # new line character
    print(i, '\n')
 



def quadratic(a, b, c, x):
    # Calculate the solution to a quadratic equation using the quadratic
    # formula.
    #
    # There are always two solutions to a quadratic equation, x_1 and x_2.
    x_1 = (- b+(b**2-4*a*c)**(1/2)) / (2*a)*x
    x_2 = (- b-(b**2-4*a*c)**(1/2)) / (2*a)*x
    return x_1, x_2

Q1 = quadratic(1,1,1, 2)
print(Q1)











x = 'John Smith'  # Student Name
student_name = 'John Smith'



#Finally, inline comments such as these are bad practice as they state the obvious and clutter code:

empty_list = []  # Initialize empty list

x = 5
x = x * 5  # Multiply x by 5



# Recommended
y = x**2 + 5
z = (x+y) * (x-y)

# Not Recommended
y = x ** 2 + 5
z = (x + y) * (x - y)



## adding a single space before and after each operator can look confusing.
# Not recommended
if x > 5 and x % 2 == 0:
    print('x is larger than 5 and divisible by 2!')



# Recommended
if x>5 and x%2==0:
    print('x is larger than 5 and divisible by 2!')