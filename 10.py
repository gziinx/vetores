# Crie uma função que encontre e retorne o maior elemento de uma lista.

def maior_ele (lista): 
    maior = 0
    for i in lista:
        if i > maior:
            maior = i
    return maior

print(maior_ele([10,20,30,90,52,34]))