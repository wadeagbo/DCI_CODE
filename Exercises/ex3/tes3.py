# To force range starting from 1 and end at 3.
def range1(start,end):
    return range(start,end+1)



def range1(start,end):
    return range(start,end+1)


numb   = input("Enter number:    ")
nn  =   int(numb)
ncount1=0
for i in range1(1,nn):
    if nn%i==0:
        if i==2:
            print(f"{nn} is an even number")
           

        ncount1 +=1
        if ncount1 > 2:
            print(f"{nn} is NOT a prime number")
            break
            
        elif ncount1 ==2 and  i==nn:
            print(f"Yes {nn} is a prime number")
            

lst = [x for x in range1(1,nn) if nn%x==0 ]
print(lst)
