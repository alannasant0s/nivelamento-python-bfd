#Média de 10 números

numeros = []
for i in range(11):
    r = int(input('Insira o número: '))
    numeros.append(r)
print(f'A média dos números {numeros} é: {sum(numeros)/ 10}')