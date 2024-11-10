import tkinter as tk
from tkinter import colorchooser

def start_paint(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y

def paint(event):
    x, y = event.x, event.y
    canvas.create_line((prev_x, prev_y, x, y), fill=current_color, width=brush_size, capstyle=tk.ROUND, smooth=tk.TRUE)
    prev_x, prev_y = x, y

def choose_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color

def change_brush_size(new_size):
    global brush_size
    brush_size = new_size

root = tk.Tk()
root.title("Basic Paint Application")

current_color = "black"
brush_size = 2
prev_x, prev_y = None, None

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind("<Button-1>", start_paint)
canvas.bind("<B1-Motion>", paint)

menu = tk.Menu(root)
root.config(menu=menu)
options_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Choose Color", command=choose_color)
options_menu.add_command(label="Brush Size (1)", command=lambda: change_brush_size(1))
options_menu.add_command(label="Brush Size (3)", command=lambda: change_brush_size(3))
options_menu.add_command(label="Brush Size (5)", command=lambda: change_brush_size(5))

root.mainloop()
