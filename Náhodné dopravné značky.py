import tkinter
import random
canvas = tkinter.Canvas(width=1000, height=700)
canvas.pack()
x = random.randint(0, 790)
y = random.randint(0, 450)

#vec 1
canvas.create_oval(x, y, x+100, y+100, fill='white')
#outline
canvas.create_oval(x+5, y+5, x+95, y+95, fill='red')
#czerveny keruh
canvas.create_oval(x+15, y+15, x+85, y+85, fill='white')
#fill
canvas.create_text(x+50, y+50, text=random.choice((10, 20, 30, 40, 50, 60, 69, 70, 80, 90)), font='arial 35 bold', fill='black')
#textung 80
canvas.create_line(x+50, y+100, x+50, y+250, fill='grey', width=5)
#tyczka


#vec 2
canvas.create_rectangle(x+110, y, x+210, y+100, fill='midnightblue')
#background
canvas.create_text(x+160, y+40, text=random.choice(('H', 'P')),fill='white', font='arial 70 bold')
#Hchko
canvas.create_text(x+160, y+85, text='NEMOCNICA', fill='white', font='arial 11 bold')
#nemocnicapis
canvas.create_line(x+160, y+101, x+160, y+250, fill='grey', width=5)
