from random import randrange

while True:
    print(
        chr(randrange(97, 123))     #od 'a' po 'z'
        + chr(randrange(97, 123))   #od 'a' po 'z'
        + str(randrange(10, 100))   #od 10 po 99
        + chr(randrange(65, 91))    #od 'A' po 'Z'
        + chr(randrange(65, 91))    #od 'A' po 'Z'
        + str(randrange(10, 100))   #od 10 po 99
    )
    input()
