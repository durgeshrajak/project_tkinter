from tkinter import *
from tkinter import messagebox
win = Tk()
win.title("Master")
win.geometry("800x600")
################################

def func():
    if var.get() == "":
        messagebox.showwarning("Warning","Empty Box")
    else:
        # messagebox.showinfo("Success", var.get())   
        messagebox.askyesno('Title','Do you want to Exit')

var = StringVar()
ent = Entry(win, textvariable=var).pack()

btn = Button(win, text="Click me", command=func).pack()





###################################
win.mainloop()