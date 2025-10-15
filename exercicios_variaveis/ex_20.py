#Peça um número e mostre se é par ou ímpar

escolha1 = int(input('Insira um número para saber se é par ou ímpar: '))

if escolha1 % 2 != 0:
    print('O número é ímpar')
else:
    print('O número é par')