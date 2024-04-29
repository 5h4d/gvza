from random import getrandbits

čísla = [getrandbits(128) for x in range(30)]
d2 = nd2 = d7 = 0
for x in čísla:
    print(x)
    d2 += 1 if x % 2 == 0 else 0
    nd2 += 1 if x % 2 != 0 else 0
    d7 += 1 if x % 7 == 0 else 0
print("Počet párnych čísel: " + str(d2))
print("Počet nepárnych čísel: " + str(nd2))
print("Počet čísel deliteľných číslom 7: " + str(d7))
