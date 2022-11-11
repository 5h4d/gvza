import random
while True:
    pssw=''
    for i in range(8):
        pssw+=chr(random.randrange(97,123))
    print(pssw)
    input("")
