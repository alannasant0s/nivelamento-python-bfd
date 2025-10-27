#Maior e menor de 5 notas

lista_notas = []
for i in range(5):
    lista_notas.append(int(input('Insira a nota: ')))
print(f'A maior nota foi: {max(lista_notas)} e a menor nota foi: {min(lista_notas)}')