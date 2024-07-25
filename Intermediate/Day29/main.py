from tkinter import *
from tkinter import messagebox
from random import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(4, 6))]
    password_symbols = [choice(symbols) for _ in range(randint(1, 2))]
    password_numbers = [choice(numbers) for _ in range(randint(1, 2))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = website_entry.get()
    name = name_entry.get()
    pword = password_entry.get()
    new_entry = f"{site} | {name} | {pword}\n"
    
    if len(site) == 0 or len(name) == 0 or len(pword) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure all fields aren't empty")
    else:    
        is_ok = messagebox.askokcancel(title=site, message =f"These are the details entered: \nEmail: {name} \nPassword: {pword} \nIs it ok to save?")
        # Write to File
        if is_ok: 
            with open("data.txt", "a") as data:
                data.write(new_entry + "\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Keeper")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = logo)
canvas.grid(column=1, row=0)

# ROW 1
website_label=Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
 
# ROW 2
name_label = Label(text="Email/Username:")
name_label.grid(column=0, row=2)
name_entry = Entry()
name_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
name_entry.insert(0, "edpvpro@hotmail.com")
 
# ROW 3
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW")
 
# ROW 4
add_btn = Button(text="Add", width=35, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()