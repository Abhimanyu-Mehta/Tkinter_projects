from tkinter import *

root = Tk()


def label_function():
    label = Label(root, text="Your text here", fg="blue")
    label.pack()


STATUS = Label(root, text="the actual thing starts from here....", bd=1, relief=SUNKEN, anchor="e")
bu = Button(STATUS, text="button", command=label_function)
bu.pack(side="left")
STATUS.pack(side="bottom", fill="x")

root.mainloop()
