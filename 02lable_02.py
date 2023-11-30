# label , grid, place, pack

import tkinter as tk

win = tk.Tk()
win.maxsize(width=1000,height=1000) # giving window size (beech bala squre click karne par ye bada max size pakdega)
win.minsize(width=600,height=600)

lbl = tk.Label(win, text="label 1")
lbl1 = tk.Label(win, text="label 2", bg="red", fg="white", width=10, height=10,font="arial") # ye sab lable me le sakte hai
# lbl.pack() # ye autometically kahi bhi out but kahi bhi deta hai
#######################################
# lbl.grid() #conrner par deta h lable
# lbl.grid(row=3,column=4) # row colomn bhi de sakte hai (bade project me use hota hai)
lbl.place(x=19,y=12)
lbl1.place(x=78,y=90)# sase jyad yahi use hota hai


win.mainloop()
