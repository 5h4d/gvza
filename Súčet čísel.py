x = int(input('Najmemšie číslo: '))
y = int(input('Najväčšie čislo: '))
z = 0
for i in range(x, y+1):
    z=z+i
    if i != y:
        print(i, end='+')
    else:
        print(i, end='=')
print(z)
