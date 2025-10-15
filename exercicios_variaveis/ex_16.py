#Peça 2 números e mostre o maior

escolha1 = int(input('Insira o primeiro número: '))
escolha2 = int(input('Insira o segundo número: '))

if escolha1 > escolha2:
    print(f'O maior número é o {escolha1}')
elif escolha1 == escolha2:
    print('Os números são iguais')
else:
    print(f'O maior número é o {escolha2}')