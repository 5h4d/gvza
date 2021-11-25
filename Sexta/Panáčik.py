import tkinter as tk
import random as r
c=tk.Canvas(height=500, width=200)
c.pack()
def yes():
    oke = input('Farba očí: ([M]odrá/[Z]elená/[H]nedá: ')
    vlas = input('Farba vlasov: [H]nedá/[C]ierna/[B]lond: ')
    pant = input('Farba gati: [M]odrá/[C]ierna/[P]iesková: ')
    heit = input('Výška: [B]ig,[S]mol: ')
    msk = input('Rúško?: [A]no/[N]ie: ')
    if pant == 'M' or pant == 'm':
        pant='blue'
    elif pant == 'C' or pant == 'c':
        pant='black'
    else:
        pant='sandybrown'
    if oke == 'M' or oke == 'm':
        oke='Blue'
    elif oke == 'Z' or oke == 'z':
        oke='green'
    else:
        oke='brown'
    if vlas == 'H' or vlas == 'h':
        vlas='brown'
    elif vlas == 'C' or vlas == 'c':
        vlas='black'
    else:
        vlas='khaki'
    if heit == 'B' or heit == 'b':
        c.create_rectangle(70, 490, 90, 250, fill=pant, tags='a')
        c.create_rectangle(110, 490, 130, 250, fill=pant,tags='a')
        c.create_line(50, 250, 150, 250, 100, 100, 50, 250, width=5,tags='a')
        c.create_oval(70, 100, 130, 40, width=3, tags='a')
        c.create_oval(80, 60, 90, 70, fill=oke, tags='a')
        c.create_oval(120, 60, 110, 70, fill=oke, tags='a')
        for aa in range(0,100):
            c.create_line(100, 40, r.randrange(0,200), r.randrange(0,60),width=r.randrange(1,5),fill=vlas,tags='a')
        if msk == 'A' or msk=='a':
            c.create_rectangle(80, 90, 120, 70, fill='black', tags='a')
            c.create_line(120, 80, 130, 70, fill='black', width=2, tags='a')
            c.create_line(80, 80, 70, 70, fill='black', width=2, tags='a')
    else:
        c.create_rectangle(70, 490, 90, 400, fill=pant, tags='a')
        c.create_rectangle(110, 490, 130, 400,fill=pant,tags='a')
        c.create_line(50, 400, 150, 400, 100, 350, 50, 400, width=5,tags='a')
        c.create_oval(70, 350, 130, 290, width=3,tags='a')
        c.create_oval(80, 310, 90, 320, fill=oke,tags='a')
        c.create_oval(120, 310, 110, 320,fill=oke,tags='a')
        for aa in range(0,100):
            c.create_line(100, 290, r.randrange(0,200), r.randrange(0, 310),fill=vlas,tags='a')
        if msk == 'A' or msk == 'a':
            c.create_rectangle(80, 340, 120, 320, fill='black',tags='a')
            c.create_line(120, 330, 130, 320, width=2,tags='a')
            c.create_line(80, 330, 70, 320, width=2,tags='a')

yes()
c.create_text(170, 490, text='r-kom reset')
def dt(i):
    c.delete(all)
    yes()
c.bind_all('r',dt)
