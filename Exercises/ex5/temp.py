T1= int(input("Input the scale shortcut you'd like to convert (F - Fahrenheit  1, C - Celsius: C  2:     "))

if T1==1:
    C = float(input("Input the value of temperature you'd like to convert in Celsius  to F:    "))
    TF =  9*C/5.0+32#
    print( f"The temperature in Fahrenheit is {TF}  degrees")
elif T1== 2:
    TF = float(input("Input the value of temperature you'd like to convert in Fahrenheit to C:    "))
    Ct =(TF-32)*5/9.0
    print( f"The temperature in Celcius is {Ct}  degrees")
