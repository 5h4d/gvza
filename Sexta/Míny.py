import tkinter as tk
import random as rnd
c=tk.Canvas(height=240, width=200)
c.pack()

try:
    diff=int(input("Kelo bomba?(5): "))
except(SyntaxError,ValueError):
    diff=5

merek=0
for bruh in range(6):
    c.create_line(0,merek,200,merek)
    c.create_line(merek,0,merek,240)
    merek+=40
    
bombi=rnd.sample(['aa','ab','ac','ad','ae','af','ba','bb','bc','bd','be','bf','ca','cb','cc','cd','ce','cf','da','db','dc','dd','de','df','ea','eb','ec','ed','ee','ef'],k=diff)

if 'aa' in bombi:
    aa=1
else:
    aa=0
if 'ab' in bombi:
    ab=1
else:
    ab=0
if 'ac' in bombi:
    ac=1
else:
    ac=0
if 'ad' in bombi:
    ad=1
else:
    ad=0
if 'ae' in bombi:
    ae=1
else:
    ae=0
if 'af' in bombi:
    af=1
else:
    af=0
if 'ba' in bombi:
    ba=1
else:
    ba=0
if 'bb' in bombi:
    bb=1
else:
    bb=0
if 'bc' in bombi:
    bc=1
else:
    bc=0
if 'bd' in bombi:
    bd=1
else:
    bd=0
if 'be' in bombi:
    be=1
else:
    be=0
if 'bf' in bombi:
    bf=1
else:
    bf=0
if 'ca' in bombi:
    ca=1
else:
    ca=0
if 'cb' in bombi:
    cb=1
else:
    cb=0
if 'cc' in bombi:
    cc=1
else:
    cc=0
if 'cd' in bombi:
    cd=1
else:
    cd=0
if 'ce' in bombi:
    ce=1
else:
    ce=0
if 'cf' in bombi:
    cf=1
else:
    cf=0
if 'da' in bombi:
    da=1
else:
    da=0
if 'db' in bombi:
    db=1
else:
    db=0
if 'dc' in bombi:
    dc=1
else:
    dc=0
if 'dd' in bombi:
    dd=1
else:
    dd=0
if 'de' in bombi:
    de=1
else:
    de=0
if 'df' in bombi:
    df=1
else:
    df=0
if 'ea' in bombi:
    ea=1
else:
    ea=0
if 'eb' in bombi:
    eb=1
else:
    eb=0
if 'ec' in bombi:
    ec=1
else:
    ec=0
if 'ed' in bombi:
    ed=1
else:
    ed=0
if 'ee' in bombi:
    ee=1
else:
    ee=0
if 'ef' in bombi:
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
            else:
                hiha()
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
            else:
                hiha()
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
def bobma(x,y,yis):
    c.create_line(x-15,y+15,x+15,y+15,width=5,tags=yis)
    c.create_line(x,y+15,x,y-15,width=5,tags=yis)
    c.create_polygon(x-2,y-14,x-2,y,x-17,y-9,fill='red',outline='red',tags=yis)
