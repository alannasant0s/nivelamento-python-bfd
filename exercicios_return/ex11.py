"""Crie uma função hipotenusa(cat1, cat2) que retorne o valor da hipotenusa."""
import math

def hipotenusa(cat1, cat2):
    return math.sqrt(cateto1**2 + cateto2**2)

cateto1 = float(input("Insira o valor do cat1: "))
cateto2 = float(input("Insira o valor do cat2: "))

calculo_hipotenusa = hipotenusa(cateto1, cateto2)
print(f"A hipotenusa é: {calculo_hipotenusa}")
