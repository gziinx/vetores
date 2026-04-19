# Crie uma função que retorne uma nova lista com o quadrado de cada elemento da lista original.

def quadrado(lista):
    l = []
    for i in lista:
        l.append(i**2)
    return l
print(quadrado([2,4,5,6,7]))