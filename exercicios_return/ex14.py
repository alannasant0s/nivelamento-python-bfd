"""Crie uma função contador_vogais(texto) que retorne quantas vogais existem na string"""

def contador_vogais(texto):
    contador = 0
    for i in texto:
        if i in "aeiouAEIOU":
            contador += 1
    return contador 
            

texto = input("Insira o seu texto aqui: ")
contador = contador_vogais(texto)
print(f"O texto inserido possui {contador} vogais.")