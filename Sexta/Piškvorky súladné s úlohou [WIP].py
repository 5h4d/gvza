import tkinter as tk
import time
canvas = tk.Canvas(width=500, height=250, bg='white')
canvas.pack()
def tri(x):
    global saa, sab, sac, sba, sbb, sbc, sca, scb, scc, a, ctr, sz, sad, sbd, scd, sda, sdb, sdc, sdd, sae, sbe, sce, sde, sea, seb, sec, sed, see
    a=0
    ctr=0
    saa=0
    sab=0
    sac=0
    sba=0
    sbb=0
    sbc=0
    sca=0
    scb=0
    scc=0
    sz=3
    sad=0
    sbd=0
    scd=0
    sda=0
    sdb=0
    sdc=0
    sdd=0
    sae=0
    sbe=0
    sce=0
    sde=0
    sea=0
    seb=0
    sec=0
    sed=0
    see=0
    canvas.create_rectangle(0, 0, 250, 250, fill='white', outline='white')
    canvas.create_line(0, 50, 150, 50, width=2)
    canvas.create_line(0, 100, 150, 100, width=2)
    canvas.create_line(50, 0, 50, 150, width=2)
    canvas.create_line(100, 0, 100, 150, width=2)
    canvas.create_line(150, 0, 150, 150, width=2)
    canvas.create_line(0, 150, 150, 150, width=2)
def štyri(x):
    global saa, sab, sac, sba, sbb, sbc, sca, scb, scc, a, ctr, sz, sad, sbd, scd, sda, sdb, sdc, sdd, sae, sbe, sce, sde, sea, seb, sec, sed, see
    a=0
    ctr=0
    saa=0
    sab=0
    sac=0
    sba=0
    sbb=0
    sbc=0
    sca=0
    scb=0
    scc=0
    sz=4
    sad=0
    sbd=0
    scd=0
    sda=0
    sdb=0
    sdc=0
    sdd=0
    sae=0
    sbe=0
    sce=0
    sde=0
    sea=0
    seb=0
    sec=0
    sed=0
    see=0
    canvas.create_rectangle(0, 0, 250, 250, fill='white', outline='white')
    canvas.create_line(0, 50, 200, 50, width=2)
    canvas.create_line(0, 100, 200, 100, width=2)
    canvas.create_line(50, 0, 50, 200, width=2)
    canvas.create_line(100, 0, 100, 200, width=2)
    canvas.create_line(150, 0, 150, 200, width=2)
    canvas.create_line(0, 150, 200, 150, width=2)
    canvas.create_line(0, 200, 200, 200, width=2)
    canvas.create_line(200, 0, 200, 200, width=2)
def päť(x):
    global saa, sab, sac, sba, sbb, sbc, sca, scb, scc, a, ctr, sz, sad, sbd, scd, sda, sdb, sdc, sdd, sae, sbe, sce, sde, sea, seb, sec, sed, see
    a=0
    ctr=0
    saa=0
    sab=0
    sac=0
    sba=0
    sbb=0
    sbc=0
    sca=0
    scb=0
    scc=0
    sz=5
    sad=0
    sbd=0
    scd=0
    sda=0
    sdb=0
    sdc=0
    sdd=0
    sae=0
    sbe=0
    sce=0
    sde=0
    sea=0
    seb=0
    sec=0
    sed=0
    see=0
    canvas.create_rectangle(0, 0, 250, 250, fill='white', outline='white')
    canvas.create_line(0, 50, 250, 50, width=2)
    canvas.create_line(0, 100, 250, 100, width=2)
    canvas.create_line(50, 0, 50, 250, width=2)
    canvas.create_line(100, 0, 100, 250, width=2)
    canvas.create_line(150, 0, 150, 250, width=2)
    canvas.create_line(0, 150, 250, 150, width=2)
    canvas.create_line(0, 200, 250, 200, width=2)
    canvas.create_line(200, 0, 200, 250, width=2)
    canvas.create_line(250, 0, 250, 250, width=2)
    canvas.create_line(0, 250, 250, 250, width=2)

