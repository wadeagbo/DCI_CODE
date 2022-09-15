import sys


choice = sys.argv[2]
num1 = int(sys.argv[1])
num2 = int(sys.argv[3])

if choice=="+":
    print(num1+num2)
elif choice=="-":
    print(num1-num2)
elif choice=="x":
    print(num1 * num2)
