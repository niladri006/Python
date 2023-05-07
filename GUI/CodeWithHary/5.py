from tkinter import *
root = Tk()
root.geometry("655x333")
root.title("VS Code")

f1 = Frame(root, bg="gray", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)

l = Label(f1, text="project Thinter", bg="gray", fg="white",font=("Arial",10, "bold"))
l.pack(pady=3, fill=X)

# <<----------------------------------------------------------->>


f2 = Frame(root, borderwidth=8, bg="gray", relief=SUNKEN)
f2.pack(side=TOP, fill=X)

l= Label(f2, text="Wellcome to VS code", bg="gray", fg="white",font=("Arial",10, "bold"), pady=4)
l.pack(fill=X)


root.mainloop()

