from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# import pyperclip
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    rd_letters = [random.choice(letters) for n in range(nr_letters)]
    rd_symbols = [random.choice(symbols) for n in range(nr_symbols)]
    rd_numbers = [random.choice(numbers) for n in range(nr_numbers)]
    password_list = rd_letters + rd_symbols + rd_numbers
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_uname_entry.get()
    manual_password = password_entry.get()
    if website == "" or email == "" or manual_password =="":
        messagebox.showerror(title="Oops", message="Please don't leave any empty fields.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {manual_password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {manual_password}\n")
                messagebox.showinfo(title="Success", message="Your Password has been added.")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image= logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
email_uname_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(column=0, row=1)
email_uname_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
email_uname_entry = Entry(width=35)
password_entry = Entry(width=21)

website_entry.grid(column=1, row=1, columnspan=2)
email_uname_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)
website_entry.focus()
email_uname_entry.insert(END,"A@gmail.com")

password_generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add",width=36, command=save)

password_generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)














window.mainloop()
