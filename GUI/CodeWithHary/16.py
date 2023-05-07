from tkinter import *


root = Tk()
root.geometry('455x233')  # width x hight
#root.iconbitmap('favicon.ico')
root.title('Scrollbar tutorial')

# for connecting scrollbar to a widget
#  1. widget(yscrollcommand = scrollbar.set)
#  2. scrollbar.config(command = widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT ,fill=Y)

# listbox = Listbox(root, yscrollcommand = scrollbar.set)
# for i in range(0, 100):
#     listbox.insert(END, f"Item {i}")
# listbox.pack(fill=BOTH, padx=22, pady=10)

# scrollbar.config(command = listbox.yview)


# small note pad
text = Text(root, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)


root.mainloop()
