print('''----> Bem vindo ao formulário de inscrição! <----\n
Selecione abaixo o tipo de modalidade, e caso possua acompanhantes também será necessário inscreve-los.''')

T = int(input('''Deseja participar individualmente ou em dupla?\n
Digite [1] para individual
Digite [2] para dupla \n'''))

A = int(input('Digite o número de acompanhantes: sendo [0] para nenhum. '))


print(f'O valor total a ser pago é R$ {T * 10 + A * 10 } reais.')
