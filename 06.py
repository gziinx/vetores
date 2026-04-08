#  Crie uma função que insira um elemento em uma lista ordenada, mantendo a ordem sem usar sort.
lista = [56,58]
def ins_ord(list, n):
    posicao = 0
    while posicao < len(list) and list[posicao] < n:
        posicao += 1
    list.insert(posicao, n)
    return list
print(ins_ord(lista, 57))