import json
import os
import tkinter as tk

from helpers import clear_screen
from PIL import Image, ImageTk

row_size = 2


def render_products(screen: tk.Tk):
    clear_screen(screen)
    with open(os.path.join("db", "products.txt")) as f:
        curr_row = curr_col = 0
        for product_idx, line in enumerate(f):
            product = json.loads(line)

            if product_idx % row_size == 0:
                curr_row += 4
                curr_col = 0

            tk.Label(screen, text=product["name"]).grid(row=curr_row, column=curr_col)

            image = Image.open(os.path.join("images", product["img_path"]))
            image = image.resize((100, 100))
            tk_image = ImageTk.PhotoImage(image)
            lbl = tk.Label(screen, image=tk_image)
            lbl.image = tk_image
            lbl.grid(row=curr_row + 1, column=curr_col)

            tk.Label(screen, text=product["count"]).grid(row=curr_row + 2, column=curr_col)
            tk.Button(screen, text=f'Buy {product["id"]}').grid(row=curr_row + 3, column=curr_col)
            curr_col += 1
