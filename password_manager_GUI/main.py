from tkinter import *
from tkinter import messagebox  # It is not class of tkinter so we have to import it
import pyperclip
from random import shuffle, choice, randint
# from passwd_generator import generate_password

FONT = "Arial"
FONT_SIZE = 11

# Password_generator
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = []
    password_list = password_letter + password_symbol + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# To save password
def save_password():
    website_data = website_entry.get()
    email_data = email_username_entry.get()
    passwd_data = password_entry.get()

    if len(website_data) == 0 or len(email_data) == 0 or len(passwd_data) == 0:
        messagebox.showinfo(title="Error", message="Don't let any field empty .!")
    else:
        verification_pop_up = messagebox.askokcancel(title=website_data,
                                                     message=f'Detail you entered:\nEmail: {email_data}\n'
                                                             f'Password: {passwd_data}\nIs it ok to save ..?')
        if verification_pop_up:
            with open("./data.txt", mode="a") as save_data:
                save_data.write(
                    f'| Website: {website_data} || Email ID or username: {email_data} || Password: {passwd_data} |\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                email_username_entry.delete(0, END)


def clear_screen():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    email_username_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=80, pady=80, bg="Black")

canvas = Canvas(width=200, height=224, highlightthickness=0, bg="Black")
lock_photo = PhotoImage(file="./logo.png")
canvas.create_image(110, 112, image=lock_photo)
canvas.grid(column=1, row=1)

website_label = Label(text="Website:", font=(FONT, FONT_SIZE), bg="Black", fg="White")
website_label.grid(column=0, row=3)
website_entry = Entry(width=53, bg="Grey", fg="white")
website_entry.insert(0, "www.abc.com")
website_entry.focus()
website_entry.grid(column=1, row=3, columnspan=2)

email_username = Label(text="Email/Username:", font=(FONT, FONT_SIZE), bg="Black", fg="White")
email_username.grid(column=0, row=4)
email_username_entry = Entry(width=53, bg="Grey", fg="white")
email_username_entry.insert(0, "xyz@gmail.com")
email_username_entry.grid(column=1, row=4, columnspan=2)

password_label = Label(text="Password:", font=(FONT, FONT_SIZE), bg="Black", fg="White")
password_label.grid(column=0, row=5)
password_entry = Entry(width=33, bg="Grey", fg="white")
password_entry.insert(0, "SuperSecurePasswd")
password_entry.grid(column=1, row=5)

generate_pass_button = Button(text="Generate Password", font=(FONT, 10), command=generate_password, width=14,
                              bg="dark Grey", fg="White")
generate_pass_button.grid(column=2, row=5, columnspan=1)

add_button = Button(text="add", font=(FONT, FONT_SIZE), width=35, command=save_password, bg="dark Grey", fg="White")
add_button.grid(column=1, row=6, columnspan=2)

# add_button = Button(text="Clear", font=(FONT, FONT_SIZE), width=8, command=clear_screen, bg="dark Grey", fg="White")
# add_button.grid(column=0, row=6, columnspan=2)

window.mainloop()
