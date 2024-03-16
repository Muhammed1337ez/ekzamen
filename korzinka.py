from tkinter import Tk, Label, Frame, LabelFrame, Button, Spinbox
from PIL import ImageTk
from tkinter import PhotoImage
from basa import Database

window = Tk()
window.geometry("1100x1000")
window.configure(bg="#F0F0F0")
window.title("Korzinka")
frame = Frame(window)
frame.grid(padx=80, pady=80)
db = Database()
image_icon = PhotoImage(file="img.png")
window.iconphoto(True, image_icon)

label_frame = LabelFrame(frame, bg="#F0F0F0")
label_frame.grid()


# YOZUV ================================================
e_label = Label(window, text="Korzinka.uz",
                fg="Red", bg="#F0F0F0",
                font=("Verdana", 40))
e_label.place(x=280, y=5)


# chuchvora =================================================
chuchvora_photo1 = ImageTk.PhotoImage(file="chuchvora.png")
chuchvora_label1 = Label(label_frame, image=chuchvora_photo1)
chuchvora_label1.grid(row=1, column=0)

chuchvora_label = Label(label_frame, text="Chuchvora",
                     font=("Verdana", 20),
                     fg="black", bg="#F0F0F0")
chuchvora_label.grid(row=2, column=0)

chuchvora_label2 = Label(label_frame, text="21,990 so'm",
                      font=("Verdana", 20),
                      fg="black", bg="#F0F0F0")
chuchvora_label2.grid(row=3, column=0)

chuchvora_spinbox = Spinbox(label_frame, from_=1, to=100)
chuchvora_spinbox.grid(row=4, column=0)
# Maloko ==================================================
Maloko_photo = ImageTk.PhotoImage(file="maloko.png")
Maloko_label = Label(label_frame, image=Maloko_photo)
Maloko_label.grid(row=1, column=1)

Maloko_label = Label(label_frame, text="Maloko",
                    font=("Verdana", 20),
                    fg="black", bg="#F0F0F0")
Maloko_label.grid(row=2, column=1)

Maloko_label2 = Label(label_frame, text="11,990 so'm",
                     font=("Verdana", 20),
                     fg="black", bg="#F0F0F0")
Maloko_label2.grid(row=3, column=1)

Maloko_spinbox = Spinbox(label_frame, from_=1, to=100)
Maloko_spinbox.grid(row=4, column=1)
# margarin ===================================================

margarin_photo = ImageTk.PhotoImage(file="margarin.png")
margarin_label = Label(label_frame, image=margarin_photo)
margarin_label.grid(row=1, column=2)

margarin_label = Label(label_frame, text="Margarin",
                      font=("Verdana", 20),
                      fg="black", bg="#F0F0F0")
margarin_label.grid(row=2, column=2)

margarin_label2 = Label(label_frame, text="5,990 so'm",
                       font=("Verdana", 20),
                       fg="black", bg="#F0F0F0")
margarin_label2.grid(row=3, column=2)

margarin_spinbox = Spinbox(label_frame, from_=1, to=100)
margarin_spinbox.grid(row=4, column=2)
# HOT DOG ===============================================
hotchland_photo = ImageTk.PhotoImage(file="hotchland.png")
hotchland_label = Label(label_frame, image=hotchland_photo)
hotchland_label.grid(row=1, column=3)

hotchland_label = Label(label_frame, text="Hotchland",
                      font=("Verdana", 20),
                      fg="black", bg="#F0F0F0")
hotchland_label.grid(row=2, column=3)

hotchland_label2 = Label(label_frame, text="23,990 so'm",
                       font=("Verdana", 20),
                       fg="black", bg="#F0F0F0")
hotchland_label2.grid(row=3, column=3)

hotdog_spinbox = Spinbox(label_frame, from_=1, to=100)
hotdog_spinbox.grid(row=4, column=3)
# SIR====================================================
sir_photo = ImageTk.PhotoImage(file="sir.png")
sir_label = Label(label_frame, image=sir_photo)
sir_label.grid(row=5, column=0)

sir_label = Label(label_frame, text="Sir",
                    font=("Verdana", 20),
                    fg="black", bg="#F0F0F0")
sir_label.grid(row=6, column=0)

sir_label2 = Label(label_frame, text="23,990 so'm",
                     font=("Verdana", 20),
                     fg="black", bg="#F0F0F0")
