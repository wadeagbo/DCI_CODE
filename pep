
https://realpython.com/python-pep8/#why-we-need-pep-8

 readability of Python code.
Code is read much more often than it is written.”

You may spend a few minutes, or a whole day, writing a piece of code to process user authentication. Once you’ve written it, you’re never going to write it again. But you’ll definitely have to read it again. 

, you’ll have to remember what that code does and why you wrote it, so readability matters.


. If you follow PEP 8, you can be sure that you’ve named your variables well. You’ll know that you’ve added enough whitespace so it’s easier to follow logical steps in your code. Yo

 is more readable and easier to come back to. 


If you have more experience writing Python code, then you may need to collaborate with others.





Choosing sensible names will save you time and energy later.



Note: Never use l, O, or I single letter names as these can be mistaken for 1 and 0, depending on typeface:


O = 2  # This may look like you're trying to reassign 2 to zero------------------------



may also be confusing for collaborator


>>> # Not recommended
>>> x = 'John Smith'
>>> y, z = x.split()
>>> print(z, y, sep=', ')
'Smith, John'




h clearer choice of names would be something like this

>>> # Recommended
>>> name = 'John Smith'
>>> first_name, last_name = name.split()
>>> print(last_name, first_name, sep=', ')
'Smith, John'








To rduce typing ---- temptation


# Not recommended
def db(x):                       ##db() could easily be an abbreviation for double. qickly forgotten
    return x * 2



recommended 
# Recommended
def multiply_by_two(x):
    return x * 2






space in between
------------------

class MyFirstClass:
    pass


class MySecondClass:
    pass


def top_level_function():
    return None



------------------

class MyClass:
    def first_method(self):
        return None

    def second_method(self):
        return None


---------------------



----calculating the varianace--------
Each step by leaving a blank line between them. 
There is also a blank line before the return statement. 
This helps the reader clearly see what’s returned:




def calculate_variance(number_list):
    sum_list = 0
    for number in number_list:
        sum_list = sum_list + number
    mean = sum_list / len(number_list)

    sum_squares = 0
    for number in number_list:
        sum_squares = sum_squares + number**2
    mean_squares = sum_squares / len(number_list)

    return mean_squares - mean**2


--------------------------------------




Maximum Line Length and Line Breaking
PEP 8 suggests lines should be limited to 79 characters. 


, keeping statements to 79 characters or less is not always possible. PEP 8 outlines ways to allow statements to run over several lines.

####
def function(arg_one, arg_two,
             arg_three, arg_four):
    return arg_one
###

If it is impossible to use implied continuation, then you can use backslashes to break lines instead:

###
from mypkg import example1, \
    example2, example3



# Recommended
total = (first_variable
         + second_variable
         - third_variable)



# Not Recommended
total = (first_variable +
         second_variable -
         third_variable)

Here, it’s harder to see which variable is being added and which is subtracted.



Indentation

x = 3
if x > 5:
    print('x is larger than 5')

The indented print statement lets Python know that it should only be executed if the if statement returns True. 




The key indentation rules laid out by PEP 8 are the following:

Use 4 consecutive spaces to indicate indentation.
Prefer spaces over tabs.



Sometimes you can find that only 4 spaces are needed to align with the opening delimiter.






Example


x = 5
if (x > 3 and
    x < 10):
    print(x)


Add a comment after the final condition. Due to syntax highlighting in most editors, 
this will separate the conditions from the nested code:

x = 5
if (x > 3 and
    x < 10):
    # Both conditions satisfied
    print(x)



Add extra indentation on the line continuation:

x = 5
if (x > 3 and
        x < 10):
    print(x)

An alternative style of indentation following a line break is a hanging indent. 
You can use a hanging indent to visually represent a continuation of a line of code.


Note: When you’re using a hanging indent, there must not be any arguments on the first line. 
The following example is not PEP 8 compliant:

# Not Recommended
var = function(arg_one, arg_two,
    arg_three, arg_four)


When using a hanging indent, add extra indentation to distinguish the continued line from code contained inside the function.


# Not Recommended
def function(
    arg_one, arg_two,
    arg_three, arg_four):
    return arg_one




#Where to Put the Closing Brace

list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
    ]


list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]


You are free to chose which option you use. But, as always, consistency is key, so try to stick to one of the above methods.




#COMMENTS

Here are some key points to remember when adding comments to your code:

Limit the line length of comments and docstrings to 72 characters.
Use complete sentences, starting with a capital letter.
Make sure to update comments if you change your code.



def quadratic(a, b, c, x):
    # Calculate the solution to a quadratic equation using the quadratic
    # formula.
    #
    # There are always two solutions to a quadratic equation, x_1 and x_2.
    x_1 = (- b+(b**2-4*a*c)**(1/2)) / (2*a)
    x_2 = (- b-(b**2-4*a*c)**(1/2)) / (2*a)
    return x_1, x_2



Inline Comments
x = 5  # This is an inline comment


Use inline comments sparingly.
--Write inline comments on the same line as the statement they refer to.
--Separate inline comments by two or more spaces from the statement.
---Start inline comments with a # and a single space, like block comments.
---Don’t use them to explain the obvious.


Sometimes, inline comments can seem necessary, but you can use better naming conventions
 instead. Here’s an example:

x = 'John Smith'  # Student Name
student_name = 'John Smith'


Finally, inline comments such as these are bad practice as they state the obvious and clutter code:

empty_list = []  # Initialize empty list

x = 5
x = x * 5  # Multiply x by 5


, adding a single space before and after each operator can look confusing. Instead, it is better to only add whitespace around the operators with the lowest priority, especially when performing mathematical manipulation




# Not recommended
if x > 5 and x % 2 == 0:
    print('x is larger than 5 and divisible by 2!')
