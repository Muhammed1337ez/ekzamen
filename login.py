from tkinter import *
from tkinter import messagebox
from basa import Database
import os
from tkinter import PhotoImage
windows = Tk()
windows.geometry("500x450")
windows.title("Korzinka")
windows.configure(bg="black")
width = windows.winfo_screenwidth()
height = windows.winfo_screenheight()
center_x = int(width / 2 - 500 / 2)
center_y = int(height / 2 - 450 / 2)
windows.geometry(f"500x450+{center_x}+{center_y}")
db = Database()
image_icon = PhotoImage(file="img.png")
windows.iconphoto(True, image_icon)
def login_open():
    os.system("python korzinka.py")

frame = Frame(bg="black")
frame.pack()

login_label = Label(frame,
                    text="Login",
                    fg="red",
                    bg="black",
                    font=("Arial", 30, "bold"))
login_label.grid(row=0, column=0, pady=30, columnspan=2)

username_label = Label(frame,
                       text="Username",
                       bg="black",
                       fg="red",
                       font=("Arial", 15))
username_label.grid(row=1, column=0, pady=20)

username_entry = Entry(frame, font=("Arial", 15))
username_entry.grid(row=1, column=1)

password_label = Label(frame,
                       text="Password",
                       fg="red",
                       bg="black",
                       font=("Arial", 15))
password_label.grid(row=2, column=0, pady=20)

password_entry = Entry(frame, font=("Arial", 15), show="*")
password_entry.grid(row=2, column=1)


def login():
    username = username_entry.get()
    password = password_entry.get()
    user = db.login_user(username=username, password=password)
    if user:
        messagebox.showinfo(title="Success",
                            message="Successfully login")
        windows.destroy()
        login_open()
    else:
        messagebox.showerror(title="Error",
                             message="Invalid login")


login_button = Button(frame,
                      text="Login",
                      bg="red",
                      font=("Arial", 15),
                      command=login)
login_button.grid(row=3, column=0, pady=30, columnspan=2)


windows.mainloop()