global saa, sab, sac, sba, sbb, sbc, sca, scb, scc, a, b, c, sz, sad, sbd, scd, sda, sdb, sdc, sdd, sae, sbe, sce, sde, sea, seb, sec, sed, see
a=0
ctr=0
saa=0
sab=0
sac=0
sba=0
sbb=0
sbc=0
sca=0
scb=0
scc=0
sz=0
sad=0
sbd=0
scd=0
sda=0
sdb=0
sdc=0
sdd=0
sae=0
sbe=0
sce=0
sde=0
sea=0
seb=0
sec=0
sed=0
see=0
def krizko(xy):
    global saa, sab, sac, sba, sbb, sbc, sca, scb, scc, a, b, c, sz, sad, sbd, scd, sda, sdb, sdc, sdd, sae, sbe, sce, sde, sea, seb, sec, sed, see
    x = xy.x
    y = xy.y
    if x <= 50:
        x = 25
        if y <= 50:
            if saa == 0:
                y = 25
                saa = 'xx'
                if sab == 'xx' and sac == 'xx':
                    canvas.create_line(25, 10, 25, 140, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
                if sba == 'xx' and sca == 'xx':
                    canvas.create_line(10, 25, 140, 25, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
                if sbb == 'xx' and scc == 'xx':
                    canvas.create_line(10, 10, 140, 140, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
            else:
                y = 500
                a -= 1
        elif y <= 100:
            if sab == 0:
                y = 75
                sab = 'xx'
                if saa == 'xx' and sac == 'xx':
                    canvas.create_line(25, 10, 25, 140, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
                if sbb == 'xx' and scb == 'xx':
                    canvas.create_line(10, 75, 140, 75, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
            else:
                y = 500
                a -= 1
        elif y<=150:
            if sac == 0:
                y = 125
                sac = 'xx'
                if saa == 'xx' and sab == 'xx':
                    canvas.create_line(25, 10, 25, 140, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
                if sbc == 'xx' and scc == 'xx':
                    canvas.create_line(10, 125, 140, 125, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
                if sbb == 'xx' and sca == 'xx':
                    canvas.create_line(140, 140, 10, 10, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
        elif y<=200:
            if sad == 0 and sz >= 4:
                y = 175
                sad = 'xx'
                if sab == 'xx' and sac == 'xx':
                    canvas.create_line(25, 60, 25, 190, width=4, tags='vec', fill='red')
                    print('Červený vyhral')
                if sbd == 'xx' and scd == 'xx':
                    canvas.create_line(10, 175, 140, 175, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbc == 'xx' and scb == 'xx':
                    canvas.create_line(10, 190, 140, 60, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sae == 'xx' and sac == 'xx':
                    canvas.create_line(25, 240, 25, 110, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
        elif y<=250:
            if sae == 0 and sz == 5:
                y = 225
                sae == 'xx'
                if sad == 'xx' and sac == 'xx':
                    canvas.create_line(25, 240, 25, 110, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbe == 'xx' and sce == 'xx':
                    canvas.create_line(10, 225, 140, 225, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbd == 'xx' and scc == 'xx':
                    canvas.create_line(10, 240, 140, 110, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
            else:
                y = 500
                a -= 1
    elif x <= 100:
        x = 75
        if y <= 50:
            if sba == 0:
                y = 25
                sba = 'xx'
                if sbb == 'xx' and sbc == 'xx':
                    canvas.create_line(75, 10, 75, 140, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
                if saa == 'xx' and sca == 'xx':
                    canvas.create_line(10, 25, 140, 25, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
        elif y <= 100:
            if sbb == 0:
                y = 75
                sbb = 'xx'
                if saa == 'xx' and scc == 'xx':
                    canvas.create_line(10, 10, 140, 140, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
                if sba == 'xx' and sbc == 'xx':
                    canvas.create_line(75, 10, 75, 140, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
                if sac == 'xx' and sca == 'xx':
                    canvas.create_line(10, 140, 140, 10, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
                if sab == 'xx' and scb == 'xx':
                    canvas.create_line(10, 75, 140, 75, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
        elif y<=150:
            if sbc == 0:
                y = 125
                sbc = 'xx'
                if sba == 'xx' and sbb == 'xx':
                    canvas.create_line(75, 10, 75, 140, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
                if sac == 'xx' and scc == 'xx':
                    canvas.create_line(10, 125, 140, 125, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
        elif y<=200:
            if sbd == 0 and sz >= 4:
                y = 175
                sbd = 'xx'
                if sbe == 'xx' and sbc == 'xx':
                    canvas.create_line(75, 240, 75, 110, width=4, fill='red', tags='vec')
                    print('Červený vyhral')#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            else:
                y=500
                a-=1
    elif x <= 150:
        x = 125
        if y <= 50:
            if sca == 0:
                y = 25
                sca = 'xx'
                if sbb == 'xx' and sac == 'xx':
                    canvas.create_line(140, 10, 10, 140, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
                if saa == 'xx' and sba == 'xx':
                    canvas.create_line(10, 25, 140, 25, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
                if scc == 'xx' and scb == 'xx':
                    canvas.create_line(125, 10, 125, 140, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
        elif y <= 100:
            if scb == 0:
                y = 75
                scb = 'xx'
                if sca == 'xx' and scc == 'xx':
                    canvas.create_line(125, 10, 125, 140, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
                if sab == 'xx' and sbb == 'xx':
                    canvas.create_line(10, 75, 140, 75, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
        elif y <= 150:
            if scc == 0:
                y = 125
                scc = 'xx'
                if saa == 'xx' and sbb == 'xx':
                    canvas.create_line(10, 10, 140, 140, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
                if sca == 'xx' and scb == 'xx':
                    canvas.create_line(125, 10, 125, 140, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
                if sac == 'xx' and sbc == 'xx':
                    canvas.create_line(10, 125, 140, 125, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
    canvas.create_line(x-24, y-24, x+24, y+24, width=2, fill='red', tags='vec')
    canvas.create_line(x+24, y-24, x-24, y+24, width=2, fill='red', tags='vec')
def kruzko(xy):
    global saa, sab, sac, sba, sbb, sbc, sca, scb, scc, a, b, c, sz, sad, sbd, scd, sda, sdb, sdc, sdd, sae, sbe, sce, sde, sea, seb, sec, sed, see
    x = xy.x
    y = xy.y
    if x <= 50:
        x = 25
        if y <= 50:
            if saa == 0:
                y = 25
                saa = 'oo'
                if sab == 'oo' and sac == 'oo':
                    canvas.create_line(25, 10, 25, 140, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if sba == 'oo' and sca == 'oo':
                    canvas.create_line(10, 25, 140, 25, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if sbb == 'oo' and scc == 'oo':
                    canvas.create_line(10, 10, 140, 140, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a+=1
        elif y <= 100:
            if sab == 0:
                y = 75
                sab = 'oo'
                if saa == 'oo' and sac == 'oo':
                    canvas.create_line(25, 10, 25, 140, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if sbb == 'oo' and scb == 'oo':
                    canvas.create_line(10, 75, 140, 75, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a+=1
        elif y<=150:
            if sac == 0:
                y = 125
                sac = 'oo'
                if saa == 'oo' and sab == 'oo':
                    canvas.create_line(25, 10, 25, 140, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if sbc == 'oo' and scc == 'oo':
                    canvas.create_line(10, 125, 140, 125, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if sbb == 'oo' and saa == 'oo':
                    canvas.create_line(140, 140, 10, 10, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a+=1
    elif x <= 100:
        x = 75
        if y <= 50:
            if sba == 0:
                y = 25
                sba = 'oo'
                if sbb == 'oo' and sbc == 'oo':
                    canvas.create_line(75, 10, 75, 140, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if saa == 'oo' and sca == 'oo':
                    canvas.create_line(10, 25, 140, 25, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a+=1
        elif y <= 100:
            if sbb == 0:
                y = 75
                sbb = 'oo'
                if saa == 'oo' and scc == 'oo':
                    canvas.create_line(10, 10, 140, 140, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if sba == 'oo' and sbc == 'oo':
                    canvas.create_line(10, 75, 140, 75, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if sac == 'oo' and sca == 'oo':
                    canvas.create_line(10, 140, 140, 10, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if sab == 'oo' and scb == 'oo':
                    canvas.create_line(10, 75, 140, 75, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a+=1
        elif y<=150:
            if sbc == 0:
                y = 125
                sbc = 'oo'
                if sba == 'oo' and sbb == 'oo':
                    canvas.create_line(75, 10, 75, 140, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if sac == 'oo' and scc == 'oo':
                    canvas.create_line(10, 125, 140, 125, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a+=1
    elif x<=150:
        x = 125
        if y <= 50:
            if sca == 0:
                y = 25
                sca = 'oo'
                if sbb == 'oo' and sac == 'oo':
                    canvas.create_line(140, 10, 10, 140, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if saa == 'oo' and sba == 'oo':
                    canvas.create_line(10, 25, 140, 25, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if scc == 'oo' and scb == 'oo':
                    canvas.create_line(125, 10, 125, 140, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a+=1
        elif y <= 100:
            if scb == 0:
                y = 75
                scb = 'oo'
                if sca == 'oo' and scc == 'oo':
                    canvas.create_line(125, 10, 125, 140, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if sab == 'oo' and sbb == 'oo':
                    canvas.create_line(10, 75, 140, 75, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a+=1
        elif y<=150:
            if scc == 0:
                y = 125
                scc = 'oo'
                if saa == 'oo' and sbb == 'oo':
                    canvas.create_line(10, 10, 140, 140, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if sca == 'oo' and scb == 'oo':
                    canvas.create_line(125, 10, 125, 140, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if sac == 'oo' and sbc == 'oo':
                    canvas.create_line(10, 125, 140, 125, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a+=1
    canvas.create_oval(x-25, y-25, x+25, y+25, width=2, outline='blue', tags='vec')
def aa(xy):
    global saa, sab, sac, sba, sbb, sbc, sca, scb, scc, a, b, ctr, sz, sad, sbd, scd, sda, sdb, sdc, sdd, sae, sbe, sce, sde, sea, seb, sec, sed, see
    if a == 0:
        krizko(xy)
        a += 1
    else:
        kruzko(xy)
        a -= 1
    ctr += 1
    if sz == 3:
        if ctr == 9:
            print('Remíza')
    if sz == 4:
        if ctr == 16:
            print('Remíza')
    if sz == 5:
        if ctr == 25:
            print('Remíza')
canvas.create_text(370, 30, text='Piškvorky', font='arial 30')
canvas.create_text(370, 80, text='Hoď tam 3 pre 3x3 rozmer, zvyšok chápeš')
canvas.create_text(370, 100, text='Ľavým hoď križok alebo kružok')
canvas.create_text(370, 120, text='max rozmer je 5x5')
canvas.bind('<Button-1>', aa)
canvas.bind_all('3', tri)
canvas.bind_all('4', štyri)
canvas.bind_all('5', päť)
