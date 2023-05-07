from tkinter import *
from PIL import Image, ImageTk

mahmdul_root = Tk()

mahmdul_root.geometry("455x244")

# for Jpg Images
image = Image.open("1.png")
photo = ImageTk.PhotoImage(image)

varun_label = Label(image=photo)
varun_label.pack()

mahmdul_root.mainloop()

# <=======================================================================>

# from tkinter import *


# root = Tk()
# # width x hight
# root.geometry('495x280')
# root.title('ttt')

# wallpaper = PhotoImage(file="1.png")
# label = Label(image=wallpaper)
# label.pack()

# root.mainloop()