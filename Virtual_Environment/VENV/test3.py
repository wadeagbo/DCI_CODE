from tkinter  import *

def printSomething():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(root, text= "Hey whatsup bro, i am doing something very interresting.")
    #this creates a new label to the GUI
    label.pack() 

root = Tk()

button = Button(root, text="Print Me", command=printSomething) 
button.pack()

root.mainloop()
