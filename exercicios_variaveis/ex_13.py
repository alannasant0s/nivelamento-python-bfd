#Peça a altura e o peso e calcule o IMC

peso = float(input('Insira o seu peso: '))
altura = float(input('Insira a sua altura: '))

print(f'Seu índice IMC é {(peso / (altura ** 2)):.2f}')