from tkinter import *

root = Tk()

label = Label(root, text="Your text here", fg="blue")
label.pack()

label1 = Label(root, text="Your text here", fg="pink", bg="black")
label1.pack(side="left")
root.mainloop()
