"""Crie uma função media(a, b, c) que retorne a média de três números."""

def media(a,b,c):
    media_numeros = (a+b+c) / 3
    return media_numeros


resultado = media(7,15,87)
print(f"{resultado:.2f}")