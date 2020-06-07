
import tkinter.messagebox

# ****** ASKING YES/NO QUESTION ******

answer = tkinter.messagebox.askquestion('TITLE', 'CONTENT')
if answer == 'yes':

    #****** SHOWING TEXT ******
    
    tkinter.messagebox.showinfo('TITLE', 'CONTENT')
    print("we will play together at 3pm")
    
    # ****** ASKING YES/NO QUESTION ******
    
    answer2 = tkinter.messagebox.askquestion('TITLE', 'CONTENT')
    if answer2 == 'yes':
        print("TEXT")
    else:
        print("TEXT")
else:
    print("TEXT")
