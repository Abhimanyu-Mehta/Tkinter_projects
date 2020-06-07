from tkinter import *

root = Tk()

Label(root, text="First Name").grid(row=0)
Label(root, text="Last Name").grid(row=2)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=1, column=1)
e2.grid(row=3, column=1)

# ***** CHEAK BOX *****

c = Checkbutton(root, text="Your text here")
c.grid(columnspan=2)

root.mainloop()
