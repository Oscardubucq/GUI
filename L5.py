#calendar
import calendar
from tkinter import *

def show_calendar():
    root = Tk()
    root.title("Calendar")
    root.geometry("500x500")
    root.config(bg="lightblue")
    year = int(entry.get())
    cal = calendar.calendar(year)
    cal_year = Label(root,text = cal,font = ("Arial", 16), bg="lightblue", fg="black")
    cal_year.grid(row = 3,column=1, padx=10, pady=10)
    root.mainloop()
if __name__ == "__main__":
    main = Tk()
    main.config(bg="lightblue")
    main.geometry("500x500")
    cal1 = Label(main, text="Enter Year", font=("Arial", 16), bg="lightblue", fg="black")
    cal1.grid(row=1, column=1, padx=10, pady=10)
    
    entry = Entry(main, font=("Arial", 16), bg="white", fg="black")
    entry.grid(row=3, column=1, padx=10, pady=10)
    button = Button(text="Show Calendar", command=show_calendar, font=("Arial", 16), bg="blue", fg="black")
    button.grid(row=4, column=1, padx=10, pady=10)
    main.mainloop()