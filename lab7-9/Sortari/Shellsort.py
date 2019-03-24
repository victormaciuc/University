def functie(x):
    return x


def shellSortare(iterable, *, key=functie, reverse=False):
    '''
            Cel mai rau caz: O(n^2)
            Cel mai bun caz: O(n)
            Caz mediu: O(n^2)
            Complexitate de spatiu: O(1)
            '''
    n = len(iterable)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = iterable[i]
            j = i
            while j >= gap and key(iterable[j - gap]) > key(temp):
                iterable[j] = iterable[j - gap]
                j -= gap
            iterable[j] = temp
        gap //= 2
    if (reverse == True):
        return iterable[::-1]
    return iterable
