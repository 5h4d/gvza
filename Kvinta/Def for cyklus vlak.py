import tkinter as tk

canvas = tk.Canvas(height=150, width=840)
canvas.pack()

#mašinka
canvas.create_rectangle(10, 60, 170, 130, fill='maroon', outline ='maroon') #krabica
canvas.create_oval(4, 60, 30, 130, fill='maroon', outline='maroon') #oblok predok
canvas.create_rectangle(25, 40, 30, 70, fill='maroon', outline='maroon') #komin
canvas.create_rectangle(90, 10, 150, 130, fill='maroon', outline='maroon') #kabinka
canvas.create_rectangle(95, 15, 145, 55, fill='skyblue') #okenko

def vlagon():
    canvas.create_rectangle(x, 60, x+160, 130, fill='blue')
    y = x
    for t in range(1, 5):
        canvas.create_rectangle(y+10, 70, y+30, 90, fill='skyblue')
        y = y+40
    canvas.create_rectangle(x+160, 92.5, x+165, 97.5, fill='grey')
    canvas.create_rectangle(x-5, 92.5, x, 97.5, fill='grey')
x = 175

#vagony
for k in range(1, 5):
    vlagon()
    x = x+165

#kolesa:
x=15
n=1
for i in range(1, 21):
    canvas.create_oval(x, 120, x+25, 145, fill='black')
    if (n < 4):
        x = x+40
    else:
        x = x+45
        n = 0
    n = n+1
