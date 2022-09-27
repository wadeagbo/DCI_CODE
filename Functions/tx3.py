#order of execution

my_variable = "A string"   #1

def hello_world():
    print("I’m inside")    #2


my_other_variable = 1     #3
hello_world()              #4
print("I’m outside")       #5
