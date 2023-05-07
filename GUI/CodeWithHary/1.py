from tkinter import *

box = Tk()

# "width x hight"
box.geometry("644x434") #box sizeing 

# width , hight
box.minsize(200, 100)
box.maxsize(700, 600)

# Label
sk = Label(text="Hi, I am Niladri Chatterjee. To become a GUI expart!")
sk.pack() #print sk contant

box.mainloop()