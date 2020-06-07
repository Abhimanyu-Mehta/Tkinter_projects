from tkinter import *from tkinter import *

root = Tk()


def label_function():
    label = Label(root, text="Your text here", fg="blue")
    label.pack()


def print_statement():
    print("Your text here")


# ****** BUTTON FOR LABEL ******
button1 = Button(root, text="click me", command=label_function)
button1.pack(side="left")

# ****** BUTTON FOR PRINTING STATEMENT ******
button1 = Button(root, text="click me", command=print_statement)
button1.pack(side="left")

# ****** BUTTON TO QUIT WINDOW ******
button2 = Button(root, text="quit", command=quit)
button2.pack(side="left")

root.mainloop()

root = Tk()


def label_function():
    label = Label(root, text="Your text here", fg="blue")
    label.pack()
    
def print():
    print("Your text here")


# ****** BUTTON FOR LABEL ******
button1 = Button(root, text="click me", command=label_function)
button1.pack(side="left")

# ****** BUTTON FOR PRINTING STATEMENT ******
button1 = Button(root, text="click me", command=print)
button1.pack(side="left")


# ****** BUTTON TO QUIT WINDOW ******
button2 = Button(root, text="quit", command=quit)
button2.pack(side="left")

root.mainloop()
