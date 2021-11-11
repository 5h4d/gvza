import tkinter as tk
import random as rnd
cnv=tk.Canvas(height=500, width=300)
cnv.pack()

cnv.create_rectangle(100, 25, 200, 175, outline='black', width=3)
cnv.create_rectangle(100, 225, 200, 400, outline='orange', width=3)
def bet():
    cnv.create_rectangle(35, 425, 85, 475, outline='blue')
    cnv.create_rectangle(95, 425, 145, 475, outline='blue')
    cnv.create_rectangle(155, 425, 205, 475, outline='blue')
    cnv.create_rectangle(215, 425, 265, 475, outline='blue')
    cnv.create_text(60, 450, text='10', font='arial 15 bold', fill='blue')
    cnv.create_text(120, 450, text='50', font='arial 15 bold', fill='blue')
    cnv.create_text(180, 450, text='100', font='arial 15 bold', fill='blue')
    cnv.create_text(240, 450, text='All In', font='arial 14 bold', fill='blue')

def act():
    cnv.create_rectangle(35, 425, 105, 475, outline='green')
    cnv.create_text(70, 455, text='Hit', font='arial 30', fill='green')
    cnv.create_rectangle(115, 425, 185, 475, outline='green')
    cnv.create_text(150, 452, text='Stand', font='arial 20', fill='green')
    cnv.create_rectangle(195, 425, 265, 475, outline='green')
    cnv.create_text(230, 450, text='Double Down', font='arial 9', fill='green', angle=35)
act()
