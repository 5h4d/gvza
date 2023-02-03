while True:
    maerk=input('Hoď písmenko pls: ')
    try:
        int(maerk)
    except ValueError:
        if len(maerk)==1:
            break
        else:
            print('Jedno písmenko...')
    else:
        print('Písmenko...')
if maerk in ['a','e','i','o','u','y']:
    print(maerk+' je samohálska')
else:
    print(maerk+' nie je samohláska')
