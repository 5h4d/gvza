import random
jozenk=open('hesielko.txt','w')
pssw=''
for i in range(8):
    pssw+=chr(random.randrange(97,123))
jozenk.write(pssw)
jozenk.close()
