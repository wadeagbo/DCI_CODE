import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format


import time
import PySimpleGUI as sg

from   colorama                          import * # optional
from   art                               import * # optional

# initializing colorama

#sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()
#sg.Window(title="Hello World", layout=[[]], margins=(200, 100)).read()



def step_print(string): # creating a function for printing the menu in a more stylish way
#    sg.Window(title=string, layout=[[]], margins=(200, 100)).read()
    cprint(figlet_format(string, font='starwars'), 'yellow', 'on_red', attrs=['bold'])   
    # OPTIONAL: you could add sound effects with the vlc library here
    time.sleep(0.1) # time sleep function to pause the program for a splitsecond so the menu experience is better




main_loop = True # main loop for main menu



while main_loop == True:
    step_print("#################")
    step_print("#               #")
    step_print("#               #")
    step_print("# W E L C O M E #")
    step_print("#               #")
    step_print("#               #")
    step_print("#################")
    step_print("(1) Menu1 (2) Menu2 (3) Exit")
    choice = input("Choose: ")
    if   choice == "1":
        step_print("You chose 1")
        #now menu1 somehow...
    elif choice == "2":
        step_print("You chose 2")
        #now menu2 somehow...
    elif choice == "3":
        step_print("You chose 3")
        main_loop = False
    else:
        step_print("Invalid Input")
