import tkinter as tk
cnv = tk.Canvas(height=400, width=400)
cnv.pack()
x=0
y=0
for g in range(0, 32):
    cnv.create_rectangle(x,y,x+50,y+50,fill='black')
    x+=100
    if x==400:
        y+=50
        x=50
    if x==450:
        y+=50
        x=0

#pisis
def w1(xy):
    y=xy.y
    x=xy.x
    cnv.create_text(x,y,text='Biely Pešiak',fill='darkgreen',angle=45,font='arial 7 bold')
def w2(xy):
    y=xy.y
    x=xy.x
    cnv.create_text(x,y,text='Biela Veža',fill='darkgreen',angle=45,font='arial 7 bold')
def w3(xy):
    x=xy.x
    y=xy.y
    cnv.create_text(x,y,text='Biely Jazdec',fill='darkgreen',angle=45,font='arial 7 bold')
def w4(xy):
    x=xy.x
    y=xy.y
    cnv.create_text(x,y,text='Biely Strelec',fill='darkgreen',angle=45,font='arial 7 bold')
def w5(xy):
    x=xy.x
    y=xy.y
    cnv.create_text(x,y,text='Biela Kráľovná',fill='darkgreen',angle=45,font='arial 7 bold')
def w6(xy):
    x=xy.x
    y=xy.y
    cnv.create_text(x,y,text='Biely Kráľ',fill='darkgreen',angle=45,font='arial 7 bold')
def b1(xy):
    y=xy.y
    x=xy.x
    cnv.create_text(x,y,text='Čierny Pešiak',fill='darkgreen',angle=45,font='arial 7 bold')
def b2(xy):
    y=xy.y
    x=xy.x
    cnv.create_text(x,y,text='Čierna Veža',fill='darkgreen',angle=45,font='arial 7 bold')
def b3(xy):
    x=xy.x
    y=xy.y
    cnv.create_text(x,y,text='Čierny Jazdec',fill='darkgreen',angle=45,font='arial 7 bold')
def b4(xy):
    x=xy.x
    y=xy.y
    cnv.create_text(x,y,text='Čierny Strelec',fill='darkgreen',angle=45,font='arial 7 bold')
def b5(xy):
    x=xy.x
    y=xy.y
    cnv.create_text(x,y,text='Čierna Kráľovná',fill='darkgreen',angle=45,font='arial 7 bold')
def b6(xy):
    x=xy.x
    y=xy.y
    cnv.create_text(x,y,text='Čierny Kráľ',fill='darkgreen',angle=45,font='arial 7 bold')


#pohyb snáď
def kde(xy):
    x=xy.x
    y=xy.y
