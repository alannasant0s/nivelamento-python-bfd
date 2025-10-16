# Maior entre três números

numero1 = int(input('Insira o primeiro número: '))
numero2 = int(input('Insira o segundo número: '))
numero3 = int(input('Insira o terceiro número: '))

if numero1 > numero2 and numero1 > numero3:
    print(f'O maior número é {numero1}')
elif numero2 > numero1 and numero2 > numero3:
    print(f'O maior número é {numero2}')

else:
    print(f'O maior número é {numero3}')