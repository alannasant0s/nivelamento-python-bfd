#Nota de aluno

nota1 = int(input('Insira a primeira nota obtida: '))
nota2 = int(input('Insira a segunda nota obtida: '))
nota3 = int(input('Insira a terceira nota obtida: '))

media = (nota1 + nota2 + nota3) / 3


if media >= 7:
    print('Parabéns, você foi aprovado.')
else:
    print('Lamento, você não foi aprovado.')