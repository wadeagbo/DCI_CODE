T =" * "
for i in range(1,5):
    print( i*T)
for i in range(1,5):
    j = 6-i
    print(j*T)
print(T)


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return fib(n-1)+fib(n-2)

for i in range(51):
    print(i, fib(i))




from PIL import Image
myImage = Image.open("./fib.png");
myImage.show()
