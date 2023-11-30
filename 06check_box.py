from tkinter import *
from tkinter import ttk
win = Tk()
win.title("Master")
win.geometry("800x600")

def func():
    print(Checkbtn1.get())
    print(Checkbtn2.get())
Checkbtn1 = IntVar()
Checkbtn2 = IntVar()

select = Checkbutton(win, text="Male", variable=Checkbtn1,onvalue=1, offvalue=0)
select.place(x=10, y=10)

select = Checkbutton(win, text="female", variable=Checkbtn2,onvalue=1, offvalue=0)
select.place(x=10, y=40)

btn = Button(win,text="Get data", command=func)
btn.pack()

win.mainloop()