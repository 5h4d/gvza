while True:
    v1=input('Hoď mi pls nejaké slovo: ')
    v2=input('Ešte jedno rovnako dlhé keby sa dalo: ')
    v3=''
    if len(v1)!=len(v2):
        print('Rovnako dlhé....')
    else:
        print('ight')
        for i in range(len(v1)):
            v3+=v1[i]+v2[i]
        print(v3)
        break
