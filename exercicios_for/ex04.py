#tabuada de um numero informado
n = int(input('Insira um número para saber sua tabuada: '))
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')