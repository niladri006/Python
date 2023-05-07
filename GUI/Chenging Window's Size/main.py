from tkinter import *


root = Tk()
width1 = 300
hight1 = 230
root.geometry(f"{width1}x{hight1}")  # width x hight
root.title('Window Re-size')
root.iconbitmap('icon.ico')
root.minsize(200,200)
root.maxsize(900,900)
root.resizable(0,0)

def harry(event):
    root.geometry(f"{num1_entey.get()}x{num2_entey.get()}")
    result_label.config(text=f"Width: {num1_entey.get()} Height: {num2_entey.get()}")
    

result_label = Label(root, text=f"Width: {width1}\t Height: {hight1}")
result_label.pack(pady=5)

num1_label = Label(root, text="ENTER WIDTH: ")
num1_label.pack()
num1_entey = Entry(root)
num1_entey.pack()


num2_label = Label(root, text="ENTER HEIGHT: ")
num2_label.pack(pady=5)
num2_entey = Entry(root)
num2_entey.pack()


btn = Button(root, text="APPLY")
btn.pack(pady=5)
btn.bind('<Button-1>', harry)




root.mainloop()