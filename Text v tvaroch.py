import tkinter
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

canvas.create_rectangle(10, 10, 110, 60, outline='blue', fill='red')
#obdoliznik
canvas.create_text(60, 35, text='ZLETELI', fill='black', font='arial 15 italic')
#obdolznikcny text

canvas.create_rectangle(120, 10, 170, 60, outline='red', fill='blue')
#setovrec
canvas.create_text(145, 35, text='ORLY', fill='white', font='fisedsys, 13 bold')
#cetvorecny text

canvas.create_line(180, 60, 230, 60, 205, 10, 180, 60, fill='magenta', width=5)
#trojuholnik
canvas.create_text(205, 40, font='Helvetica, 20', text='Z', fill='orange')
#trojuholenikovny text

canvas.create_oval(240, 10, 340, 60, outline='orange', fill='green')
#ovalis
canvas.create_text(290, 35, font='times, 23 italic', text='TATRY', fill='blue')
#ovalisosidny text

canvas.create_oval(10, 70, 340, 400, outline='blue', fill='yellow')
#keruh
canvas.create_text(175, 235, text='MOR HO', font='sans 55 italic bold', fill='purple')
#kruhoidnoi text
