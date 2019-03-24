def functie(x):
    return x

def bubleSortare (iterable,*, key = functie, reverse = False):
    n = len(iterable)
    for i in range(n):
        for j in range(0, n - i - 1):
            if key(iterable[j]) > key(iterable[j + 1]):
                iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]
    if (reverse == True):
        return iterable[::-1]
    return iterable
