print('a*x+b=c')
try:
    a = int(input('a = ?: '))
    b = int(input('b = ?: '))
    c = int(input('c = ?: '))
    try:
        print('x = ', (c-b)/a)
    except ZeroDivisionError:
     print('Tak akože toto by mohlo byť úplne hocičo, vráť sa s lepším číslom.')
except ValueError:
    print('Haló? Neviem čo si tam akože zadal ale čislo to nebude...')

