n = int(input("Číslo: "))
divs = [x if n % x == 0 else 0 for x in range(1, n)]
print("Súčet deliteľov je " + str(sum(divs)))
if sum(divs) == n:
    print(str(n) + " je dokonalé číslo")
