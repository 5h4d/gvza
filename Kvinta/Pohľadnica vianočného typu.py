import tkinter as tk
import random as rnd
import time
canvas = tk.Canvas(width=297, height=420, bg='black')
canvas.pack()

def trojuholnik():
    canvas.create_line(118.5, y, 148.5, y-30, 178.5, y, 118.5, y, fill='green', width=30)

y=100
for i in range(1, 5):
    trojuholnik()
    a = rnd.randrange(120, 160)
    b = rnd.randrange(y-30, y-10)
    c = rnd.randrange(120, 160)
    d = rnd.randrange(y-30, y-10)
    clra=rnd.choice(('red', 'lightgreen', 'blue', 'yellow', 'orange', 'purple'))
    clrb=rnd.choice(('red', 'lightgreen', 'blue', 'yellow', 'orange', 'purple'))
    canvas.create_oval(a, b, a+5, b+5, fill=clra)
    canvas.create_oval(c, d , c+5, d+5, fill=clrb)
    y = y+45

canvas.create_rectangle(138.5, 250, 158.5, 290, fill='brown', outline='brown')
aaaa=rnd.choice(('red', 'darkgreen', 'blue', 'magenta', 'orange', 'purple'))
canvas.create_text(148.5, 350, text='Veselé Vianoce!', font='times 30', fill=aaaa)
while True:
    xx = rnd.randrange(0, 285)
    yy = rnd.randrange(0, 300)
    xh = canvas.create_line(xx, yy, xx+12, yy, fill='paleturquoise')
    xv = canvas.create_line(xx+6, yy-6, xx+6, yy+6, fill='paleturquoise')
    xd1 = canvas.create_line(xx+3, yy-3, xx+9, yy+3, fill='paleturquoise')
    xd2 = canvas.create_line(xx+9, yy-3, xx+3, yy+3, fill='paleturquoise')
    a = rnd.randrange(0, 285)
    b = rnd.randrange(0, 300) 
    dh = canvas.create_line(a, b, a+12, b, fill='paleturquoise')
    dv = canvas.create_line(a+6, b-6, a+6, b+6, fill='paleturquoise')
    dd1 = canvas.create_line(a+3, b-3, a+9, b+3, fill='paleturquoise')
    dd2 = canvas.create_line(a+9, b-3, a+3, b+3, fill='paleturquoise')
    c = rnd.randrange(0, 285)
    d = rnd.randrange(0, 300)
    h = canvas.create_line(c, d, c+12, d, fill='paleturquoise')
    v = canvas.create_line(c+6, d-6, c+6, d+6, fill='paleturquoise')
    d1 = canvas.create_line(c+3, d-3, c+9, d+3, fill='paleturquoise')
    d2 = canvas.create_line(c+9, d-3, c+3, d+3, fill='paleturquoise')
    q = rnd.randrange(0, 285)
    w = rnd.randrange(0, 300)
    q1 = canvas.create_line(q, w, q+12, w, fill='paleturquoise')
    q2 = canvas.create_line(q+6, w-6, q+6, w+6, fill='paleturquoise')
    q3 = canvas.create_line(q+3, w-3, q+9, w+3, fill='paleturquoise')
    q4 = canvas.create_line(q+9, w-3, q+3, w+3, fill='paleturquoise')
    e = rnd.randrange(0, 285)
    f = rnd.randrange(0, 300)
    e1 = canvas.create_line(e, f, e+12, f, fill='paleturquoise')
    e2 = canvas.create_line(e+6, f-6, e+6, f+6, fill='paleturquoise')
    e3 = canvas.create_line(e+3, f-3, e+9, f+3, fill='paleturquoise')
    e4 = canvas.create_line(e+9, f-3, e+3, f+3, fill='paleturquoise')
    m = rnd.randrange(0, 285)
    n = rnd.randrange(0, 300)
    m1 = canvas.create_line(m, n, m+12, n, fill='paleturquoise')
    m2 = canvas.create_line(m+6, n-6, m+6, n+6, fill='paleturquoise')
    m3 = canvas.create_line(m+3, n-3, m+9, n+3, fill='paleturquoise')
    m4 = canvas.create_line(m+9, n-3, m+3, n+3, fill='paleturquoise')
    
    for x in range(0,105):
        canvas.move(xh,0,8)
        canvas.move(xv,0,8)
        canvas.move(xd1,0,8)
        canvas.move(xd2,0,8)

        canvas.move(dh,0,5)
        canvas.move(dv,0,5)
        canvas.move(dd1,0,5)
        canvas.move(dd2,0,5)

        canvas.move(h,0,4)
        canvas.move(v,0,4)
        canvas.move(d1,0,4)
        canvas.move(d2,0,4)

        canvas.move(q1,0,8)
        canvas.move(q2,0,8)
        canvas.move(q3,0,8)
        canvas.move(q4,0,8)

        canvas.move(e1,0,5)
        canvas.move(e2,0,5)
        canvas.move(e3,0,5)
        canvas.move(e4,0,5)

        canvas.move(m1,0,4)
        canvas.move(m2,0,4)
        canvas.move(m3,0,4)
        canvas.move(m4,0,4)


        canvas.update()
        time.sleep(.03)
