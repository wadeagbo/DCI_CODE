"""
Names, objects and mutability
>>> def test(param1=[]):
... print(id(param1))
... param1.append(2)
... print(param1)
...
>>> test()
10501056
[2]
>>> test()
10501056
[2, 2]
The objects that store the default
values are created on function
definition and then are reused.
The first time, param1 starts as an
empty list.
The second time, since the object is
mutable and is not created anew on
every execution, it already contains an
element from the previous call.
Default mutable arguments

The default value of param1
changes when using the function

"""
def test(param1=[]):
    print(id(param1))
    param1.append(2)
    print(param1)

test()
test()
test()
test()
test()
test()
test()
test()
test()
test()

