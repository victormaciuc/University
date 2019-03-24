def functie(x):
    return x

def bonu (iterable,*, key = functie, reverse = False):

n = len(aux)
        for i in range(1, n):
            key = aux[i]
            j = i-1
            while j >=0 and key < aux[j] :
                aux[j+1] = aux[j]
                j -= 1
            aux[j+1] = key
        return aux