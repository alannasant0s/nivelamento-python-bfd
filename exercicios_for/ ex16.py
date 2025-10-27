#Quantos números são positivos entre 5 entradas 
positivos = []
for i in range(5):
    n = int(input('Insira o número: '))
    if n > 0:
        positivos.append(n)
print(positivos)
    