#Número positivo ou negativo.

escolha1 = int(input('Insira um número: '))
if escolha1 > 0:
    print('O número é positivo')
elif escolha1 == 0:
    print('Você inseriu 0, digite outro número')
else:
    print('O número é negativo')