from tkinter import *
 
def add():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    result = num1 + num2
    result_label.config(text=result)
 
# create the main window
root = Tk()
root.title("SUM")
root.geometry("250x155")
root.iconbitmap('favicon.ico')
 
# create the widgets
num1_label = Label(root, text="Number 1:", padx=10,pady=10)
num1_entry = Entry(root)
num2_label = Label(root, text="Number 2:", padx=10, pady=10)
num2_entry = Entry(root)
add_button = Button(root, text="Add", command=add, padx=5)
result_label = Label(root, text="Result:")
 
# layout the widgets
num1_label.grid(row=1, column=0)
num1_entry.grid(row=1, column=1)

num2_label.grid(row=2, column=0)
num2_entry.grid(row=2, column=1)

add_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label.grid(row=4, column=0, columnspan=2)
 
# run the main loop
root.mainloop()