from tkinter import *
from tkinter import ttk
win = Tk()
win.title("Master")
win.geometry("800x600")

var = StringVar()

com = ttk.Combobox(win, width=27, textvariable=var)
com['state'] = 'readonly'
com['values'] = ('jan','fab','march','apr')
com.current(0)
com.place(x=10,y=20)

win.mainloop()
