from tkinter import *

root = Tk()

def label_function():
    label = Label(root, text="Your text here", fg="blue")
    label.pack()

toolbar = Frame(root, bg="black")
b = Button(toolbar, text="welcome", bg="black", fg="white", command=label_function)
b.pack(side="left", padx=2, pady=2)
b1 = Button(toolbar, text="signin", bg="black", fg="white", command=label_function)
b1.pack(side="left", padx=2, pady=2)
toolbar.pack(side="top", fill="x")

root.mainloop()
