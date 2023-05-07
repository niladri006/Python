from tkinter import *
# from tkinter import Tk, Menu


root = Tk()
root.geometry('400x430')  # width x hight
root.title('VS Code')

def myfunc():
    print("Clicked!")
    

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




root.mainloop()

