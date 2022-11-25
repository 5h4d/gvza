from random import randrange
p1=('Jožek', 'Madrid', 'Ignác', 'Istvany', 'Grco')
p2=('prezradil','stratil','ukryl','preklial','spapal')
p3=('rožok','tajomstvo','kľúče','prihlasovacie údaje na portál www.bazos.sk, kde si človek möže kúpiť mnoho zaujímavých vecí za zaujímavé ceny. www.bazos.sk, kde sny sa stávajú cenovo dostupnými')

print(p1[randrange(len(p1))]+' '+p2[randrange(len(p2))]+' '+p3[randrange(len(p3))])
