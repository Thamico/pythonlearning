from tkinter import *
import tkinter as tk
import tkinter.messagebox as tkmb

root = Tk()
root.title('Enter height')

e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


def calculate():
    tkmb.showinfo("Your height is", str(root.get()))


def close():
    sys.exit(0)


button_calculate = Button(root, text="calculate", padx=10, pady=10, command=calculate)
button_close = Button(root, text="close", padx=20, pady=10, command=close)

button_calculate.grid(row=1, column=0)
button_close.grid(row=1, column=1)
root.mainloop()
