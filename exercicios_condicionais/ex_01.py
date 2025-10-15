# Leia um número e diga se ele é maior que 10

numero = int(input('Insira um número: '))
if numero > 10:
    print(f'O número {numero} é maior que 10.')
elif numero == 10:
    print('O número inserido é igual a 10.')
else:
    print('O número {numero} é menor que 10.')
