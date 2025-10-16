#Número entre 1 e 100

numero = int(input('Insira um número: '))
if numero > 0 and numero <= 100:
    print(f'O número {numero} está contido no intervalo de 1 a 100')
else: 
    print(f'O número {numero} não está no intervalo de 1 a 100')