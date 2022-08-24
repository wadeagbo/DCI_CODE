user_input= input("Input the scale shortcut you'd like to convert (F - Fahrenheit  1, C - Celsius: C  2:  \n   ")


if int(user_input)==1:
    input_user_Celcius = input("Input the value of temperature you'd like to convert in Celsius  to F:    ")
    C=     input_user_Celcius = float(input_user_Celcius)
    TF =  9*C/5.0+32
    print( f"The temperature in Fahrenheit is {TF}  degrees")
elif int(user_input)== 2:
    input_user_Fahrenheit = input("Input the value of temperature you'd like to convert in Fahrenheit to C: \n   ")
    TFtemp = float(input_user_Fahrenheit)
    Ctemp = (TFtemp-32)*5/9.0
    print(f"The temperature in Celcius  is {Ctemp}  degrees")
