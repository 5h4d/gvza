import random as rng
meno = input('Ako sa voláš? ')
print('Ahoj '+meno+' rád Ťa spoznávam :) ')
while True:
    try:
        rok = int(input(meno+' v ktorom roku si sa narodil? '))
        break
    except ValueError:
        print('rok ty tupe vajco')
vek=2022-rok
print('Ah yes, čiže máš '+str(vek)+' rokov, toľko má aj ' +rng.choice(('Gregor', 'Maroš', 'Ignác', 'Istvany', 'Burgir')))
dm = input('Mimochodom, aký máš názor na drogériu? ')
if dm=='excelentná vec':
    print('Výborne ja si tiež myslím že drogéria je '+dm)
elif vek<100:
    print('Sorry ale tvoj názor nie je dostatočne pozitívny aby mohol byť vnímaný ako správny')
    print('Mimochodom do smrti ti zostáva pri najlepšom ' +str(100-vek)+ ' rokov, to je dosť času aby si si svoj názor lepšie premyslel/-a')
else:
    print('Hádal by som sa s tebou ale ako '+str(vek)+'-ročný nesmrteľník toho asi vieš viac.')
