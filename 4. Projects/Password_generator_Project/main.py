from tkinter import *
import random
import string
import pyperclip

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("Password Generator Project")

"""Definition of the heading"""
heading = Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()
Label(root, text='Source - First steps in programming', font='arial 10 bold').pack(side=BOTTOM)

"""Selection of password length between 8 to 32 symbols"""
password_label = Label(root, text='PASSWORD LENGTH', font='arial 10 bold').pack()
password_length = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=password_length, width=15).pack()


"""Definition of the function to generate randomly the password"""
password_string = StringVar()


def Generator():
    password = ""

    for i in range(4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + \
                   random.choice(string.digits) + random.choice(string.punctuation)

    for j in range(password_length.get() - 4):
        password += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)

    password_string.set(password)


"""Definition of the fields for generating the password"""
Button(root, text='GENERATE PASSWORD', command=Generator).pack(pady=5)
Entry(root, textvariable=password_string).pack()


"""Definition of a function to copy the password on a clipboard"""


def Copy_Password():
    pyperclip.copy(password_string.get())


Button(root, text='COPY TO CLIPBOARD', command=Copy_Password).pack(pady=5)

"""To run the GUI app"""
root.mainloop()
