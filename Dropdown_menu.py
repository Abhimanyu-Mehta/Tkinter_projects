from tkinter import *

root = Tk()


def label_function():
    label = Label(root, text="Your text here", fg="blue")
    label.pack()


menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="file", menu=submenu)

submenu.add_command(label="project", command=label_function)

submenu.add_separator()

submenu.add_command(label="new project", command=label_function)

root.mainloop()
