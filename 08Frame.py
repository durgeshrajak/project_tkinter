from tkinter import *
from tkinter import ttk
win = Tk()
win.title("Master")
win.geometry("800x600")
#################################

topheader = Frame(win).pack()
bottom = Frame(win).pack()

lbl = Label(topheader, text="this is header", bg="green")
lbl.pack(side=LEFT)

lbl = Label(bottom, text="this is bottom", bg="red")
lbl.pack(side=BOTTOM)
win.mainloop()