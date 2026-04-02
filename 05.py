# Crie uma função que remova a primeira ocorrência de um elemento de uma lista sem utilizar o método remove.

def rem_primeira (lista):
    n = int(input('Digite o número para remover: '))
    for i in range(len(lista)):
        print(lista[i])
        if lista[i] == n:
            lista.pop(i)
    return lista

print(rem_primeira([23,43,4,2,21,4]))