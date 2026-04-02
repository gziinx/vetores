#  Crie uma função que faça pesquisa linear em uma lista e retorne o índice do elemento se encontrado ou -1 se não estiver presente.
lista = [2143,243,43,22,134,1]
def pesq_linear(lista):
    n = int(input('Digite o número para pesquisar: '))
    for i in range(len(lista)):
        if lista[i] == n:
            return i
    return -1

print(pesq_linear(lista))