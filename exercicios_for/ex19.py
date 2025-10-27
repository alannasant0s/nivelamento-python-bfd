#Lista com 10 elementos e seus índices 

numeros = []
for i in range(10):
    numeros.append(int(input('Insira o numero: ')))
for posicao, num in enumerate(numeros):
    print(f'Índice: {posicao} {num}')