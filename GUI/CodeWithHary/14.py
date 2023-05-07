from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry('400x230')  # width x hight
root.iconbitmap('favicon.ico')
root.title('Radio Button')

def getorder():
    messagebox.showinfo("Radio button", f"Your order {var.get()} has been record")

var = StringVar()
var.set("rosa")

label1 = Label(root, text="What whould you like to have sir ?")
label1.config(font='lucida 15 bold', justify=LEFT, padx=14)
label1.pack()

radio = Radiobutton(root, text="Dosa", padx=14, variable= var, value="Dosa").pack(anchor=W, side=TOP)
radio = Radiobutton(root, text="Idly", padx=14, variable= var, value="Idly").pack(anchor=W)
radio = Radiobutton(root, text="Paratha", padx=14, variable= var, value="Paratha").pack(anchor=W)
radio = Radiobutton(root, text="Samosa", padx=14, variable= var, value="Samosa").pack(anchor=W)



btn_lavel = Button(root, text='ORDER')
btn_lavel.config(font=('verdana 10'), fg='#000080', bg='#EEEE40', padx=0, pady=0, command=getorder)
btn_lavel.pack()






root.mainloop()
