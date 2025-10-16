#Maior entre dois números


numero1 = int(input('Insira um número: '))
numero2 = int(input('Insira o segundo número: '))

if numero1 > numero2:
    print(f'O maior número é {numero1}')
elif numero1 == numero2:
    print('Os números são iguais')
else:
    print(f'O maior número é {numero2}')