import os
from time import sleep

for i in range(11):
    sleep(.5)
    print("*"*i +  "" +  str(i), "%")
    sleep(.1)
    os.system("clear")
