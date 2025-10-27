#Quantidade de letra 'a' em uma frase 

qtd_a = 0

frase = input('Insira a sua frase: ').lower()
for i in frase:
    if i == 'a' :
        qtd_a += 1

print(f'A frase possui {qtd_a} letras a')