'''Crie uma classe Aluno com os atributos nome e nota.
Peça para o usuário digitar os valores e mostre o resultado.'''

class Aluno():
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

aluno1_nome = input('Insira seu nome: ')
aluno1_nota = input('Insira sua nota final: ')

aluno1 = Aluno(aluno1_nome, aluno1_nota)

print(f'O nome do aluno é {aluno1.nome} sua nota final foi {aluno1.nota} ')