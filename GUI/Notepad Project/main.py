from tkinter import *


root = Tk()
root.geometry('500x330')  # width x hight
root.iconbitmap('icon.ico')
root.title('Notepad')

def myfunc():
    print(f"Clicked!")
    
# <<======================= File Menu ==========================>>

def new():
    pass

def new_window():
    pass

def Open():
    pass

def save():
    pass

def save_as():
    pass
    

# <<======================= Edit Menu ==========================>>

def undo():
    text.event_generate(("<<Undo>>"))
    pass

def cut():
    text.event_generate(("<<Cut>>"))

def copy():
    text.event_generate(("<<Copy>>"))

def paste():
    text.event_generate(("<<Paste>>"))

def delete():
    pass

def find():
    pass

def fint_next():
    pass

def find_previous():
    pass

def replace():
    pass

def go_to():
    pass

def select_all():
    pass

# <<======================= Format Menu ==========================>>

def word_warp():
    pass

def font():
    pass

# <<======================= View Menu ==========================>>

def zoom_in():
    pass

def zoom_out():
    pass

def restore_default_zoom():
    pass

def status_bar():
    pass


# <<======================= Help Menu ==========================>>

def view_help():
    pass

def send_feedback():
    pass

def about_notepad():
    pass




# <<======================= Main Menu ==========================>>
mainmenu = Menu(root)

# <<======================= File Menu ==========================>>
m1 = Menu(mainmenu, tearoff=0)

m1.add_command(label="New", command=new)
m1.add_command(label="New Window", command=new_window)
m1.add_command(label="Open...", command=Open)
m1.add_command(label="Save", command=save)
m1.add_command(label="Save As...", command=save_as)
m1.add_separator()
m1.add_command(label="Exit", command=exit)


# File Menu packing
root.config(menu=mainmenu) 
mainmenu.add_cascade(label="File", menu=m1)


# <<======================= Edit Menu ==========================>>
m2 = Menu(mainmenu, tearoff=0)

m2.add_command(label="Undo", command=undo)
m2.add_separator()
m2.add_command(label="Cut", command=cut)
m2.add_command(label="Copy", command=copy)
m2.add_command(label="Paste", command=paste)
m2.add_command(label="Delete", command=delete)
m2.add_separator()
m2.add_command(label="Find...", command=find)
m2.add_command(label="Find Next", command=fint_next)
m2.add_command(label="Find Previous", command=find_previous)
m2.add_separator()
m2.add_command(label="Replace...", command=replace)
m2.add_command(label="Go To...", command=go_to)
m2.add_command(label="Select All", command=select_all)


# File Menu packing
root.config(menu=mainmenu) 
mainmenu.add_cascade(label="Edit", menu=m2)


# <<======================= Format Menu ==========================>>
m3 = Menu(mainmenu, tearoff=0)

m3.add_checkbutton(label= "Word Warp", command=word_warp)
m3.add_command(label= "Font", command=font)

# File Menu packing
root.config(menu=mainmenu) 
mainmenu.add_cascade(label="Format", menu=m3)


# <<======================= View Menu ==========================>>
m4 = Menu(mainmenu, tearoff=0)
m41 = Menu(m4, tearoff=0)

m4.add_cascade(label="Zoom", menu=m41)
m41.add_command(label="Zoom In", command=zoom_in)
m41.add_command(label="Zoom Out", command=zoom_out)
m41.add_command(label="Restore Default Zoom", command=restore_default_zoom)

m4.add_checkbutton(label= "Status Bar", command=myfunc)


# File Menu packing
root.config(menu=mainmenu) 
mainmenu.add_cascade(label="View", menu=m4)


# <<======================= Help Menu ==========================>>
m5 = Menu(mainmenu, tearoff=0)

m5.add_command(label= "View Help", command=view_help)
m5.add_command(label= "Send Feedback", command=send_feedback)
m5.add_separator()
m5.add_command(label="About Notepad", command=about_notepad)

# File Menu packing
root.config(menu=mainmenu) 
mainmenu.add_cascade(label="Help", menu=m5)

# <<======================= Text Editer ==========================>>

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT ,fill=Y)

# small note pad
text = Text(root, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH, expand=True)
scrollbar.config(command=text.yview)


root.mainloop()