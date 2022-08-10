# To force range starting from 1 and end at 3.
def range1(start,end):
    return range(start,end+1)

numb   = input("Enter number:    ")
nn  =   int(numb)
for i in range1(1,nn):
    if nn%i==0:
        print(i)
lst = [x for x in range1(1,nn) if nn%x==0 ]
print(lst)




numb   = input("Enter number:    ")
nn  =   int(numb)
ncount = 0
for i in range1(1,nn):
    if nn%i==0 :
            ncount +=1
            if(ncount<3):
                print("prime numbers: ", i)
            elif(ncount>3):
                print("not prime numbers: ", i)

lst = [x for x in range1(1,nn) if nn%x==0 ]
print(lst)

