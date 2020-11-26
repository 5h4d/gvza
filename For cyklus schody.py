import tkinter as tk

#schudky
canvas = tk.Canvas(height=152, width=361)
canvas.pack()

x=1
y=1
a=360
for v in range(1, 6):
    canvas.create_line(x+30, y, x+30, y+30)     #vertikala lava
    canvas.create_line(a-30, y, a-30, y+30)     #vertikala prava
    canvas.create_line(x, y, x+30, y)           #horizontala lava
    canvas.create_line(a, y, a-30, y)           #horizontala prava
    x=x+30
    y=y+30
    a=a-30

canvas.create_line(151, 151, 211, 151)          #spajatkova vec
