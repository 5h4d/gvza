import tkinter as tk
import random as rnd
c=tk.Canvas(height=240, width=200)
c.pack()


merek=0
for bruh in range(6):
    c.create_line(0,merek,200,merek)
    c.create_line(merek,0,merek,240)
    merek+=40

if rnd.randrange(2)==1:
    aa=1
else:
    aa=0
if rnd.randrange(2)==1:
    ab=1
else:
    ab=0
if rnd.randrange(2)==1:
    ac=1
else:
    ac=0
if rnd.randrange(2)==1:
    ad=1
else:
    ad=0
if rnd.randrange(2)==1:
    ae=1
else:
    ae=0
if rnd.randrange(2)==1:
    af=1
else:
    af=0
if rnd.randrange(2)==1:
    ba=1
else:
    ba=0
if rnd.randrange(2)==1:
    bb=1
else:
    bb=0
if rnd.randrange(2)==1:
    bc=1
else:
    bc=0
if rnd.randrange(2)==1:
    bd=1
else:
    bd=0
if rnd.randrange(2)==1:
    be=1
else:
    be=0
if rnd.randrange(2)==1:
    bf=1
else:
    bf=0
if rnd.randrange(2)==1:
    ca=1
else:
    ca=0
if rnd.randrange(2)==1:
    cb=1
else:
    cb=0
if rnd.randrange(2)==1:
    cc=1
else:
    cc=0
if rnd.randrange(2)==1:
    cd=1
else:
    cd=0
if rnd.randrange(2)==1:
    ce=1
else:
    ce=0
if rnd.randrange(2)==1:
    cf=1
else:
    cf=0
if rnd.randrange(2)==1:
    da=1
else:
    da=0
if rnd.randrange(2)==1:
    db=1
else:
    db=0
if rnd.randrange(2)==1:
    dc=1
else:
    dc=0
if rnd.randrange(2)==1:
    dd=1
else:
    dd=0
if rnd.randrange(2)==1:
    de=1
else:
    de=0
if rnd.randrange(2)==1:
    df=1
else:
    df=0
if rnd.randrange(2)==1:
    ea=1
else:
    ea=0
if rnd.randrange(2)==1:
    eb=1
else:
    eb=0
if rnd.randrange(2)==1:
    ec=1
else:
    ec=0
if rnd.randrange(2)==1:
    ed=1
else:
    ed=0
if rnd.randrange(2)==1:
    ee=1
else:
    ee=0
if rnd.randrange(2)==1:
    ef=1
else:
    ef=0
if rnd.randrange(2)==1:
    fa=1
else:
    fa=0
if rnd.randrange(2)==1:
    fb=1
else:
    fb=0
if rnd.randrange(2)==1:
    fc=1
else:
    fc=0
if rnd.randrange(2)==1:
    fd=1
else:
    fd=0
if rnd.randrange(2)==1:
    fe=1
else:
    fe=0
if rnd.randrange(2)==1:
    ff=1
else:
    ff=0

def yes(xy):
    x=xy.x
    y=xy.y
    if x<40:
        if y<40:
            if aa==0:
                saa=ba+bb+ab
                c.create_text(20,20,text=saa)
c.bind("<Button-1>",yes)
