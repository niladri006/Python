from tkinter import *

box1 = Tk()
box1.geometry("500x400")
box1.title("Ready!")


ready = Label(text='''Ready!''', bg="green", fg="white",font=("",8, "bold"), relief="ridge", pady=2)

ready.pack(side=BOTTOM, fill=X)

box1.mainloop()
