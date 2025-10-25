
cont = 0
vogais = ['a', 'e', 'i', 'o', 'u']

palavra = input('Insira uma palavra: ').lower()
for i in palavra:
    if i in vogais:
        cont += 1
print(f'A palavra possui {cont} vogais.')