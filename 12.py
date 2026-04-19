#  Crie uma função que conte quantas vezes um dado elemento aparece em uma lista

def conta(lista):
    p = int(input("Digite o numero que voce deseja: "))
    contador = 0
    for i in lista:
        if p == i:
            contador +=1
    return contador

print(conta([12,3,43,2,12,12]))