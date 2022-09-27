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


def full_name(**kwargs):           #**
    first = kwargs["first"]
    last = kwargs["last"]
    return f"{first} {last}"

data = {"first": "James",   "last": "Brown"}

friend = full_name(**data)       #**   I also tried none * it works
print(friend)

