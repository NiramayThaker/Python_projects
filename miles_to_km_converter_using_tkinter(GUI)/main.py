from tkinter import *


def miles_to_km():
    new_label = Label(text=float(input_box.get())*1.609, font=("Arial", 12, "bold"))
    new_label.grid(column=3, row=2)


window = Tk()
window.title("Miles To Kilometer converter")
window.minsize(330, 150)
window.config(padx=30, pady=30)

# Entry
input_box = Entry(width=10)
input_box.grid(column=1, row=1)

# Label for miles
mile_label = Label(text="miles", font=("Arial", 12))
mile_label.grid(column=3, row=1)

# Label for equal to
eqaul_to_label = Label(text="is equal to", font=("Arial", 12))
eqaul_to_label.grid(column=1, row=2)

# Label for Kilometer
km_label = Label(text="km", font=("Arial", 12, "bold"))
km_label.config(text="km")
km_label.grid(column=4, row=2)

# button
button = Button(text="Convert", command=miles_to_km)
button.grid(column=1, row=4)

window.mainloop()
