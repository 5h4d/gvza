import tkinter as tk
import random as rnd
cnv=tk.Canvas(height=500, width=300, bg='white')
cnv.pack()

cnv.create_rectangle(100, 25, 200, 175, outline='black', width=3)
cnv.create_rectangle(100, 225, 200, 400, outline='orange', width=3)
def bet():
    cnv.create_rectangle(35, 425, 265, 475, outline='white', fill='white')
    cnv.create_rectangle(35, 425, 85, 475, outline='blue')
    cnv.create_rectangle(95, 425, 145, 475, outline='blue')
    cnv.create_rectangle(155, 425, 205, 475, outline='blue')
    cnv.create_rectangle(215, 425, 265, 475, outline='blue')
    cnv.create_text(60, 450, text='10', font='arial 15 bold', fill='blue')
    cnv.create_text(120, 450, text='50', font='arial 15 bold', fill='blue')
    cnv.create_text(180, 450, text='100', font='arial 15 bold', fill='blue')
    cnv.create_text(240, 450, text='All In', font='arial 14 bold', fill='blue')

def act():
    cnv.create_rectangle(35, 425, 265, 475, outline='white', fill='white')
    cnv.create_rectangle(35, 425, 105, 475, outline='green')
    cnv.create_text(70, 455, text='Hit', font='arial 30', fill='green')
    cnv.create_rectangle(115, 425, 185, 475, outline='green')
    cnv.create_text(150, 452, text='Stand', font='arial 20', fill='green')
    cnv.create_rectangle(195, 425, 265, 475, outline='green')
    cnv.create_text(230, 450, text='Double Down', font='arial 9', fill='green', angle=35)
bet()
bal=500
ctrl=0
def igra(xy):
    global bal, ctrl
    x=xy.x
    y=xy.y
    if ctrl==0:
        bet()
        if y>=425 and y<=475:
            if x>=35 and x<=85:
                tab=10
                bal-=10
            if x>=95 and x<=145:
                tab=50
                bal-=50
            if x>=155 and x<=205:
                tab=100
                bal-=100
            if x>=215 and x<=265:
                tab=bal
                bal=0
        if tab!=0:
            ctrl+=1
            cnv.create_rectangle(120, 180, 180, 220, fill='white', outline='white')
            cnv.create_rectangle(160, 370, 190, 395, fill='white', outline='white')
            cnv.create_text(150, 200, text=tab)
            cnv.create_text(185, 393, text=bal)
            act()
            psum=rnd.randint(1,10)+rnd.randint(1,11)
            dsum=rnd.randint(1,11)
            cnv.create_text(

cnv.bind('<Button-1>',igra)
