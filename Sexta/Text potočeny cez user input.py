import tkinter as tk
c=tk.Canvas(width=500, height=500)
c.pack()

def sus(xy):
    x=xy.x
    y=xy.y
    angil=360/int(pocte.get())
    medzki='    '*int(len(amogus.get()))
    for ඞ in range(0,int(pocte.get())):
        c.create_text(x,y,text=medzki+amogus.get(),angle=angil,fill=clr.get(),font='arial 20')
        angil+=360/int(pocte.get())


amogus=tk.Entry()
amogus.pack()
pocte=tk.Entry()
pocte.pack()
clr=tk.Entry()
clr.pack()
c.bind('<Button-1>',sus)
