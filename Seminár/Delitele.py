from math import sqrt
def delitel(foo):
    mirec=1
    bar=[]
    while mirec <= foo:
        if foo%mirec==0:
            bar.append(mirec)
        mirec+=1
    return bar
