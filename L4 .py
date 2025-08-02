from tkinter.ttk import *
from time import strftime
from tkinter import *
root =Tk()
root.title("frames and listbox")


# frames
frame_1= Frame(root, width=500, height=500, bg="blue")
frame_1.pack(side=LEFT, expand=True)


#listbox
Listbox_1 = Listbox(frame_1, width=20, height=10, bg="yellow", fg="black", font=("Arial", 16))

Listbox_1.pack(pady=20)
Listbox_1.insert(1, "Oscar")
Listbox_1.insert(2, "aarshi")
Listbox_1.insert(3, "sahil")
Listbox_1.insert(4, "clément")
Listbox_1.insert(5, "sarah")
Listbox_1.insert(6, "alexandre")
Listbox_1.insert(7, "gabriel")
Listbox_1.insert(8, "noah")
Listbox_1.insert(9, "matteo")


mainloop()