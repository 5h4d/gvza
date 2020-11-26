x = int(input('Aké číselko treba sfaktoriálniť?: '))
y = 1
if x < 0:
    print('Fatkoriál sa dá vypočítať iba z prirodzených čísel, takže tak')
else:
    for i in range(1, x+1):
        y=y*i
        if i != x:
            print(i, end='*')
        else:
            print(i, end='=')
    print(y)
