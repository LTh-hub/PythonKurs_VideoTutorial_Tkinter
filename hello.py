# hello.py
#
# YouTube :: Python GUI's With Tkinter
#            CODEMY.COM - Learn to code
#
# 1) Create Graphical User Interface with Python and Tkinter
#   
#
from tkinter import *

root = Tk()

# Create a Label Widget
myLabel = Label(root, text="Hello World!")

# Shoving it to screen
myLabel.pack(pady=10)


root.mainloop()

