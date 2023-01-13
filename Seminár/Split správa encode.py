with open('správa.txt','r') as spravenc:
    mirec=spravenc.read()
    x=0
    a1=a2=''
    y=len(mirec)
    while x+1<y:
        a1+=mirec[x]
        a2+=mirec[x+1]
        x+=2
    with open('znaky1.txt','w') as z1:
        z1.write(a1)
    with open('znaky2.txt','w') as z2:
        z2.write(a2)
