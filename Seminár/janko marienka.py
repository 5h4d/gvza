def heslo():
    kľúč={"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, 'i':9, 'j':15, 'k':16, 'l':17, 'm':18, 'n':19, 'o':25, 'p':26, 'q':27, 'r':28, 's':29, 't':35, 'u':36, 'v':37, 'w':38, 'x':39, 'y':45, 'z':46, "!":47, "?":48}
    rev_kľúč={y: x for x,y in kľúč.items()}
    vec: str=input('šifra alebo string: ')
    out=[]
    if vec[0].isnumeric():
        slova=vec.split(",")
        for slovo in slova:
            pismena=[int(x) for x in slovo.split()]
            for pismeno in pismena:
                out.append(rev_kľúč[pismeno/5])
            out.append(" ")
    else:
        slova = vec.lower().split()
        for slovo in slova:
            pismena = list(slovo)
            for pismeno in pismena:
                out.append(str(kľúč[pismeno]*5))
                out.append(' ')
            out.pop()
            out.append(', ')
        out.pop()
    print("".join(out))
heslo()