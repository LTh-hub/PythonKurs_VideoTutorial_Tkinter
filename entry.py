# entry.py
#
# YouTube :: Python GUI's With Tkinter
#            CODEMY.COM - Learn to code
#
# 1) Create Graphical User Interface with Python and Tkinter
# 2) Positioning WithTkinter Grid System - Python Tkinter GUI #2
# 3) Creating Buttons With Tkinter - Python Tkinter GUI #3
# 4) Creating Input Fields With Tkinter - Python Tkinter GUI #4
#
#
from tkinter import *

root = Tk()
root.title("Learn to Code")
root.geometry("500x350")


e = Entry(root, width=50)
e.pack(pady=10)


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Ange ditt namn", command=myClick, fg="blue", bg="white")
myButton.pack()






root.mainloop()





