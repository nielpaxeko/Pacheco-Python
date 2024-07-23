from tkinter import *

window = Tk()
window.title("Mile to KM")
window.config(padx=20, pady=20)

def convert():
    miles = float(input.get())
    kms = round((1.609 * miles), 2)
    answer.config(text=f"{kms}") 

input = Entry(width=7)
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=1)

is_equal_to_label = Label(text="Is equal to ")
is_equal_to_label.grid(column=0, row=1)

answer = Label(text="0")
answer.grid(column=1, row=1)

km_label = Label(text="Kilometers")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()