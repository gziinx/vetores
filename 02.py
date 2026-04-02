# Crie uma lista vazia e use append para adicionar os números 5, 3, 8, 6 e 1. Imprima a lista resultante.

lista = []
while True:
    n = int(input("Digite o número: "))
    lista.append(n)
    if n == 00:
        break
    print(lista)
    print("Digite '00' para sair!!")