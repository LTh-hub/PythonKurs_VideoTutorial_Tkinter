# buttons.py
#
# YouTube :: Python GUI's With Tkinter
#            CODEMY.COM - Learn to code
#
# 1) Create Graphical User Interface with Python and Tkinter
# 2) Positioning WithTkinter Grid System - Python Tkinter GUI #2
# 3) Creating Buttons With Tkinter - Python Tkinter GUI #3
#
#
from tkinter import *

root = Tk()
root.title("Learn to Code")
root.geometry("300x350")


def myClick():
    myLabel = Label(root, text="Look, I clicked a button!!")
    myLabel.pack()



myButton1 = Button(root, text="1 - Click me!")
myButton1.pack()

myButton2 = Button(root, text="2 - Click me!", state=DISABLED)
myButton2.pack()

myButton3 = Button(root, text="3 - Click me!", padx=50, pady=15)
myButton3.pack()


myButton = Button(root, text=" - Click me!", command=myClick, fg="blue", bg="white")
myButton.pack()






root.mainloop()





