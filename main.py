import string, random
from customtkinter import *
from tkinter import messagebox
from random import shuffle


password = ""

def copy_text(_event):
    global password
    if password =='':
        messagebox.showerror('Copy Error', 'Nothing to copy.')
    else:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo('', 'Copied to clipboard.')

def generate_password():
    global password
    password = ""
    canva.delete('all')

    try:
        pw_len = int(pw_len_input.get())
        if pw_len < 0:
            messagebox.showerror('ValueError', "Password length can't be less than or equal to 0")

        elif pw_len > 30:
            messagebox.showerror('Length Limit', 'You have reached the length limit. Maximum length is 30.')

        else:
            chars = list(string.ascii_letters + string.digits + "!@#$%&*+?|/-_~")
            shuffle(chars)
            for i in range(pw_len):
                password += random.choice(chars)
        canva.create_text(10, 10,
                          text=password, width=245,
                          anchor='nw',
                          font=('Arial', 20),
                          fill='white')

    except ValueError:
        messagebox.showerror("Error", "Password Length Must Be A Number")

root = CTk()
root.wm_title("Password Generator")
root.geometry('300x380')
root.resizable(False, False)

pw_len_input = CTkEntry(root, placeholder_text='Password Length', font=('Arial', 20),width=200, height=50)
pw_len_input.place(x=50, y=30)

generate_button = CTkButton(root, text='Generate Password', command=generate_password,  width=200).place(x=50, y=90)

canva = CTkCanvas(root, width=260, height=110, bg='#2b2b2b')
canva.bind('<Button-1>', copy_text)
canva.place(x=60, y=210)

root.mainloop()