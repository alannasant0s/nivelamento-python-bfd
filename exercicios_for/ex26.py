#Quantos números negativos entre 10 

numeros = 0
for i in range(10):
    n = int(input('Insira um número inteiro: '))
    if n < 0 :
        numeros += 1
print(f'Foram inseridos {numeros} numero(s) negativos')

    