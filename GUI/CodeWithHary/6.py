from tkinter import *


root = Tk() 
root.geometry("655x333")
root.title("Button")

def hello():
    print("Hello tkinter button!")


frame = Frame(root, borderwidth=6, bg="gray", relief="sunken")
frame.pack(side=TOP,padx=10, pady=10, fill=X)


b1 = Button(frame, fg="red", text="Print Now", font=("Arial", 20, "bold"), command=hello)
b1.pack(side=LEFT, padx=10,pady=5)

b2 = Button(frame, fg="red", text="Print Now", font=("Arial", 20, "bold"))
b2.pack(side=LEFT, padx=10,pady=5)

b3 = Button(frame, fg="red", text="Print Now", font=("Arial", 20, "bold"))
b3.pack(side=LEFT, padx=10,pady=5)

b4 = Button(frame, fg="red", text="Print Now", font=("Arial", 20, "bold"))
b4.pack(side=LEFT, padx=10,pady=5)

root.mainloop()