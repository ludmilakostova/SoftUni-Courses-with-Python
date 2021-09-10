import os
import tkinter as tk

from authentification import render_register, render_login
from products import render_products


def render_main_screen(screen: tk.Tk):
    tk.Button(screen, text="Login", background="green", foreground="white",
              command=lambda: render_login(screen, on_success=render_products)).grid(
        row=0, column=0)
    tk.Button(screen, text="Register", background="yellow", foreground="black",
              command=lambda: render_register(screen, on_success=render_main_screen)).grid(
        row=0, column=1)


if __name__ == "__main__":
    window = tk.Tk()
    window.title(" My first e-shop")
    window.geometry('700x600')

    render_main_screen(window)

    window.mainloop()
