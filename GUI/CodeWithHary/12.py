from tkinter import *
import tkinter.messagebox as mb


root = Tk()
root.geometry('600x430')  # width x hight
root.title('VS Code')

def myfunc():
    print("Clicked!")
    
def help():
    print("I will help you")
    mb.showinfo("This", "Harry will help you with this gui")
    
def rate():
    print("Rate Us")
    value=mb.askquestion("Rate Us", "How Good your experience ?")
    if value == "yes":
        mb.showinfo("Rate Us","Grate. Rate us on appstore please")
    else:
        mb.showinfo("Rate Us","Tell us what wrong. We will call you soon")
    
    

# <<======================= Main Menu ==========================>>
mainmenu = Menu(root)


# <<======================= File Menu ==========================>>
m1 = Menu(mainmenu, tearoff=0)

m1.add_command(label="New Text File", command=myfunc)
m1.add_command(label="New File", command=myfunc)
m1.add_command(label="New Window", command=myfunc)
m1.add_separator()
m1.add_command(label="Open File", command=myfunc)
m1.add_command(label="Open Folder", command=myfunc)
m1.add_command(label="Open Workspace from file", command=myfunc)
m1.add_command(label="Open Resent", command=myfunc)
m1.add_separator()
m1.add_command(label="Add Folder to Workspace", command=myfunc)
m1.add_command(label="Save Workspace As", command=myfunc)
m1.add_command(label="Duplicate Workspace", command=myfunc)
m1.add_separator()
m1.add_command(label="Save", command=myfunc)
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Save All", command=myfunc)
m1.add_separator()
m1.add_command(label="Share", command=myfunc)
m1.add_separator()
m1.add_command(label="Auto Save", command=myfunc)
m1.add_command(label="Preferencs", command=myfunc)

# File Menu packing
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)


# <<======================= Edit Menu ==========================>
m2 = Menu(mainmenu, tearoff=0)

m2.add_command(label="Undo", command=myfunc)
m2.add_command(label="Redo", command=myfunc)
m2.add_separator()
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_command(label="Paste", command=myfunc)
m2.add_separator()
m2.add_command(label="Find", command=myfunc)
m2.add_command(label="Replace", command=myfunc)
m2.add_separator()
m2.add_command(label="Find in Files", command=myfunc)
m2.add_command(label="Replace in Flies", command=myfunc)
m2.add_separator()
m2.add_command(label="Toggle Line Comment", command=myfunc)
m2.add_command(label="Toggle Block Comment", command=myfunc)
m2.add_command(label="Emmet: Expand Abbreviation", command=myfunc)

# Edit Menu packing
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)


# <<======================= Help Menu ==========================>
m3 = Menu(mainmenu, tearoff=0)

m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=rate)

# Help Menu packing
root.config(menu=mainmenu)
mainmenu.add_cascade(label="About Us", menu=m3)


# <<=======================  ==========================>


root.mainloop()

