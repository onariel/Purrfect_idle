from tkinter import *
from tkinter.ttk import *
root = Tk()
frm = Frame(root, padding=10)
frm.grid()
Label(frm, text="Hello World!").grid(column=0, row=0)
Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()