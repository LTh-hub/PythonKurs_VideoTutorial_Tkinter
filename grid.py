# grid.py
#
# YouTube :: Python GUI's With Tkinter
#            CODEMY.COM - Learn to code
#
# 1) Create Graphical User Interface with Python and Tkinter
# 2) Positioning WithTkinter Grid System - Python Tkinter GUI #2
#
from tkinter import *

root = Tk()

# Create a Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Lars")
myLabel3 = Label(root, text="                      ")


# Shoving it to screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)



myLabel1 = Label(root, text="Hello World!").grid(row=2, column=0)
myLabel2 = Label(root, text="My name is Lars").grid(row=3, column=5)



root.mainloop()





