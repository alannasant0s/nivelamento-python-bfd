#Quantos números são positivos entre 5 entradas 
n = []
for i in range(5):
    n = int(input('Insira o número: '))
    if i > 0:
        n.append(i)
print(n)
    