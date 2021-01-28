import tkinter as tk
import random as rnd
canvas = tk.Canvas(width=500, height=500)
canvas.pack()

def czaroczka(xy):
    x = xy.x
    y = xy.y
    if x <= 250:
        if y <= 250:
            z = 'orangered'
        else:
            z = 'cornflowerblue'
    else:
        if y <= 250:
            z = 'yellowgreen'
        else:
            z = 'goldenrod'
    canvas.create_line(250, 250, x, y, fill=z, width=5 )

canvas.bind('<Button-1>', czaroczka)
