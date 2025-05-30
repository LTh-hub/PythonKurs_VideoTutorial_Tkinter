# images.py
#
# YouTube :: Python GUI's With Tkinter
#            CODEMY.COM - Learn to code
#
# 1) Create Graphical User Interface with Python and Tkinter
# 2) Positioning WithTkinter Grid System - Python Tkinter GUI #2
# 3) Creating Buttons With Tkinter - Python Tkinter GUI #3
# 4) Creating Input Fields With Tkinter - Python Tkinter GUI #4
# 5) Build a Simple Calculator App - Python Tkinter GUI #5
# 6) Continuing Build a Simple Calculator App - Python Tkinter GUI #6
# 7) Finish Build a Simple Calculator App - Python Tkinter GUI #7
# 8) Using Icons, Images, and Exit Buttons - Python Tkinter GUI #8
#
#
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learn to Code at Codemy.com")
#root.geometry("500x350")
root.iconbitmap('static/codemy105a_2.ico')      # Codemy's ikon


my_img = ImageTk.PhotoImage(Image.open("static/Skärmbild_Lama.png"))
my_label = Label(image=my_img)
my_label.pack()






button_quit = Button(root, text="Exit the program", command=root.quit)
button_quit.pack(pady=10)




root.mainloop()
