s1=''
s=input("Napíš čosi ig: ")
while len(s1)!=len(s):
    s1+=s[-1-len(s1)]
print(s1)
