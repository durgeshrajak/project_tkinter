import tkinter as tk

win = tk.Tk()

win.title("add numbers")
win.geometry("800x600")
win.config(bg="#1282e3")

def myfunc():
    num1 = float(ent.get())
    num2 = float(ent1.get())
    result = num1+num2
    return lab.config(text="Result: {:.2f}".format(result))
    # lab.config(text="Result: {:.2f}".format(result))


ent = tk.Entry(win, width=10)
ent.place(x=10,y=10)

ent1 = tk.Entry(win, width=10)
ent1.place(x=10,y=40)

btn = tk.Button(win,text="Submit" ,width=10, bg="#e312cb", command=myfunc, bd=10)
btn.place(x=10, y=80)

lab = tk.Label(win, width=20,text="Result: ")
lab.place(x=10, y=120)

win.mainloop()