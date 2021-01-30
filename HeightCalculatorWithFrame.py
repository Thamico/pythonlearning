from tkinter import *
import tkinter as tk

from tkinter import ttk, messagebox

root = Tk()
root.title('Enter height')

e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

info = StringVar()
entry_1 = Entry(root, textvariable=info)


def calculate():
    popup = tk.Tk()
    popup.wm_title("Your height is:")
    label = ttk.Label(popup, text=e.get(), font=NORM_FONT)
    label.pack(side="top", fill="x", padx=100, pady=25)
    b1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    b1.pack()
    popup.mainloop()


def close():
    sys.exit(0)


button_calculate = Button(root, text="calculate", padx=10, pady=10, command=calculate)
button_close = Button(root, text="close", padx=20, pady=10, command=close)

button_calculate.grid(row=1, column=0)
button_close.grid(row=1, column=1)
root.mainloop()
