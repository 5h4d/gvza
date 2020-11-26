import tkinter as tk

#otocivy vec
canvas = tk.Canvas(height=200, width=200)
canvas.pack()

a = 0
for i in range(1, 4):
    canvas.create_text(100, 100, text='ŤAHAŤ', angle=a, fill='blue', font='arial 30')
    a = a+120
