v1=input('Vlož prerývaný text: ')
v2=''
v3=''
for i in range(len(v1)):
    if i%2==0:
        v2+=v1[i]
    else:
        v3+=v1[i]
print(v2)
print(v3)
