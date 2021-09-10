import json
import os
import tkinter as tk

from helpers import clear_screen


def register(**user):
    with open(os.path.join('db', 'user_store.txt'), 'a') as f:
        f.write(f"{user['username']} - {user['password']}\n")
    return "we are here"


def render_register(screen: tk.Tk, on_success):
    clear_screen(screen)
    inputs = [
        ('username', tk.Entry(screen)),
        ('password', tk.Entry(screen)),
        ('first_name', tk.Entry(screen)),
        ('last_name', tk.Entry(screen)),
    ]
    for idx, (label, input_widget) in enumerate(inputs):
        input_widget.grid(row=idx, column=0)

    def on_click():
        result = register(**{user_attribute: widget.get() for (user_attribute, widget) in inputs})
        if result:
            clear_screen(screen)
            on_success(screen)
        else:
            tk.Label(screen, text="Error", background="red", foreground="white").grid(row=5, column=0)

    tk.Button(
        screen,
        text="Submit",
        command=on_click).grid(row=len(inputs), column=0)


def render_login(screen: tk.Tk, on_success):
    clear_screen(screen)
    username = tk.Entry(screen)
    username.grid(row=0, column=0)
    password = tk.Entry(screen)
    password.grid(row=1, column=0)

    def on_click():
        if login(username.get(), password.get()):
            on_success(screen)
        else:
            tk.Label(screen, text="Invalid username or password", bg="black", fg="red").grid(row=3, column=0)

    tk.Button(screen, text="Login",
              command=on_click
              ).grid(row=2, column=0)


def login(username, password):
    with open(os.path.join("db", "user_store.txt")) as file:
        for row in file:
            line = row.strip().split("-", maxsplit=1)
            if username == line[0] and password == line[1]:
                with open(os.path.join("db", "current_users.txt"), 'w') as f:
                    f.write(f'{username}-{password}')
                return True

    return False
