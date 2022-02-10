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
def hiha():
    c.delete('all')
    c.create_text(100,120,text='L',font='arial 40')

def yes(xy):
    x=xy.x
    y=xy.y
    if x<40:
        if y<40:
            if aa==0:
                ctl=ba+bb+ab
                c.create_text(20,20,text=ctl)
            else:
                hiha()
        elif y<80:
            if ab==0:
                ctl=aa+ac+ba+bb+bc
                c.create_text(20,60,text=ctl)
            else:
                hiha()
        elif y<120:
            if ac==0:
                ctl=ab+ad+bb+bc+bd
                c.create_text(20,100,text=ctl)
            else:
                hiha()
        elif y<160:
            if ad==0:
                ctl=ac+ae+bc+bd+be
                c.create_text(20,140,text=ctl)
            else:
                hiha()
        elif y<200:
            if ae==0:
                ctl=ad+af+bd+be+bf
                c.create_text(20,180,text=ctl)
            else:
                hiha()
        elif y<240:
            if af==0:
                ctl=ae+be+bf
                c.create_text(20,220,text=ctl)
            else:
                hiha()
    elif x<80:
        if y<40:
            if ba==0:
                ctl=aa+ab+bb+ca+cb
                c.create_text(60,20,text=ctl)
            else:
                hiha
        elif y<80:
            if bb==0:
                ctl=aa+ab+ac+ba+bc+ca+cb+cc
                c.create_text(60,60,text=ctl)
            else:
                hiha()
        elif y<120:
            if bc==0:
                ctl=ab+ac+ad+bb+bd+cb+cc+cd
                c.create_text(60,100,text=ctl)
            else:
                hiha()
        elif y<160:
            if bd==0:
                ctl=ac+ad+ae+bc+be+cc+cd+ce
                c.create_text(60,140,text=ctl)
            else:
                hiha()
        elif y<200:
            if be==0:
                ctl=ad+ae+af+bd+bf+cd+ce+cf
                c.create_text(60,180,text=ctl)
            else:
                hiha()
        elif y<240:
            if bf==0:
                ctl=ae+af+be+ce+cf
                c.create_text(60,220,text=ctl)
    elif x<120:
        if y<40:
            if ca==0:
                ctl=ba+bb+cb+da+db
                c.create_text(100,20,text=ctl)
            else:
                hiha()
        elif y<80:
            if cb==0:
                ctl=ba+bb+bc+ca+cc+da+db+dc
                c.create_text(100,60,text=ctl)
            else:
                hiha()
        elif y<120:
            if cc==0:
                ctl=bb+bc+bd+cb+cd+db+dc+dd
                c.create_text(100,100,text=ctl)
            else:
                hiha()
        elif y<160:
            if cd==0:
                ctl=bc+bd+be+cc+ce+dc+dd+de
                c.create_text(100,140,text=ctl)
            else:
                hiha()
        elif y<200:
            if ce==0:
                ctl=bd+be+bf+cd+cf+dd+de+df
                c.create_text(100,180,text=ctl)
            else:
                hiha()
        elif y<240:
            if cf==0:
                ctl=be+bf+ce+de+df
                c.create_text(100,220,text=ctl)
    elif x<160:
        if y<40:
            if da==0:
                ctl=ca+cb+db+ea+eb
                c.create_text(140,20,text=ctl)
            else:
                hiha()
        elif y<80:
            if db==0:
                ctl=ca+cb+cc+da+dc+ea+eb+ec
                c.create_text(140,60,text=ctl)
            else:
                hiha()
        elif y<120:
            if dc==0:
                ctl=cb+cc+cd+db+dd+eb+ec+ed
                c.create_text(140,100,text=ctl)
            else:
                hiha()
        elif y<160:
            if dd==0:
                ctl=cc+cd+ce+dc+de+ec+ed+ee
                c.create_text(140,140,text=ctl)
            else:
                hiha()
        elif y<200:
            if de==0:
                ctl=cd+ce+cf+dd+df+ed+ee+ef
                c.create_text(140,180,text=ctl)
            else:
                hiha()
        elif y<240:
            if df==0:
                ctl=ce+cf+de+ee+ef
                c.create_text(140,220,text=ctl)
    elif x<200:
        if y<40:
            if ea==0:
                ctl=da+db+eb
                c.create_text(180,20,text=ctl)
            else:
                hiha()
        elif y<80:
            if eb==0:
                ctl=ea+ec+da+db+dc
                c.create_text(180,60,text=ctl)
            else:
                hiha()
        elif y<120:
            if ec==0:
                ctl=eb+ed+db+dc+dd
                c.create_text(180,100,text=ctl)
            else:
                hiha()
        elif y<160:
            if ed==0:
                ctl=ec+ee+dc+dd+de
                c.create_text(180,140,text=ctl)
            else:
                hiha()
        elif y<200:
            if ee==0:
                ctl=ed+ef+dd+de+df
                c.create_text(180,180,text=ctl)
            else:
                hiha()
        elif y<240:
            if ef==0:
                ctl=ee+de+df
                c.create_text(180,220,text=ctl)
            else:
                hiha()
def no(xy):
    
c.bind("<Button-1>",yes)
c.bind("<Button-2>",no)
