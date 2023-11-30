from tkinter import *
from tkinter import ttk
win = Tk()
win.title("Master")
win.geometry("800x600")
################################
def func():
    lst.delete(ANCHOR)
    
lst = Listbox(win,width=20)
items = ['Apple','Banana',"etc"]
for i in items:
    lst.insert(END,i)
# lst.insert(END,"apple") # good way
##################### for deleteing#######

btn = Button(win, text="Delete", command=func).pack()

lst.pack()



###################################
win.mainloop()