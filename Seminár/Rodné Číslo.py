from datetime import date
while True:
    rc=input('Aké je tvoje rodné číslo? (Vo formáte YYMMDD/XXXX): ')
    if len(rc)==11 and rc[6]=='/' and int(rc[4:6])<=31:
        if int(rc[2:4])<=12 or 50<int(rc[2:4])<63:
            if int(rc[2:4])<=12:
                m=rc[2:4]
            else:
                m=int(rc[2:4])-50
            if int(rc[:2])<int(str(date.today().year)[2:4]):
                print('Dátum narodenia: '+rc[4:6]+'.'+str(m)+'.20'+rc[:2])
            else:
                print('Dátum narodenia: '+rc[4:6]+'.'+str(m)+'.19'+rc[:2])
            break
    else:
        print('Zlý formát bby')
if int(rc[2:4])<=12:
    print('Pohlavie: M')
else:
    print('Pohlavie: F')
