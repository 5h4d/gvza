import tkinter as tk
i = int(input('¿Veľkosť článkov? : '))
if i>10:
    print('nah daj menšie dzik')
else:
    canvas=tk.Canvas(height=i*100, width=i*100)
    canvas.pack()
    x=i
    y=i
    for bruh in range(0, 100):
        #zvisel
        canvas.create_line(x, 0, x, 1000)
        #horzen
        canvas.create_line(0, y, 1000, y)
        x+=i
        y+=i
