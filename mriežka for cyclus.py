import tkinter as tk
canvas=tk.Canvas(height=1000, width=1000)
canvas.pack()

x=10
y=10
for bruh in range(0, 100):
    #zvisel
    canvas.create_line(x, 0, x, 1000)
    #horzen
    canvas.create_line(0, y, 1000, y)
    x+=10
    y+=10
