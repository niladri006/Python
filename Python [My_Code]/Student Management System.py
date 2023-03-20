from logging import root
from tkinter import *
from turtle import title
class Student:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        


root=Tk()
ob=Student(root)
root.mainloop()