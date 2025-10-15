#Peça 2 números e mostre o menor

escolha1 = int(input('Insira o primeiro número: '))
escolha2 = int(input('Insira o segundo número: '))

if escolha1 < escolha2:
    print(f'O menor número é o {escolha1}')
elif escolha1 == escolha2:
    print('Os números são iguais')
else:
    print(f'O menor número é o {escolha2}')