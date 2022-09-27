import time

counter = int(input("Enter a counter number: "))
timeS = time.time()


for i in range(1, counter+1):
    print(i)
    time .sleep(1)

timeE = time.time()
print("COUNTER DONE")
time.sleep(1)
print("Start   :  " +str(time.ctime(timeS)) )
print("End     :  " +str(time.ctime(timeS)) )

print("Counter of    :  " +str(counter)  +  "  was chosen.")



