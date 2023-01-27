def sator(foo):
    for i in range(len(foo)):
        if foo[i] != foo[-i-1]:
            return print(foo+' is not a palindrome')
    return print(foo+' is a palindrome')
