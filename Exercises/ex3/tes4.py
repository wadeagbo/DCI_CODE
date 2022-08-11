user_num = int(input("Please choose a number: "))

prime = True
odd = True

for n in range (2, user_num):
    if user_num % n == 0:
        prime = False
    if user_num % 2 == 0:
        odd = False

if prime == True:
    print(f"{user_num} is a prime number")
else:
    print(f"{user_num} is not a prime number")

if odd == True and user_num != 2 and user_num !=0:
    print("Your number is odd")
else:
    print("Your number is even") 
