def guests(foo):
    global zeny,muzi
    zeny=[]
    muzi=[]
    for i in range(len(foo)):
        tmp=foo[i]
        if tmp[-1:]=='á':
            zeny.append(foo[i])
        else:
            muzi.append(foo[i])
    muzi.sort()
    for i in range(len(muzi)):
        print(muzi[i])
    print()
    for i in range(len(zeny)):
        print(zeny[i])
    return
