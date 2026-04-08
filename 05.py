# Crie uma função que remova a primeira ocorrência de um elemento de uma lista sem utilizar o método remove.

def rem_primeira (lista):
    lista.pop(0)
    return lista

print(rem_primeira([23,43,4,2,21,4]))