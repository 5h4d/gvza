with open('znaky1.txt','r') as z1:
    with open('znaky2.txt','r') as z2:
        a1=z1.read()
        a2=z2.read()
        mirec=''
        x=0
        for x in range(len(a1)):
            mirec+=a1[x]+a2[x]
        with open('správa.txt','w') as spravenc:
            spravenc.write(mirec)
