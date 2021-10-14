import tkinter as tk
canvas = tk.Canvas(height=600, width=300)
canvas.pack()

#dve zvisle veci æ
canvas.create_line(220, 600, 30, 20, width=3)
canvas.create_line(270, 600, 80, 20, width=3)

#prički
x = 10
y = 40
for a in range(0, 20):
    canvas.create_line(x, y, x+100, y, width=3)
    x+=10
    y+=30
    
