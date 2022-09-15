import os
import time


os.system("clear")



print("It is time for lunch. Please downlad fast")

n= 3
m= 101

for i in range(0,m,n):
    line =("."* ((m//n)-(i//n)) )
    bar = "#"*(i//n)

    full_bar = "|" + bar + line + "|" +str(i)+ "%"
    print(full_bar + "\r" , end="")
    time.sleep(0.1)
print("Congratulation! Download done"   + " "* 50 )
