# Maior número ímpar de 5 entradas

numeros = []
for i in range(5):
    n = int(input('Insira um número inteiro: '))
    if n % 2 != 0:
        numeros.append(n)
print(f'O maior número impar inserido é: {max(numeros)}')
