s1 = ""
s = input("Napíš čosi ig: ")
for i in range(len(s)):
    s1 += s[-1 - i]
print(s1)
