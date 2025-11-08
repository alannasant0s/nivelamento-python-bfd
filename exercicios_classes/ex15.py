"""Crie uma classe Aluno que receba nome e curso pelo método __init__.
Crie dois alunos e exiba seus dados."""


class Aluno:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso

aluno1 = Aluno("Alanna", "Ciência da computação")
aluno2 = Aluno("Áurea", "Psicopedagogia")

print(f"O aluno1 se chama {aluno1.nome} e cursa {aluno1.curso}")
print(f"O aluno1 se chama {aluno2.nome} e cursa {aluno2.curso}")