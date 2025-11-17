"""Crie uma função soma_lista(lista) que retorne a soma de todos os elementos de uma lista"""

def soma_lista(lista):
    soma = sum(lista)
    return soma

lista = [5, 8 ,9 , 4, 6]
soma = soma_lista(lista)
print(f"A soma dos elementos da lista é {soma}")