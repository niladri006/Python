from tkinter import *


root = Tk()
root.geometry('772x654+350+50')  # width x hight
root.title('Mylogin')
root.configure(bg='#2D2929')
root.resizable(0,0)


wellcome=Label(root,text='Wellcome', fg='#FFFFFF', bg='#2D2929', font=('Inter', 52))
wellcome.place(x=267, y=48)


wellcome=Label(root,text='Username:', fg='#FFFFFF', bg='#2D2929', font=('Inter', 31))
wellcome.place(x=100, y=234)

user_entry=PhotoImage(file='Rectangle 3.png')
Label(root, image=user_entry).place(x=330, y=237)



root.mainloop()