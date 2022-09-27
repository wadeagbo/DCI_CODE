import math
print()
print('############')
print("Example 1")
print('############')
print()

def simp_maths(x,y):
    print("values: ",  x, " , ",  y)
    print("I return: addition, substraction, multiplication, division in this order")
    addition= x+y
    substraction = x-y
    multiplication = x*y
    division  = x/y
    return addition, substraction, multiplication, division


print(simp_maths(10,2))








print()
print('############')
print("Example 2")
print('############')
print()


def simp_maths2(x,y,z):
    print("values: ",  x, " , ",  y, "operation: ", z)
    if z=='+':
        addition= x+y
        answer = addition
    elif  z=='-':
        substraction = x-y
        answer = substraction
    elif  z=='x':
        multiplication = x*y
        answer = multiplication
    elif  z=='/':
        division  = x/y
        answer = division
    elif z=='pow':
        Power = math.pow(3,2)
        answer = Power
    return answer



print(simp_maths2(3,4,'+'))
print()
print(simp_maths2(7,3,'-'))
print()
print(simp_maths2(5,4,'x'))
print()
print(simp_maths2(5,4,'/'))
print()
print(simp_maths2(3,2,'pow'))


