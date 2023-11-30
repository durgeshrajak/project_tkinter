from tkinter import *
from tkinter import ttk
win = Tk()
win.title("Master")
win.geometry("800x600")

def func():
    print(var.get())
var = IntVar()


radio = Radiobutton(win,text="Male",value=0,variable=var    ).pack()
radio = Radiobutton(win,text="Female",value=1,variable=var).pack()

btn = Button(win,text="Submit",command=func).pack()
win.mainloop()