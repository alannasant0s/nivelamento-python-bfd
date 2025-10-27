#Nome com mais letras entre 5 
lista_nome = []
maior = ''
for i in range(5):
    n = input('Insira o nome: ')
    lista_nome.append(n)

for j in lista_nome:
    if len(j) > len(maior):
        maior = j

print(f'Nome com mais letras é {maior}')