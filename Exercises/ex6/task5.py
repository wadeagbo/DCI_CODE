x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x ==y or y == z or x==z:
    result = 0
    print("Calculated sum is ", result)

else:
    sum = x + y + z
    print(f"Calculated sum is   ", sum)
