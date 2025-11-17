"""Crie uma função contar_palavras(frase) que retorne o número de palavras de uma frase."""

def contar_palavras(frase):
    contador = frase.split()
    contador1 = len(contador) 
    return contador1
            
frase = input("Insira a sua frase: ")
contador = contar_palavras(frase)
print(contador)
    