vaa=vab=vac=vad=vae=vaf=vba=vbb=vbc=vbd=vbe=vbf=vca=vcb=vcc=vcd=vce=vcf=vda=vdb=vdc=vdd=vde=vdf=vea=veb=vec=ved=vee=vef=0
def no(xy):
    global vaa,vab,vac,vad,vae,vaf,vba,vbb,vbc,vbd,vbe,vbf,vca,vcb,vcc,vcd,vce,vcf,vda,vdb,vdc,vdd,vde,vdf,vea,veb,vec,ved,vee,vef
    x=xy.x
    y=xy.y
    if x<40:
        if y<40:
            if vaa==1:
                c.delete('vaa')
                vaa=0
            else:
                bobma(20,20,'vaa')
                vaa=1
        elif y<80:
            if vab==1:
                c.delete('vab')
                vab=0
            else:
                bobma(20,60,'vab')
                vab=1
        elif y<120:
            if vac==1:
                c.delete('vac')
                vac=0
            else:
                bobma(20,100,'vac')
                vac=1
        elif y<160:
            if vad==1:
                c.delete('vad')
                vad=0
            else:
                bobma(20,140,'vad')
                vad=1
        elif y<200:
            if vae==1:
                c.delete('vae')
                vae=0
            else:
                bobma(20,180,'vae')
                vae=1
        elif y<240:
            if vaf==1:
                c.delete('vaf')
                vaf=0
            else:
                bobma(20,220,'vaf')
                vaf=1
    elif x<80:
        if y<40:
            if vba==1:
                c.delete('vba')
                vba=0
            else:
                bobma(60,20,'vba')
                vba=1
        elif y<80:
            if vbb==1:
                c.delete('vbb')
                vbb=0
            else:
                bobma(60,60,'vbb')
                vbb=1
        elif y<120:
            if vbc==1:
                c.delete('vbc')
                vbc=0
            else:
                bobma(60,100,'vbc')
                vbc=1
        elif y<160:
            if vbd==1:
                c.delete('vbd')
                vbd=0
            else:
                bobma(60,140,'vbd')
                vbd=1
        elif y<200:
            if vbe==1:
                c.delete('vbe')
                vbe=0
            else:
                bobma(60,180,'vbe')
                vbe=1
        elif y<240:
            if vbf==1:
                c.delete('vbf')
                vbf=0
            else:
                bobma(60,220,'vbf')
                vbf=1
    elif x<120:
        if y<40:
            if vca==1:
                c.delete('vca')
                vca=0
            else:
                bobma(100,20,'vca')
                vca=1
        elif y<80:
            if vcb==1:
                c.delete('vcb')
                vcb=0
            else:
                bobma(100,60,'vcb')
                vcb=1
        elif y<120:
            if vcc==1:
                c.delete('vcc')
                vcc=0
            else:
                bobma(100,100,'vcc')
                vcc=1
        elif y<160:
            if vcd==1:
                c.delete('vcd')
                vcd=0
            else:
                bobma(100,140,'vcd')
                vcd=1
        elif y<200:
            if vce==1:
                c.delete('vce')
                vce=0
            else:
                bobma(100,180,'vce')
                vce=1
        elif y<240:
            if vcf==1:
                c.delete('vcf')
                vcf=0
            else:
                bobma(100,220,'vcf')
                vcf=1
    elif x<160:
        if y<40:
            if vda==1:
                c.delete('vda')
                vda=0
            else:
                bobma(140,20,'vda')
                vda=1
        elif y<80:
            if vdb==1:
                c.delete('vdb')
                vdb=0
            else:
                bobma(140,60,'vdb')
                vdb=1
        elif y<120:
            if vdc==1:
                c.delete('vdc')
                vdc=0
            else:
                bobma(140,100,'vdc')
                vdc=1
        elif y<160:
            if vdd==1:
                c.delete('vdd')
                vdd=0
            else:
                bobma(140,140,'vdd')
                vdd=1
        elif y<200:
            if vde==1:
                c.delete('vde')
                vde=0
            else:
                bobma(140,180,'vde')
                vde=1
        elif y<240:
            if vdf==1:
                c.delete('vdf')
                vdf=0
            else:
                bobma(140,220,'vdf')
                vdf=1
    elif x<200:
        if y<40:
            if vea==1:
                c.delete('vea')
                vea=0
            else:
                bobma(180,20,'vea')
                vea=1
        elif y<80:
            if veb==1:
                c.delete('veb')
                veb=0
            else:
                bobma(180,60,'veb')
                veb=1
        elif y<120:
            if vec==1:
                c.delete('vec')
                vec=0
            else:
                bobma(180,100,'vec')
                vec=1
        elif y<160:
            if ved==1:
                c.delete('ved')
                ved=0
            else:
                bobma(180,140,'ved')
                ved=1
        elif y<200:
            if vee==1:
                c.delete('vee')
                vee=0
            else:
                bobma(180,180,'vee')
                vee=1
        elif y<240:
            if vef==1:
                c.delete('vef')
                vef=0
            else:
                bobma(180,220,'vef')
                vef=1
c.bind("<Button-1>",yes)
c.bind("<Button-3>",no)
