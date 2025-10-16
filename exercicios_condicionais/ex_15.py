#Vogal ou consoante

vogais = 'aeiouAEIOU'

escolha = input('Insira uma letra: ')
if escolha in vogais:
    print(f'A letra {escolha} é uma vogal')
else:
    print(f'A letra {escolha} é uma consoante')