print("Task     1")
city= "London"
print(city)

####----------------------------------------------------------

print(" ")
print(" ")
print("Task     2")

city = "berlin"
population =3645000
#print(city.capitalize()+":"+ str(population))
print(city.capitalize(),":", population)


####----------------------------------------------------------


print(" ")
print(" ")
print("Task     3")


w = input("Input the city name in small letter:    ")
city = w
#city="london"
population=9000000 
#Tr ="TRUE"
if city=="london":
    Tr ="TRUE"
    print("City: ", city.capitalize(), "("+Tr +")")
    print("Population: ",  population) 
else:
    print("City is not london  on in capital L but ",  city) 

####------------------------------------------------------------
print(" ")
print(" ")
print("Task     4")


text= "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
texfind= text.find('capital')
print("capital: ", texfind)

####--------------------------------------------------------------
print(" ")
print(" ")
print("Task     5")




text= "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau. "
textsplit = text.split()
print(textsplit)
#print(text.split())


####------------------------------------------------

print(" ")
print(" ")
print("Task     6")


text= "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital.  "
textreplace= text.replace("capital", "capital of Germany")
print(textreplace)
