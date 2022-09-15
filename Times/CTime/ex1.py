import time 

x= time.time()              # current time in seconds since unix epoch
y= time.ctime(x)            # x converted to human readable time format

z= time.ctime(1)            # one second more (to 1970)

print(x)

time.sleep(1)                #  pauses exeecuation  of program for x seconds (1)
print(y)

print(z)

