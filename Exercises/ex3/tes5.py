numb   = input("Enter number:    ")
nn  =   int(numb)

prime = True
odd   = True

for i  in range(2,nn):
    if  nn%i==0:
        prime = False

if nn%2==0:
    odd  = False


if prime==True:
    print(f"{nn}  is a prime number")
else: 
    print(f"{nn}  is not  prime number")

if odd ==True:
    print(f"{nn}  is odd  number")
else:
    print(f"{nn}  is even  number")


print([x for x in range(1,nn+1) if nn%x==0 ])

