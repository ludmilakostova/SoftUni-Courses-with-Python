import tkinter as tk


def clear_screen(screen: tk.Tk):
    for element in screen.grid_slaves():
        element.destroy()