from random import randint as rng

a=rng(1,6)
b=rng(1,6)
c=rng(1,6)

print(a,b,c)
print('VÝHRA' if a==b==c else 'SKORO' if a==b or a==c or b==c else 'PREHRA')