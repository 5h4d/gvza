def dh(hodini):     #prepočíta hodiny na dni a hodiny
    if abs(hodini)==1:
        h='hodina'
    elif 1<abs(hodini)<5:
        h='hodiny'
    else:
        h='hodín'
    if abs(hodini%24)==1:
        hh='hodina'
    elif 1<abs(hodini%24)<5:
        hh='hodiny'
    else:
        hh='hodín'
    if abs(hodini//24)==1:
        d='deň'
    elif 1<abs(hodini//24)<5:
        d='dni'
    else:
        d='dní'
    print("{} {} je {} {} a {} {}".format(hodini,h,hodini//24,d,hodini%24,hh))


def sm(minuti):    #prepočíta minúty na stupne a minúty
    print("{}'={}°{}'".format(minuti,minuti//60,minuti%60))

def splatky(spl):   #vypčíta koľko rokov a mesiacov zadlženia zostáva
    rok=spl//12
    mesac=spl%12
    if abs(rok)==1:
        z='zostáva'
        r='rok'
    elif 1<abs(rok)<5:
        z='zostávajú'
        r='roky'
    else:
        z='zostáva'
        r='rokov'
    if abs(mesac)==1:
        m='mesiac'
    elif 1<abs(mesac)<5:
        m='mesiace'
    else:
        m='mesiacov'
    print("{} {} {} a {} {}".format(z,rok,r,mesac,m))

def pozicka(pozicka, splatka):      #vypočíta roky a mesiace zadlženia + doplatok
    num=pozicka//splatka
    doplatok=pozicka%splatka
    rok=num//12
    mesac=num%12
    if abs(rok)==1:
        r='rok'
    elif 1<abs(rok)<5:
        r='roky'
    else:
        r='rokov'
    if abs(mesac)==1:
        m='mesiac'
    elif 1<abs(mesac)<5:
        m='mesiace'
    else:
        m='mesiacov'
    print("Pôžičku splatíte za {} {} a {} {} a doplatok bude {}€".format(rok,r,mesac,m,doplatok))

def mincovka(moni): #rozpočíta peniaz na počet denominácií
    bankovky=[500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
    veci=[]
    while moni>0:
        i=0
        while moni//bankovky[i]<1:
            i+=1
        veci.append("{}x{}€".format(round(moni//bankovky[i]),bankovky[i]))
        moni-=round(moni//bankovky[i])*bankovky[i]
        moni=round(moni,2)
    print(veci)
