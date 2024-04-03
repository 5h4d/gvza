infile=input("názov súboru: ")
print()
n=0
k=0
with open(infile) as file:
    og=file.read()
    veci=[x for x in og]
    for y in range(len(veci)):
        n+=1 if veci[y]!='\n' else 0
        k+=1 if veci[y]=='k' else 0
        veci[y]='m' if veci[y]=='k' else veci[y]
    veci=''.join(veci)
    print('počet znakov: '+str(n))
    print('počet k: '+str(k))
    print('originálny text:\n'+og)
    print()
    print('nový text:\n'+veci)