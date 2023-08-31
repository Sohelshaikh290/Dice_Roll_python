from tkinter import *
import random

window = Tk()

def roll():   # This is a blank function
    pass

window.minsize(600,600)   # for setting the minimum width and height for our window
window.maxsize(600,600)   # for setting the maximum width and height for our window  
window.title('ROLL THE DICE')  # for giving title to our window

# This will create a label which will contain heading
heading = Label(window,text='ROLL THE DICE',font=('bold',50),bg='light cyan')
heading.pack(fill=X)

# This will create a button.
button = Button(window,text='Roll',font=('normal',25),command=lambda:roll())
button.pack()

window.mainloop()
