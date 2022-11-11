from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('Silly Clock')



def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("DS-Digital", 70), background='black', foreground="pink")
label.pack(anchor="center")

time()
mainloop()
    