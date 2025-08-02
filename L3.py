from tkinter.ttk import *
from time import strftime
from tkinter import *
root =Tk()
root.title("menu bar")

menu_bar = Menu(root)

file = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file)
file.add_command(label="New",commmand = None)
file.add_command(label="open",commmand = None)
file.add_command(label="save",commmand = None)
file.add_command(label="delete",commmand = None)
file.add_separator()
file.add_command(label="Exit", command=root.quit)

next = Menu(menu_bar, tearoff=0)

edit = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Undo",commmand = None)
edit.add_command(label="Redo",commmand = None)
edit.add_separator()
edit.add_command(label="Cut",commmand = None)
edit.add_command(label="Copy",commmand = None)
edit.add_command(label="Paste",commmand = None)


# scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
#scrollbar2

scroll_bar = Scrollbar(root, orient=HORIZONTAL,activebackground= "red",bg= "blue", troughcolor="green",width=20,bd=15)
scroll_bar.pack(side= BOTTOM, fill=X)




root.config(menu=menu_bar)
mainloop()

