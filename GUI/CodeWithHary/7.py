from tkinter import *


root = Tk()
# "width x hight"
root.geometry("255x133")
root.title()

user = Label(root, text="Username  ", padx=15, pady=15)
password = Label(root, text="Password", padx=15)

user.grid()
password.grid()

# Different types of Variable class in tkinter =>>   BooleanVar, DoubleVar, IntVar, StringVar 

userValue = StringVar()
passValue = StringVar()


userEntry = Entry(root, textvariable = userValue)
passEntry = Entry(root, textvariable = passValue)


userEntry.grid(row=0, column=1)
passEntry.grid(row=1, column=1)

# Commend function
def getVals():
    print(f"Username: {userValue.get()}         Password: {passValue.get()}")

# Button
Button(text="Submit", borderwidth=3, command=getVals).grid(row=3, column=1, pady=10)

root.mainloop()