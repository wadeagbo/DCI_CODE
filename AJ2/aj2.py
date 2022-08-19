import os
import datetime
from   colorama                          import * # optional
from   art                               import * # optional

# initializing colorama
init()

# datetime variable
now        = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")


print(Fore.LIGHTCYAN_EX+"")
tprint("AWESOME JOURNAL", font="random") # displaying wonderful title
print(""+Style.RESET_ALL)

# display current journal
new_entry = input("ENTER DIARY ENTRY HERE >>> ")

here = os.getcwd().replace("\\","/") # defining path variable for later if statement

if here.upper() in new_entry.upper(): # if weird path bug, dont save
    print("")
elif new_entry != "": # if entry is not empty, save entry
    with open("journal.txt", "a") as file:
        file.write(now + " " + new_entry + "\n")
else:
    print("Empty string. NOT ADDING.") # if entry empty, dont save
