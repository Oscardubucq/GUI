from tkinter import *
import tkinter.font as font

def convert():
    temp_celcius = celcius_value.get()
    temp_fahrenheit = (float(temp_celcius) * 9/5) + 32

    output_fahrenheit.config(text=f"Temperature in Fahrenheit: {temp_fahrenheit:.2f} °F")

root = Tk()
root.title("Temperature Converter")
root.config(bg="lightblue")
root.geometry("400x300")

heading = Label(root, text="Celcius to Fahrenheit Converter", font=("Arial", 18), bg="lightblue", fg="black")
heading.pack(pady=20)   

celcius_label = Label(root, text="Enter Temperature in Celcius:", font=("Arial", 16), bg="lightblue", fg="black")
celcius_label.pack(pady=10)

celcius_value = Entry(root, font=("Arial", 16), bg="white", fg="black")
celcius_value.pack(pady=10)

convert_button = Button(root, text="Convert", command=convert, font=("Arial", 16), bg="blue", fg="black")
convert_button.pack(pady=10)

output_fahrenheit = Label(root, text="Temperature in Fahrenheit: ", font=("Arial", 16), bg="lightblue", fg="black")
output_fahrenheit.pack(pady=10)
root.mainloop()



