from tkinter import *

BROWN = 845460


# To SAVE PASSWORD 
def save_password():
    website_data = website_entry.get()
    email_username_data = email_username_entry.get()
    password_data = password_entry.get()
    with open("./data.txt", mode="w") as save_data:
        save_data.write(f'Website -> {website_data}\n')
        save_data.write(f'Email ID or username -> {email_username_data}\n')
        save_data.write(f'Password -> {password_data}\n')


# GUI SETUP

window = Tk()
window.title("Password manager")
window.config(padx=80, pady=80, bg="Black")

canvas = Canvas(width=200, height=224, highlightthickness=0, bg="Black")
lock_photo = PhotoImage(file="./logo.png")
canvas.create_image(110, 112, image=lock_photo)
canvas.grid(column=1, row=1)

website_label = Label(text="Website:", font=("Arial", 12), bg="Black", fg="White")
website_label.grid(column=0, row=3)
website_entry = Entry(width=53, bg="Grey", fg="white")
website_entry.grid(column=1, row=3, columnspan=2)

email_username = Label(text="Email/Username:", font=("Arial", 12), bg="Black", fg="White")
email_username.grid(column=0, row=4)
email_username_entry = Entry(width=53, bg="Grey", fg="white")
email_username_entry.grid(column=1, row=4, columnspan=2)

password_label = Label(text="Password:", font=("Arial", 12), bg="Black", fg="White")
password_label.grid(column=0, row=5)
password_entry = Entry(width=33, bg="Grey", fg="white")
password_entry.grid(column=1, row=5)

generate_pass_button = Button(text="Generate Password", font=("Arial", 10), width=14, bg="dark Grey", fg="White")
generate_pass_button.grid(column=2, row=5, columnspan=1)

add_button = Button(text="add", font=("Arial", 12), width=35, command=save_password, bg="dark Grey", fg="White")
add_button.grid(column=1, row=6, columnspan=2)

window.mainloop()
