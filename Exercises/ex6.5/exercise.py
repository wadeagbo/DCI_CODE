'''
#STORY PROGRAM

"""This program should take user input() and based on the choice
the user made change the course of the story.

For example:

print("You are in a dark alley. Where do you go?")
print("(1) left (2) straight (3) right")
choice = input("choose: ")

if choice == "1":
   print("u go left and die")
elif choice == "2":
   print("u go straight and there is another crossing")
   #continue tree here
elif choice == "3":
   print("u go right and theres a wall")
else:
   print("u just die for inaction")

'''



from tprint import tprint


data = {
    "a": (100, 2, 3, 4),
    "b": (1, 200, 3, 4),
    "c": (1, 2, 300, 4),
    "d": (1, 2, 3, 400),
}



Choice = int(input("You are in a dark alley. Where do you go?   Choose (1) left (2) straight (3) right (4  to get another chance)  safe any number     "))

if Choice==1:
   print("u go left and die")
elif Choice==2:
   print("u go straight and there is another crossing")
elif Choice==3:
   print("u go right and theres a wall")
elif Choice==4:
   print("u just die for in action")
   Choice_2 = int(input("You are have another choice. Choose 5 if you want to run "))
   if Choice_2 ==5:
      print("Run and print data for me")
      print()
      tprint(data)
else:
   print("You are lucky that you are safe")




