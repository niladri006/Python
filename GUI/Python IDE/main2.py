from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import os

root = Tk()
root.title('Python IDLE')
root.geometry('1280x720+150+40')
root.configure(bg='#323846')
root.resizable(False,False)

file_path=''

def set_file_path(path):
    global file_path
    file_path = path

def open_file():
    path = askopenfilename(filetypes=[('Python Files','.py')])
    with open(path, 'r') as file:
        code = file.read()
        code_input.delete('1.0', END)
        code_input.insert('1.0', code)
        set_file_path(path)
        
        
def save():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files','.py')])
    else:
        path = file_path
    with open(path,'w') as file:
        code=code_input.get('1.0',END)
        file.write(code)
        set_file_path(path)
        

def run():
    if file_path == "":
        messagebox.showerror('Python IDLE', 'Save your code')
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error=process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)



#icon
image_icon = PhotoImage(file='logo.png')
root.iconphoto(False, image_icon)

#code input
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT ,fill=Y)
code_input = Text(root, font='consolas 18', yscrollcommand=scrollbar.set)
code_input.place(x=10, y=5, width=1250, height=550)
scrollbar.config(command=code_input.yview)

#code output
code_output = Text(root, font='consolas 18', bg='#323846', fg='lightgreen')
code_output.place(x=10, y=580, width=1250, height=100)

mainmenu = Menu(root)
mainmenu.add_command(label='Open File', command=open_file)
mainmenu.add_command(label='Save', command=save)
mainmenu.add_command(label='Run', command=run)
root.config(menu=mainmenu)

root.mainloop()

