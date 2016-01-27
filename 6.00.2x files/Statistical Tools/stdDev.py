def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    
    if L == []:
        return float('NaN')

    test = []
    for strings in L:
        test.append(len(strings))

    tot = 0.0

    #calculate mean
    for e in test:
        tot += e
    mean = tot/len(test)

    #calculate SD
    varSum = 0.0
    for e in test:
        varSum += (e-mean)**2
    var = varSum/len(test)

    return var**0.5

L = ['a', 'z', 'p']
print stdDevOfLengths(L)
L = ['apples', 'oranges', 'kiwis', 'pineapples']
print stdDevOfLengths(L)