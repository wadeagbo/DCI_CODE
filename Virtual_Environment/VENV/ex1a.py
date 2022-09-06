# hello_world.py

import PySimpleGUI as sg

#sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()
sg.Window(title="Hello World", layout= [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]], margins=(200, 100)).read()

