#Turno de estudo
'''
Manhã -> 7.00 às 11.00
Tarde -> 13.00 às 17.00
Noite -> 19.00 às 22.00
'''
horario_entrada = float(input('Insira o horário da sua entrada no curso(ex: 7.00): '))
horario_saida = float(input('Insira o horário da sua saida do curso(ex: 11.00): '))

if horario_entrada >= 7 and horario_saida <= 11:
    print('Você é um aluno do turno manhã')
elif horario_entrada >= 13 and horario_entrada <= 17:
    print('Você é um aluno do turno tarde')
elif horario_entrada > 17 and horario_saida <= 22:
    print('Você é um aluno do turno da noite')
else:
    print('Lamento, você não pertence a nenhuma turma')

