# Crie uma função que encontre e retorne o menor elemento de uma lista.

def menor_ele(lista):
    l = len(lista)
    print(l[1])
    for i in range(l):
        if l[i] < l[i+1]:
            menor = i
    return menor

print(menor_ele([10,20,30,90,52,34]))