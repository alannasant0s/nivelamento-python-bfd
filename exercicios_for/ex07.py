#Contar vogais em uma palavra

palavra = input('Insira uma palavra: ')
cont = 0
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for j in palavra:
    if j in vogais:
        cont += 1      
print(f'A palavra inserida possui {cont} vogais')
    