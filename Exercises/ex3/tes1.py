nr = int(input("Enter number of arguments in range() function:   "))
for n in range(1,nr):
    if n==1:
        ns   = input("Enter starting number:   ")
        nst  = int(ns)
        ne   = input("Enter stopping number:   ")
        ned  = int(ne)
        ste  = input("Enter step:   ")
        step = int(ste)

        lst1 ={x  for x in list(range(nst,ned, step))}
#        for  x in range(nst,ned,step):
        print(lst1)


