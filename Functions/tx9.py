#Packing and unpacking arguments

"""

Keyword arguments
We can automatically pack all
incoming keyword arguments into a
dictionary with the ** operator.
This converts a series of named
elements into a dictionary with those
elements.
With the same operator ** we can also
do the opposite and unpack all
elements in the dictionary data to pass
them on to the function as keyword
arguments
"""


def full_name(*arg, **kwargs):           #**   *a---takes all none takes only one letter
    first = kwargs["first"]
    last = kwargs["last"]
    return f" {arg[0]} {first} {last}"

data = {"first": "James",   
          "last": "Brown"
        }

friend = full_name("Mr" , **data)       #**   I also tried none * it works
print(friend)

