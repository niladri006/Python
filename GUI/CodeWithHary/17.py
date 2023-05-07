from tkinter import *


root = Tk()
root.geometry('400x330')  # width x hight
#root.iconbitmap('favicon.ico')
root.title('Status bar')

def upload():
    statusvar.set("Ready")
    import time
    time.sleep(2)
    statusvar.set("Busy...")
    
    

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor=W).pack(side=BOTTOM, fill=X)

Button(root, text="Upload", command=upload).pack()

root.mainloop()
