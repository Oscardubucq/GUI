#progress bar
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.config(bg="pink")
root.geometry("500x500")
# root.title("Progress Bar Example")
# progress = ttk.Progressbar(root, orient="horizontal", length=100, mode="determinate")

# def bar():
#     import time
#     progress["value"] = 30
#     root.update_idletasks()
#     time.sleep(1)

#     progress["value"] = 60
#     root.update_idletasks()
#     time.sleep(1)

#     progress["value"] = 90
#     root.update_idletasks()
#     time.sleep(1)

#     progress["value"] = 100
    

   
# progress.pack(pady=20)
   

# start = tk.Button(root, text="Start Progress", command=bar)
# start.pack(pady=20)


#SPINBOX
spin  = tk.Spinbox(root, from_=0, to=10, increment=1, width=5, font=("Arial", 16),bg = "yellow", fg="black")
spin.pack(pady=20)


root.mainloop()