###TROJUHOLNÍK###
yea=input("trojuholník: ")
for i in range(len(yea)):
    print(yea[i]*(i+1))
print()

###PYRAMÍDA###
yea=int(input("tak daj n: "))
for i in range(yea):
    print(' '*(yea-1-i)+'*'*(2*i+1))
print()

###CIFERNÝ SÚČET###
csum=0
yea=input("číslo na ciferné rozloženie a súčet pls: ")
for i in range(len(yea)):
    print('{}. cifra je: {}'.format(i+1,str(yea)[i]))
    csum+=int(str(yea)[i])
print('Ciferný súčet je: '+str(csum))
print()

###MOCNINY###
yea=int(input("zadaj od: "))
yae=int(input("zadaj do: "))
n=len(str(yae**4))
for i in range(yea,yae+1):
    print('%-{}i%-{}i%-{}i%-{}i'.format(n,n,n,n) % (i,i**2,i**3,i**4))
print()

###NÁSOBILKA###
yea=int(input("zadaj od: "))
yae=int(input("zadaj do: "))
print("toto nejde a neviem ako to spraviť, to je celkom smola, čo?")
for i in range(yea,yae+1):
    print(niečo čo to spraí pls)
