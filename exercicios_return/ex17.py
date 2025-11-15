"""Crie uma função reverso(texto) que retorne o texto invertido."""

def reverso(texto):
    return texto[::-1]

texto = "A vida é bela"
texto_invertido = reverso(texto)
print(texto_invertido)