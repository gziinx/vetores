# Crie uma função que retorne uma nova lista contendo apenas os números pares de uma lista dada.

def par(lista):
    l = []
    for i in lista:
        if i % 2 == 0:
            l.append(i)
    return l
print(par([2,4,5,6,7]))