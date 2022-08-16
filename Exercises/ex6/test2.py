x = float(input("First number: "))
y = float(input("Second number: "))

if x % y== 0:print("First number is divisible by second number, result =", y/x)
elif y % x == 0:print("Second number is divisible by first number, result =", y/x)
else:print("Numbers are non-divisable!")

