import tkinter as tk

root = tk.Tk()
root.title("oscar")

root.config(bg="pink")
root.geometry("500x500")
label = tk.Label(root, text="Oscar login page",fg = "yellow", bg="pink", font=("Arial", 24))
label.pack(pady=20)

label2 = tk.Label(root, text="USERNAM",fg = "red", bg="pink", font=("Arial", 24))
label2.place(x= 10,y=100)
entry = tk.Entry(root, font=("Arial", 16))
entry.place(x=150, y=100)

label3 = tk.Label(root, text="PASSWORD",fg = "red", bg="pink", font=("Arial", 24))
label3.place(x= 10,y=150)

button = tk.Button(root, text="LOGIN", command=lambda: print("Login button clicked"), font=("Arial", 16), bg="blue", fg="white")
button.place(x=200, y=200)

root.mainloop()


