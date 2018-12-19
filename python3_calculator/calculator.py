from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Calculator")

bttn_list = [
    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "+/-", "C",
    "0", ".", "="
]

def calc(key):
    global memory
    if key == '=':
        str1 = "-+1234567890.*/"
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "The first char is Not Digit!")
            messagebox.showerror("Error!", "You have been entered not a digit!")
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the data!")

    elif key == 'C':
        calc_entry.delete(0, END)
    elif key == '+/-':
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == '-':
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, '-')
        except IndexError:
            pass
    else:
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

r = 1
c = 0

for i in bttn_list:
    rel = ""
    cmd = lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width=35)
calc_entry.grid(row=0, column=0, columnspan=5)

root.mainloop()
