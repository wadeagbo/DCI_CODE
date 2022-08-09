# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

import math

from telnetlib import TTYLOC


print()
print("Task 1 - basic math operations")

#Hint: You can assign math operation to a variable, and then perform another math operation on this variable, for example:

a = 2/3
print(round(a, 2))  # result is 0.67
pie =22/7
print(round(pie,4))


print()
print("Task 1 - basic math operations")

ex_add=  12 + 34
print( "12 + 34 = ", ex_add) 
ex_sub=43 - 56
print( "43 - 56  = ", ex_sub) 
ex_mult= 4 * 4
print( "4 * 4  = ", ex_mult)
ex_div= 4 / 5
print( "4 / 5  = ", ex_div)
print( "12 % 5  = ", 12 % 5)
print("2 ** 4 = ", 2**4)
print("12 // 3  = ", 12 // 3)
print("12.2 // 3  = ", 12 // 3)
T = True
F = False
TF= T*F
TT = T*T
FF = F*F
print( f"{T} * {F} = " , TF  )
print( f"{T} * {T} = " , TT  )
print( f"{F} * {F} = " , FF  )

constant = 5
cmplx = (2-3j)
ccomplx = constant*cmplx
print (f"{constant} * {cmplx} = ", ccomplx) 



print()
print("Task 2 - basic math functions")

ex_max = max(2, 2.0, -0.5)
print("max(2, 2.0, -0.5) = " , ex_max )
ex_min = min(23, 22, 55.0) 
print("min(23, 22, 55.0) = " , ex_min)
ex_abs = abs(-34.23) 
print("abs(-34.23) = ", ex_abs)
ex_pw = pow(3, 4)
print("pow(3, 4) = " , ex_pw)
ex_cell = math.ceil(34/5)
print("ceil(34/5) = ", ex_cell)

ex_floor= math.floor(34/5)
print("floor(34/5) = ", ex_floor)
ex_maxtf = max(T,F)
print(f"max({T},{F}) = " , ex_maxtf)
ex_abscmplx = abs(4 - 3j) 
print("abs(4 - 3j) = ", ex_abscmplx)