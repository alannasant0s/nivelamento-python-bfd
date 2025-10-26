#Contar espaços em uma frase  
espacos = 0
frase = input('Insira sua frase: ')
for i in frase:
    if i == ' ':
        espacos += 1
print(f'A quantidade de espaços na frase inserida é: {espacos}')
