# Crie uma função que receba uma lista e retorne a soma de todos os seus elementos.

def soma_lista (lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

print(soma_lista([1,2,3,4,5]))