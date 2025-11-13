"""Crie uma função par(n) que retorne True se o número for par, senão False.
"""
def par(x):
    if x % 2 == 0:
        return True
    else:
        return False

numero_par = par(15)
print(numero_par)