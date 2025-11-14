"""Crie uma função celsius_para_fahrenheit(c) que retorne o valor convertido para Fahrenheit."""

def celsius_para_fahrenheit(c):
    return 1.8 * c + 32

c = float(input("Insira os graus em Celsius para ser convertido em Fahrenheit: "))
conversao = celsius_para_fahrenheit(c)
print(f"A temperatura de {c} graus Celsius equivale a {conversao} graus em Fahrenheit ")