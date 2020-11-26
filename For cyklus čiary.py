import tkinter as tk

#cziarky
canvas = tk.Canvas(width=60, height=210)
canvas.pack()
y = 0
x = 0
for i in range(1, 6):
    x = x+10
    y = y+30
    canvas.create_line(x, y, x, 200)
