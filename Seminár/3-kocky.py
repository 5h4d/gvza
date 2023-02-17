from random import randint
bochnik = [0]*16
rohlik = int(input("Koľko krát hádžeme?: "))
for i in range(rohlik):
    zemla=0
    for i in range(3):
        zemla+=randint(1,6)
    bochnik[zemla-3]+=1
for i in range(16):
    print("{} sme hodili {}-krát".format(str(3+i),bochnik[i]))
