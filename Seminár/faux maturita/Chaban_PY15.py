n = input("n = ")
try:
    if int(n) >= 1 and n.isdigit():
        fib = [1, 1]
        while len(fib) < int(n):
            fib.append(fib[-1] + fib[-2])
        print(fib[-1])
    else:
        print(n + " nie je platný vstup")
except:
    print(n + " nie je platný vstup")
