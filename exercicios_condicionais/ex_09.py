#Classificação por idade

idade = int(input('Insira a sua idade: '))

if idade >= 18:
    print('Você é adulto')
elif idade < 18 and idade > 13:
    print('VocÊ é adolescente')
else: 
    print('Você é criança') 