# entry bao and button

import tkinter as tk

win = tk.Tk()
win.title("first window")
win.iconbitmap("wolf-48_46777.ico")

############################# create function #############################
def func():
    x = var.get()
    con.config(text=x )

win.configure(bg="#FFFF00") # To change the background color of a Tkinter window, you can use the configure method along with the bg (background) parameter. Here's an example:

win.maxsize(width=1000,height=1000) # giving window size (beech bala squre click karne par ye bada max size pakdega)
win.minsize(width=600,height=600)


lbl = tk.Label(win,text= "User name", bg="#03f4fc", fg="red", font=("Arial", 12))
lbl.place(x=10, y=100)

con = "StringVar"
lbl = tk.Label(win,text= "nothing", bg="#03f4fc", fg="red", font=("Arial", 12), textvariable=con)
lbl.place(x=10, y=10)

# entry box or input box
var = "StringVar"
ent = tk.Entry(win, bg='yellow', fg='white',font=("Arial", 12), textvariable=var )
ent.place(x=100, y=10)

# BUTTON 
btn = tk.Button(win, text="Submit", bg="#32a89e",command=func)
btn.place(x=40, y=80)

win.mainloop()