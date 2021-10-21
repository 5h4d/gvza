import tkinter as tk

canvas = tk.Canvas(width=50, height=100, bg='green')
canvas.pack()

canvas.create_oval(10, 10, 40, 90, fill='brown', outline='brown')
canvas.create_rectangle(10, 50, 20, 100, fill='green', outline='green')
canvas.create_rectangle(30, 50, 50, 100, fill='green', outline='green')
