from tkinter import *
from tkinter import messagebox 


root = Tk()
root.geometry('500x330')  # width x hight
root.title('  Slider Tutorial')
root.iconbitmap("favicon.ico")

def getdollar():
    print(f"We have created {myslider.get()} dollars to your account")
    messagebox.showinfo("Get Dollars", f"We have created {myslider.get()} dollars to your account")

Label(root, text="How many Dollers do you want ?").pack()

myslider = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=10)
myslider.set(20)
myslider.pack(fill=X, padx=5)

btn = Button(root, text="Get Dollars!", command=getdollar)
btn.pack(pady=8)

root.mainloop()