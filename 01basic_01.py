# import tkinter as tk

# win = tk.Tk()

# win.mainloop()

############################################
# giving title
############################################
# import tkinter as tk

# win = tk.Tk()
# win.title("first window")

# win.mainloop()
############################################
# useing icon facvicon (iso file ki jarurat hoti h.)
############################################
import tkinter as tk

win = tk.Tk()
win.title("first window")
win.iconbitmap("wolf-48_46777.ico")
win.configure(bg="#FFFF00") # To change the background color of a Tkinter window, you can use the configure method along with the bg (background) parameter. Here's an example:
# win.maxsize(width=1000,height=1000) # giving window size (beech bala squre click karne par ye bada max size pakdega)
# win.minsize(width=600,height=600)  # giving window size (bydefault minsize pakadega)
##########################################
win.geometry("300x400") # (is tarike se karane par beech bale squere button click karne par puri windo ka size le lega)

win.mainloop()
