"""
Input arguments

Combining with non-default

If we have parameters with and
without default values, first we need to
define the non-default arguments, and
leave the default ones at the end.
If we define the default arguments
first, the interpreter will produce an
error.
Default arguments must be
defined at the end in the
function header

"""


def full_name(first, last="Doe"):
    return f"{first} {last}"


## This creates error because of the position of the 1st arguamet
def full_name(first="John", last):
    return f"{first} {last}"
