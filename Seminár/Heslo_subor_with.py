import random
with open('hesielko.txt','w') as jozenk:
    bruh=int(input('Kelo hesielok pls: '))
    for i in range(bruh):
        pssw=''
        for i in range(8):
            pssw+=chr(random.randrange(97,123))
        jozenk.write(pssw+'\n')
