#Ler 5 nomes e mostrar em ordem inversa  
lista_nomes = []
for i in range(5):
    lista_nomes1 = input('Insira um nome: ')
    lista_nomes.append(lista_nomes1)
    

print(f'Ordem normal dos nomes: {lista_nomes}')
lista_nomes.reverse()
print(f'{lista_nomes}')