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

global saa, sab, sac, sba, sbb, sbc, sca, scb, scc, a, b, c, sz, sad, sbd, scd, sda, sdb, sdc, sdd, sae, sbe, sce, sde, sea, seb, sec, sed, see, ctr
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
    global saa, sab, sac, sba, sbb, sbc, sca, scb, scc, a, b, c, sz, sad, sbd, scd, sda, sdb, sdc, sdd, sae, sbe, sce, sde, sea, seb, sec, sed, see, ctr
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
                if sac == 'xx' and sad == 'xx':
                    canvas.create_line(25, 60, 25, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbc == 'xx' and scd == 'xx':
                    canvas.create_line(10, 60, 140, 190, width=4, fill='red', tags='vec')
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
                    canvas.create_line(10, 140, 140, 10, fill='red', width=4, tags='vec')
                    print('Červený vyhral')
                if sab == 'xx' and sad == 'xx':
                    canvas.create_line(25, 60, 25, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sad == 'xx' and sae == 'xx':
                    canvas.create_line(25, 160, 25, 290, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbd == 'xx' and sce == 'xx':
                    canvas.create_line(10, 60, 140, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
            else:
                y = 500
                a -= 1
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
            else:
                y = 500
                a -= 1
        elif y<=250:
            if sae == 0 and sz >= 5:
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
                if sca == 'xx' and sda == 'xx':
                    canvas.create_line(60, 25, 190, 25, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scb == 'xx' and sdc == 'xx':
                    canvas.create_line(60, 10, 190, 140, width=4, fill='red', tags='vec')
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
                if scb == 'xx' and sdb == 'xx':
                    canvas.create_line(60, 75, 190, 75, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scc == 'xx' and sdd == 'xx':
                    canvas.create_line(60, 60, 190, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbc == 'xx' and sbd == 'xx':
                    canvas.create_line(75, 60, 75, 190, width=4, fill='red', tags='vec')
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
                if sbb == 'xx' and sbd == 'xx':
                    canvas.create_line(75, 60, 75, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scc == 'xx' and sdc == 'xx':
                    canvas.create_line(60, 175, 190, 175, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scd == 'xx' and sde == 'xx':
                    canvas.create_line(60, 160, 190, 290, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbd == 'xx' and sbe == 'xx':
                    canvas.create_line(75, 110, 75, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
            else:
                y = 500
                a -= 1
        elif y<=200:
            if sbd == 0 and sz >= 4:
                y = 175
                sbd = 'xx'
                if sbe == 'xx' and sbc == 'xx':
                    canvas.create_line(75, 240, 75, 110, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sad == 'xx' and scd == 'xx':
                    canvas.create_line(10, 175, 140, 175, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sac == 'xx' and sce == 'xx':
                    canvas.create_line(10, 110, 140, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scc == 'xx' and sae == 'xx':
                    canvas.create_line(140, 110, 10, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbb == 'xx' and sbc == 'xx':
                    canvas.create_line(75, 60, 75, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scd == 'xx' and sdd == 'xx':
                    canvas.create_line(60, 175, 190, 175, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scc == 'xx' and sdb == 'xx':
                    canvas.create_line(60, 190, 190, 60, width=4, fill='red', tags='vec')
                    print('Červený vyhral')        
            else:
                y=500
                a-=1
        elif y<=250:
            if sbe == 0 and sz == 5:
                y = 225
                sbe = 'xx'
                if sbc == 'xx' and sbd == 'xx':
                    canvas.create_line(75, 110, 75, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sdc == 'xx' and scd == 'xx':
                    canvas.create_line(190, 110, 60, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sae == 'xx' and sce == 'xx':
                    canvas.create_line(10, 225, 140, 225, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sce == 'xx' and sde == 'xx':
                    canvas.create_line(60, 225, 190, 225, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
            else:
                y = 500
                a -= 1
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
                if sba == 'xx' and sda == 'xx':
                    canvas.create_line(60, 25, 190, 25, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sda == 'xx' and sea == 'xx':
                    canvas.create_line(110, 25, 240, 25, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sdb == 'xx' and sec == 'xx':
                    canvas.create_line(10, 110, 140, 240, width=4, fill='red', tags='vec')
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
                if sba == 'xx' and sdc == 'xx':
                    canvas.create_line(60, 10, 190, 140, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sda == 'xx' and sbc == 'xx':
                    canvas.create_line(190, 10, 60, 140, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbb == 'xx' and sdb == 'xx':
                    canvas.create_line(60, 75, 190, 75, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sdb == 'xx' and seb == 'xx':
                    canvas.create_line(110, 75, 240, 75, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sdc == 'xx' and sed == 'xx':
                    canvas.create_line(110, 60, 240, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scc == 'xx' and scd == 'xx':
                    canvas.create_line(60, 125, 190, 125, width=4, fill='red', tags='vec')
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
                if scb == 'xx' and scd == 'xx':
                    canvas.create_line(175, 60, 175, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbc == 'xx' and sdc == 'xx':
                    canvas.create_line(60, 175, 190, 175, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbb == 'xx' and sdd == 'xx':
                    canvas.create_line(60, 60, 190, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sdb == 'xx' and sbd == 'xx':
                    canvas.create_line(190, 60, 60, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sea == 'xx' and sdb == 'xx':
                    canvas.create_line(240, 10, 110, 140, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sdc == 'xx' and sec == 'xx':
                    canvas.create_line(110, 125, 240, 125, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sdd == 'xx' and see == 'xx':
                    canvas.create_line(110, 110, 240, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scd == 'xx' and sce == 'xx':
                    canvas.create_line(125, 110, 125, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
        elif y <= 200:
            if scd == 0 and sz >= 4:
                y = 175
                scd = 'xx'
                if scc == 'xx' and sce == 'xx':
                    canvas.create_line(125, 110, 125, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbd == 'xx' and sdd == 'xx':
                    canvas.create_line(60, 175, 190, 175, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbc == 'xx' and sde == 'xx':
                    canvas.create_line(60, 110, 190, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sdc == 'xx' and sbe == 'xx':
                    canvas.create_line(190, 110, 60, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sab == 'xx' and sbc == 'xx':
                    canvas.create_line(10, 60, 140, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sad == 'xx' and sbd == 'xx':
                    canvas.create_line(10, 175, 140, 175, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scb == 'xx' and scc == 'xx':
                    canvas.create_line(125, 60, 125, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if seb == 'xx' and sdc == 'xx':
                    canvas.create_line(240, 60, 110, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sed == 'xx' and sdd == 'xx':
                    canvas.create_line(110, 175, 240, 175, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
        elif y <= 250:
            if sce == 0 and sz >= 5:
                y = 225
                sce = 'xx'
                if sbe == 'xx' and sde == 'xx':
                    canvas.create_line(60, 225, 190, 225, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sae == 'xx' and sbe == 'xx':
                    canvas.create_line(10, 225, 140, 225, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sac == 'xx' and sbd == 'xx':
                    canvas.create_line(10, 110, 140, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scc == 'xx' and scd == 'xx':
                    canvas.create_line(125, 110, 125, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sec == 'xx' and sdd == 'xx':
                    canvas.create_line(240, 110, 110, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if see == 'xx' and sde == 'xx':
                    canvas.create_line(110, 225, 240, 225, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
    elif x <= 200:
        x=175
        if y <= 50:
            if sda == 0 and sz >= 4:
                sda = 'xx'
                y = 25
                if sca == 'xx' and sea == 'xx':
                    canvas.create_line(110, 25, 240, 25, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sba == 'xx' and sca == 'xx':
                    canvas.create_line(60, 25, 190, 25, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbc == 'xx' and scb == 'xx':
                    canvas.create_line(60, 140, 190, 10, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sdb == 'xx' and sdc == 'xx':
                    canvas.create_line(175, 10, 175, 140, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
        elif y <= 100:
            if sdb == 0 and sz >= 4:
                y = 75
                sdb = 'xx'
                if scb == 'xx' and seb == 'xx':
                    canvas.create_line(110, 75, 240, 75, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sda == 'xx' and sdc == 'xx':
                    canvas.create_line(175, 10, 175, 140, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sca == 'xx' and sec == 'xx':
                    canvas.create_line(110, 10, 240, 140, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sea == 'xx' and scc == 'xx':
                    canvas.create_line(240, 10, 110, 140, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbb == 'xx' and scb == 'xx':
                    canvas.create_line(60, 75, 190, 75, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbd == 'xx' and scc == 'xx':
                    canvas.create_line(60, 190, 190, 60, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sdc == 'xx' and sdd == 'xx':
                    canvas.create_line(175, 60, 175, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
        elif y <= 150:
            if sdc == 0 and sz >= 4:
                y = 125
                sdc = 'xx'
                if sdb == 'xx' and sdd == 'xx':
                    canvas.create_line(175, 60, 175, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scb == 'xx' and sed == 'xx':
                    canvas.create_line(110, 60, 240, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scc == 'xx' and sec == 'xx':
                    canvas.create_line(110, 125, 240, 125, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scd == 'xx' and seb == 'xx':
                    canvas.create_line(110, 190, 240, 60, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sda == 'xx' and sdb == 'xx':
                    canvas.create_line(175, 10, 175, 140, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sba == 'xx' and scb == 'xx':
                    canvas.create_line(60, 10, 190, 140, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbc == 'xx' and scc == 'xx':
                    canvas.create_line(60, 125, 190, 125, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbe == 'xx' and scd == 'xx':
                    canvas.create_line(60, 240, 190, 110, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sdd == 'xx' and sde == 'xx':
                    canvas.create_line(110, 175, 240, 175, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
        elif y <= 200:
            if sdd == 0 and sz >= 4:
                y = 175
                sdd = 'xx'
                if sdc == 'xx' and sde == 'xx':
                    canvas.create_line(175, 110, 175, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scd == 'xx' and sed == 'xx':
                    canvas.create_line(110, 175, 240, 175, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scc == 'xx' and see == 'xx':
                    canvas.create_line(110, 110, 240, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sec == 'xx' and sce == 'xx':
                    canvas.create_line(240, 110, 110, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbb == 'xx' and scc == 'xx':
                    canvas.create_line(60, 60, 190, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sdb == 'xx' and sdc == 'xx':
                    canvas.create_line(175, 60, 175, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbd == 'xx' and scd == 'xx':
                    canvas.create_line(60, 175, 190, 175, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
        elif y <= 250:
            if sde == 0 and sz >= 5:
                y = 225
                sde = 'xx'
                if sce == 'xx' and see == 'xx':
                    canvas.create_line(110, 225, 240, 225, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbe == 'xx' and sce == 'xx':
                    canvas.create_line(60, 225, 190, 225, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sbc == 'xx' and scd == 'xx':
                    canvas.create_line(60, 110, 190, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sdc == 'xx' and sdd == 'xx':
                    canvas.create_line(175, 110, 175, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
    elif x <= 250:
        x = 225
        if y <= 50:
            if sea == 0 and sz >= 5:
                y = 25
                sea = 'xx'
                if sda == 'xx' and sca == 'xx':
                    canvas.create_line(110, 25, 240, 25, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sdb == 'xx' and scc == 'xx':
                    canvas.create_line(110, 110, 240, 10, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if seb == 'xx' and sec == 'xx':
                    canvas.create_line(225, 10, 225, 140, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
        elif y <= 100:
            if seb == 0 and sz >= 5:
                seb = 'xx'
                y = 75
                if sea == 'xx' and sec == 'xx':
                    canvas.create_line(225, 10, 225, 140, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scb == 'xx' and sdb == 'xx':
                    canvas.create_line(110, 75, 240, 75, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scd == 'xx' and sdc == 'xx':
                    canvas.create_line(110, 190, 240, 60, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sec == 'xx' and sed == 'xx':
                    canvas.create_line(225, 60, 225, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
        elif y <= 150:
            if sec == 0 and sz >= 5:
                y=125
                sec = 'xx'
                if seb == 'xx' and sed == 'xx':
                    canvas.create_line(225, 60, 225, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sea == 'xx' and seb == 'xx':
                    canvas.create_line(225, 10, 225, 140, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sca == 'xx' and sdb == 'xx':
                    canvas.create_line(110, 10, 240, 140, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scc == 'xx' and sdc == 'xx':
                    canvas.create_line(110, 125, 240, 125, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sce == 'xx' and sdd == 'xx':
                    canvas.create_line(110, 240, 240, 110, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sed == 'xx' and see == 'xx':
                    canvas.create_line(225, 110, 225, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
        elif y <= 200:
            if sed == 0 and sz >= 5:
                y = 175
                sed = 'xx'
                if sec == 'xx' and see == 'xx':
                    canvas.create_line(225, 110, 225, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if seb == 'xx' and sec == 'xx':
                    canvas.create_line(225, 60, 225, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scb == 'xx' and sdc == 'xx':
                    canvas.create_line(110, 60, 240, 190, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scd == 'xx' and sdd == 'xx':
                    canvas.create_line(110, 175, 240, 175, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
        elif y <= 250:
            if see == 0 and sz >= 5:
                y = 225
                see = 'xx'
                if  sec == 'xx' and sed == 'xx':
                    canvas.create_line(225, 110, 225, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if scc == 'xx' and sdd == 'xx':
                    canvas.create_line(110, 110, 240, 240, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
                if sce == 'xx' and sde == 'xx':
                    canvas.create_line(110, 225, 240, 225, width=4, fill='red', tags='vec')
                    print('Červený vyhral')
            else:
                y=500
                a-=1
    else:
        x=1000
        a-=1
    canvas.create_line(x-24, y-24, x+24, y+24, width=2, fill='red', tags='vec')
    canvas.create_line(x+24, y-24, x-24, y+24, width=2, fill='red', tags='vec')
    if x<500 and y<500:
        ctr+=1
def kruzko(xy):
    global saa, sab, sac, sba, sbb, sbc, sca, scb, scc, a, b, c, sz, sad, sbd, scd, sda, sdb, sdc, sdd, sae, sbe, sce, sde, sea, seb, sec, sed, see, ctr
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
                y = 500
                a -= 1
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
                if sac == 'oo' and sad == 'oo':
                    canvas.create_line(25, 60, 25, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbc == 'oo' and scd == 'oo':
                    canvas.create_line(10, 60, 140, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y = 500
                a -= 1
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
                if sbb == 'oo' and sca == 'oo':
                    canvas.create_line(140, 140, 10, 10, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if sab == 'oo' and sad == 'oo':
                    canvas.create_line(25, 60, 25, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sad == 'oo' and sae == 'oo':
                    canvas.create_line(25, 160, 25, 290, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbd == 'oo' and sce == 'oo':
                    canvas.create_line(10, 60, 140, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y = 500
                a -= 1
        elif y<=200:
            if sad == 0 and sz >= 4:
                y = 175
                sad = 'oo'
                if sab == 'oo' and sac == 'oo':
                    canvas.create_line(25, 60, 25, 190, width=4, tags='vec', fill='blue')
                    print('Modrý vyhral')
                if sbd == 'oo' and scd == 'oo':
                    canvas.create_line(10, 175, 140, 175, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbc == 'oo' and scb == 'oo':
                    canvas.create_line(10, 190, 140, 60, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sae == 'oo' and sac == 'oo':
                    canvas.create_line(25, 240, 25, 110, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y = 500
                a -= 1
        elif y<=250:
            if sae == 0 and sz >= 5:
                y = 225
                sae == 'oo'
                if sad == 'oo' and sac == 'oo':
                    canvas.create_line(25, 240, 25, 110, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbe == 'oo' and sce == 'oo':
                    canvas.create_line(10, 225, 140, 225, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbd == 'oo' and scc == 'oo':
                    canvas.create_line(10, 240, 140, 110, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y = 500
                a -= 1
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
                if sca == 'oo' and sda == 'oo':
                    canvas.create_line(60, 25, 190, 25, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scb == 'oo' and sdc == 'oo':
                    canvas.create_line(60, 10, 190, 140, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a-=1
        elif y <= 100:
            if sbb == 0:
                y = 75
                sbb = 'oo'
                if saa == 'oo' and scc == 'oo':
                    canvas.create_line(10, 10, 140, 140, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if sba == 'oo' and sbc == 'oo':
                    canvas.create_line(75, 10, 75, 140, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if sac == 'oo' and sca == 'oo':
                    canvas.create_line(10, 140, 140, 10, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if sab == 'oo' and scb == 'oo':
                    canvas.create_line(10, 75, 140, 75, fill='blue', width=4, tags='vec')
                    print('Modrý vyhral')
                if scb == 'oo' and sdb == 'oo':
                    canvas.create_line(60, 75, 190, 75, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scc == 'oo' and sdd == 'oo':
                    canvas.create_line(60, 60, 190, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbc == 'oo' and sbd == 'oo':
                    canvas.create_line(75, 60, 75, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a-=1
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
                if sbb == 'oo' and sbd == 'oo':
                    canvas.create_line(75, 60, 75, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scc == 'oo' and sdc == 'oo':
                    canvas.create_line(60, 175, 190, 175, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scd == 'oo' and sde == 'oo':
                    canvas.create_line(60, 160, 190, 290, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbd == 'oo' and sbe == 'oo':
                    canvas.create_line(75, 110, 75, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y = 500
                a -= 1
        elif y<=200:
            if sbd == 0 and sz >= 4:
                y = 175
                sbd = 'oo'
                if sbe == 'oo' and sbc == 'oo':
                    canvas.create_line(75, 240, 75, 110, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sad == 'oo' and scd == 'oo':
                    canvas.create_line(10, 175, 140, 175, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sac == 'oo' and sce == 'oo':
                    canvas.create_line(10, 110, 140, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scc == 'oo' and sae == 'oo':
                    canvas.create_line(140, 110, 10, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbb == 'oo' and sbc == 'oo':
                    canvas.create_line(75, 60, 75, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scd == 'oo' and sdd == 'oo':
                    canvas.create_line(60, 175, 190, 175, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scc == 'oo' and sdb == 'oo':
                    canvas.create_line(60, 190, 190, 60, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')        
            else:
                y=500
                a-=1
        elif y<=250:
            if sbe == 0 and sz == 5:
                y = 225
                sbe = 'oo'
                if sbc == 'oo' and sbd == 'oo':
                    canvas.create_line(75, 110, 75, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sdc == 'oo' and scd == 'oo':
                    canvas.create_line(190, 110, 60, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sae == 'oo' and sce == 'oo':
                    canvas.create_line(10, 225, 140, 225, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sce == 'oo' and sde == 'oo':
                    canvas.create_line(60, 225, 190, 225, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y = 500
                a -= 1
    elif x <= 150:
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
                if sba == 'oo' and sda == 'oo':
                    canvas.create_line(60, 25, 190, 25, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sda == 'oo' and sea == 'oo':
                    canvas.create_line(110, 25, 240, 25, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sdb == 'oo' and sec == 'oo':
                    canvas.create_line(10, 110, 140, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a-=1
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
                if sba == 'oo' and sdc == 'oo':
                    canvas.create_line(60, 10, 190, 140, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sda == 'oo' and sbc == 'oo':
                    canvas.create_line(190, 10, 60, 140, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbb == 'oo' and sdb == 'oo':
                    canvas.create_line(60, 75, 190, 75, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sdb == 'oo' and seb == 'oo':
                    canvas.create_line(110, 75, 240, 75, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sdc == 'oo' and sed == 'oo':
                    canvas.create_line(110, 60, 240, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scc == 'oo' and scd == 'oo':
                    canvas.create_line(60, 125, 190, 125, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a-=1
        elif y <= 150:
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
                if scb == 'oo' and scd == 'oo':
                    canvas.create_line(175, 60, 175, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbc == 'oo' and sdc == 'oo':
                    canvas.create_line(60, 175, 190, 175, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbb == 'oo' and sdd == 'oo':
                    canvas.create_line(60, 60, 190, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sdb == 'oo' and sbd == 'oo':
                    canvas.create_line(190, 60, 60, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sea == 'oo' and sdb == 'oo':
                    canvas.create_line(240, 10, 110, 140, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sdc == 'oo' and sec == 'oo':
                    canvas.create_line(110, 125, 240, 125, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sdd == 'oo' and see == 'oo':
                    canvas.create_line(110, 110, 240, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scd == 'oo' and sce == 'oo':
                    canvas.create_line(125, 110, 125, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a-=1
        elif y <= 200:
            if scd == 0 and sz >= 4:
                y = 175
                scd = 'oo'
                if scc == 'oo' and sce == 'oo':
                    canvas.create_line(125, 110, 125, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbd == 'oo' and sdd == 'oo':
                    canvas.create_line(60, 175, 190, 175, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbc == 'oo' and sde == 'oo':
                    canvas.create_line(60, 110, 190, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sdc == 'oo' and sbe == 'oo':
                    canvas.create_line(190, 110, 60, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sab == 'oo' and sbc == 'oo':
                    canvas.create_line(10, 60, 140, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sad == 'oo' and sbd == 'oo':
                    canvas.create_line(10, 175, 140, 175, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scb == 'oo' and scc == 'oo':
                    canvas.create_line(125, 60, 125, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if seb == 'oo' and sdc == 'oo':
                    canvas.create_line(240, 60, 110, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sed == 'oo' and sdd == 'oo':
                    canvas.create_line(110, 175, 240, 175, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a-=1
        elif y <= 250:
            if sce == 0 and sz >= 5:
                y = 225
                sce = 'oo'
                if sbe == 'oo' and sde == 'oo':
                    canvas.create_line(60, 225, 190, 225, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sae == 'oo' and sbe == 'oo':
                    canvas.create_line(10, 225, 140, 225, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sac == 'oo' and sbd == 'oo':
                    canvas.create_line(10, 110, 140, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scc == 'oo' and scd == 'oo':
                    canvas.create_line(125, 110, 125, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sec == 'oo' and sdd == 'oo':
                    canvas.create_line(240, 110, 110, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if see == 'oo' and sde == 'oo':
                    canvas.create_line(110, 225, 240, 225, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a-=1
    elif x <= 200:
        x=175
        if y <= 50:
            if sda == 0 and sz >= 4:
                sda = 'oo'
                y = 25
                if sca == 'oo' and sea == 'oo':
                    canvas.create_line(110, 25, 240, 25, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sba == 'oo' and sca == 'oo':
                    canvas.create_line(60, 25, 190, 25, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbc == 'oo' and scb == 'oo':
                    canvas.create_line(60, 140, 190, 10, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sdb == 'oo' and sdc == 'oo':
                    canvas.create_line(175, 10, 175, 140, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a-=1
        elif y <= 100:
            if sdb == 0 and sz >= 4:
                y = 75
                sdb = 'oo'
                if scb == 'oo' and seb == 'oo':
                    canvas.create_line(110, 75, 240, 75, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sda == 'oo' and sdc == 'oo':
                    canvas.create_line(175, 10, 175, 140, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sca == 'oo' and sec == 'oo':
                    canvas.create_line(110, 10, 240, 140, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sea == 'oo' and scc == 'oo':
                    canvas.create_line(240, 10, 110, 140, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbb == 'oo' and scb == 'oo':
                    canvas.create_line(60, 75, 190, 75, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbd == 'oo' and scc == 'oo':
                    canvas.create_line(60, 190, 190, 60, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sdc == 'oo' and sdd == 'oo':
                    canvas.create_line(175, 60, 175, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a-=1
        elif y <= 150:
            if sdc == 0 and sz >= 4:
                y = 125
                sdc = 'oo'
                if sdb == 'oo' and sdd == 'oo':
                    canvas.create_line(175, 60, 175, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scb == 'oo' and sed == 'oo':
                    canvas.create_line(110, 60, 240, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scc == 'oo' and sec == 'oo':
                    canvas.create_line(110, 125, 240, 125, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scd == 'oo' and seb == 'oo':
                    canvas.create_line(110, 190, 240, 60, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sda == 'oo' and sdb == 'oo':
                    canvas.create_line(175, 10, 175, 140, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sba == 'oo' and scb == 'oo':
                    canvas.create_line(60, 10, 190, 140, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbc == 'oo' and scc == 'oo':
                    canvas.create_line(60, 125, 190, 125, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbe == 'oo' and scd == 'oo':
                    canvas.create_line(60, 240, 190, 110, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sdd == 'oo' and sde == 'oo':
                    canvas.create_line(110, 175, 240, 175, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a-=1
        elif y <= 200:
            if sdd == 0 and sz >= 4:
                y = 175
                sdd = 'oo'
                if sdc == 'oo' and sde == 'oo':
                    canvas.create_line(175, 110, 175, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scd == 'oo' and sed == 'oo':
                    canvas.create_line(110, 175, 240, 175, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scc == 'oo' and see == 'oo':
                    canvas.create_line(110, 110, 240, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sec == 'oo' and sce == 'oo':
                    canvas.create_line(240, 110, 110, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbb == 'oo' and scc == 'oo':
                    canvas.create_line(60, 60, 190, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sdb == 'oo' and sdc == 'oo':
                    canvas.create_line(175, 60, 175, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbd == 'oo' and scd == 'oo':
                    canvas.create_line(60, 175, 190, 175, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a-=1
        elif y <= 250:
            if sde == 0 and sz >= 5:
                y = 225
                sde = 'oo'
                if sce == 'oo' and see == 'oo':
                    canvas.create_line(110, 225, 240, 225, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbe == 'oo' and sce == 'oo':
                    canvas.create_line(60, 225, 190, 225, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sbc == 'oo' and scd == 'oo':
                    canvas.create_line(60, 110, 190, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sdc == 'oo' and sdd == 'oo':
                    canvas.create_line(175, 110, 175, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a-=1
    elif x <= 250:
        x = 225
        if y <= 50:
            if sea == 0 and sz >= 5:
                y = 25
                sea = 'oo'
                if sda == 'oo' and sca == 'oo':
                    canvas.create_line(110, 25, 240, 25, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sdb == 'oo' and scc == 'oo':
                    canvas.create_line(110, 110, 240, 10, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if seb == 'oo' and sec == 'oo':
                    canvas.create_line(225, 10, 225, 140, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a-=1
        elif y <= 100:
            if seb == 0 and sz >= 5:
                seb = 'oo'
                y = 75
                if sea == 'oo' and sec == 'oo':
                    canvas.create_line(225, 10, 225, 140, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scb == 'oo' and sdb == 'oo':
                    canvas.create_line(110, 75, 240, 75, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scd == 'oo' and sdc == 'oo':
                    canvas.create_line(110, 190, 240, 60, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sec == 'oo' and sed == 'oo':
                    canvas.create_line(225, 60, 225, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a-=1
        elif y <= 150:
            if sec == 0 and sz >= 5:
                y=125
                sec = 'oo'
                if seb == 'oo' and sed == 'oo':
                    canvas.create_line(225, 60, 225, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sea == 'oo' and seb == 'oo':
                    canvas.create_line(225, 10, 225, 140, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sca == 'oo' and sdb == 'oo':
                    canvas.create_line(110, 10, 240, 140, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scc == 'oo' and sdc == 'oo':
                    canvas.create_line(110, 125, 240, 125, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sce == 'oo' and sdd == 'oo':
                    canvas.create_line(110, 240, 240, 110, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sed == 'oo' and see == 'oo':
                    canvas.create_line(225, 110, 225, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a-=1
        elif y <= 200:
            if sed == 0 and sz >= 5:
                y = 175
                sed = 'oo'
                if sec == 'oo' and see == 'oo':
                    canvas.create_line(225, 110, 225, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if seb == 'oo' and sec == 'oo':
                    canvas.create_line(225, 60, 225, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scb == 'oo' and sdc == 'oo':
                    canvas.create_line(110, 60, 240, 190, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scd == 'oo' and sdd == 'oo':
                    canvas.create_line(110, 175, 240, 175, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a-=1
        elif y <= 250:
            if see == 0 and sz >= 5:
                y = 225
                see = 'oo'
                if  sec == 'oo' and sed == 'oo':
                    canvas.create_line(225, 110, 225, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if scc == 'oo' and sdd == 'oo':
                    canvas.create_line(110, 110, 240, 240, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
                if sce == 'oo' and sde == 'oo':
                    canvas.create_line(110, 225, 240, 225, width=4, fill='blue', tags='vec')
                    print('Modrý vyhral')
            else:
                y=500
                a-=1
    else:
        x=1000
        a-=1
    canvas.create_oval(x-24, y-24, x+24, y+24, width=2, outline='blue', tags='vec')
    if x<500 and y<500:
        ctr+=1
def aa(xy):
    global saa, sab, sac, sba, sbb, sbc, sca, scb, scc, a, b, ctr, sz, sad, sbd, scd, sda, sdb, sdc, sdd, sae, sbe, sce, sde, sea, seb, sec, sed, see, ctr
    if a == 0:
        krizko(xy)
        a += 1
    else:
        kruzko(xy)
        a -= 1
    if ctr == sz*sz:
        print('Remíza')
canvas.create_text(370, 30, text='Piškvorky', font='arial 30')
canvas.create_text(370, 80, text='Hoď tam 3 pre 3x3 rozmer, zvyšok chápeš')
canvas.create_text(370, 100, text='Ľavým hoď križok alebo kružok')
canvas.create_text(370, 120, text='max rozmer je 5x5')
canvas.create_text(370, 140, text='Nastavením veľkosti sa taktiež resetuje hra')
canvas.create_text(370, 160, text='Hrá sa do troch')
canvas.bind('<Button-1>', aa)
canvas.bind_all('3', tri)
canvas.bind_all('4', štyri)
canvas.bind_all('5', päť)
