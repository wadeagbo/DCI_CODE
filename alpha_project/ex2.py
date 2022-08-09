print("Task     1")

text= "Berlin is a world city of culture, politics, media and science."
textlength= len(text)
print("The text length is:   ", textlength)


######   --------------------


print(" ")
print(" ")
print("Task     2")
firstChar =text[0]
lastChar  =text[-1]
print("The fist and the last charcter of the text are: ",  firstChar,  lastChar)


#####   --------------------


print(" ")
print(" ")
print("Task     3")
first_three_Char= text[0:3].upper()
print("The first three characters in upper case are:  " , first_three_Char)



####   --------------------


print(" ")
print(" ")
print("Task     4")
text = " Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"
targetchar = "B"
count = 0
for char in text:
    if char ==targetchar:
        count = count +1
        print(char, count)
print("The number of times B appears in text is:  " , count)




####   --------------------


print(" ")
print(" ")
print("Task     5")
text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
length_char = len(text)
last_10char= length_char-10
print(last_10char, length_char)
last_ten_char= text[last_10char:length_char]
print("The last 10 characters of the text is from:  " ,  last_ten_char)




####   --------------------


print(" ")
print(" ")
print("Task     6")

text= "---Python programming--- ."
delete_minus= text.replace("-","")
delete_dot_space = delete_minus.replace(".","").strip()
print ("New text after _'s, . and space  are deleted: " , delete_dot_space)



###   --------------------


print(" ")
print(" ")
print("Task     7")
Fname= "Waheed Adeniyi"
Lname= "ADEAGBO"
print("Firstname: " + Fname, "\n" +  "Lastname: "+ Lname)




