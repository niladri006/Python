
from tkinter import *


root = Tk()
root.geometry('400x330')  # width x hight
#root.iconbitmap('favicon.ico')
root.title('Listbox')

i=0
def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i += 1

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "Frist item o your listbox")


# Button label
btn_lavel = Button(root, text='Add')
btn_lavel.config(font=('verdana 10'), fg='#000080', bg='#EEEE40', padx=0, pady=0, command= add)
btn_lavel.pack()


root.mainloop()
