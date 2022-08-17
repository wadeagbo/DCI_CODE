class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("My name is "+ self.name)
        print("I am " + str(self.age) + " years old" )


P1= Person("Waheed", 51)
P1.myfunc()
