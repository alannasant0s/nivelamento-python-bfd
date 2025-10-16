#Velocidade


velocidade_atual = int(input('Insira a sua velocidade atual: '))

if velocidade_atual > 0 and velocidade_atual <= 80:
    print('Você está na velocidade permitida para a via')
elif velocidade_atual < 0:
    print('ERRO, insira a velocidade correta')
else:
    print('Você está acima do permitido para o trecho, reduza a velocidade')