"""Crie uma função menor_elemento(lista) que retorne o menor valor da lista."""


def menor_elemento(lista):
    menor = min(lista)
    return menor

lista = [0,1,2,3,4,5,6,7,8,9,10]
menor_numero = menor_elemento(lista)
print(f"O menor elemento da lista é {menor_numero}")