sir_label2.grid(row=7, column=0)

sir_spinbox = Spinbox(label_frame, from_=1, to=100)
sir_spinbox.grid(row=8, column=0)
# SNACKS ================================================
oreo_photo = ImageTk.PhotoImage(file="oreo.png")
oreo_label = Label(label_frame, image=oreo_photo)
oreo_label.grid(row=5, column=1)

oreo_label = Label(label_frame, text="Oreo",
                     font=("Verdana", 20),
                     fg="black", bg="#F0F0F0")
oreo_label.grid(row=6, column=1)

oreo_label2 = Label(label_frame, text="6,990 so'm",
                      font=("Verdana", 20),
                      fg="black", bg="#F0F0F0")
oreo_label2.grid(row=7, column=1)

oreo_spinbox = Spinbox(label_frame, from_=1, to=100)
oreo_spinbox.grid(row=8, column=1)
# HOT DOG ===============================================
tvorok_photo = ImageTk.PhotoImage(file="tvorok.png")
tvorok_label = Label(label_frame, image=tvorok_photo)
tvorok_label.grid(row=5, column=2)

tvorok_label = Label(label_frame, text="Tvorok",
                    font=("Verdana", 20),
                    fg="black", bg="#F0F0F0")
tvorok_label.grid(row=6, column=2)

tvorok_label2 = Label(label_frame, text="23,990 so'm",
                     font=("Verdana", 20),
                     fg="black", bg="#F0F0F0")
tvorok_label2.grid(row=7, column=2)

tvorok_spinbox = Spinbox(label_frame, from_=1, to=100)
tvorok_spinbox.grid(row=8, column=2)
# COFFEE ===========================================
coffee_photo = ImageTk.PhotoImage(file="COFE.png")
coffee_label = Label(label_frame, image=coffee_photo)
coffee_label.grid(row=5, column=3)

coffee_label = Label(label_frame, text="Coffee",
                     font=("Verdana", 20),
                     fg="black", bg="#F0F0F0")
coffee_label.grid(row=6, column=3)

coffee_label2 = Label(label_frame, text="59,990 so'm",
                      font=("Verdana", 20),
                      fg="black", bg="#F0F0F0")
coffee_label2.grid(row=7, column=3)

coffee_spinbox = Spinbox(label_frame, from_=1, to=100)
coffee_spinbox.grid(row=8, column=3)


# KNOPKA=================================================
def button_count():
    chuchvora_total = int(chuchvora_spinbox.get()) * 21_990
    Maloko_total = int(Maloko_spinbox.get()) * 11_990
    margarin_total = int(margarin_spinbox.get()) * 5_990
    hotchland_total = int(hotdog_spinbox.get()) * 23_990
    sir = int(sir_spinbox.get()) * 23_990
    oreo_total = int(oreo_spinbox.get()) * 6_990
    tvorok_total = int(tvorok_spinbox.get()) * 23_990
    coffee_total = int(coffee_spinbox.get()) * 59_990
    total_bills = sum([chuchvora_total, Maloko_total, margarin_total, hotchland_total,
                       sir, oreo_total, tvorok_total, coffee_total])
    bills = Label(text=f"Sizning hisobingiz {total_bills} so'm bo'ldi, "
                       f"Xaridingiz uchun rahmat",
                  bg="#F0F0F0", fg="black", font=("Arial", 20, "bold"))
    bills.place(x=200, y=700)




buyur_button = Button(window, text="Narxni bilish",
                      font=("Verdana", 25),
                      fg="#279240", bg="white", command=button_count)
buyur_button.place(x=310, y=750)

# =====================================================

for widget in label_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
from tkinter import Tk, Frame, Button, Menu, filedialog


my_menu = Menu(window)
window.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Options", menu=file_menu)

def open_file():
    filedialog.askopenfilename()


file_menu.add_command(label="Exit", command=window.quit)
file_menu.add_separator()

sub_menu = Menu(file_menu, tearoff=0)
file_menu.add_cascade(label="Admin menu", menu=sub_menu)

sub_menu2 = Menu(file_menu, tearoff=0)
sub_menu2.add_command(label="Reload APP")
sub_menu2.add_command(label="Change MODE")
sub_menu.add_cascade(label="Settings", menu=sub_menu2)






window.mainloop()
