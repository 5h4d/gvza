import tkinter as tk
canvas=tk.Canvas(height=300, width=300)
canvas.pack()


#slunko yes pepega
canvas.create_oval(100, 100, 200, 200, fill='yellow', outline='yellow')


#lučiki ano
foo = 0
for i in range(1, 19):
    canvas.create_text(150, 150, text='------------------------------------------', font='bold 30', fill='yellow', angle=foo)
    foo+=10
