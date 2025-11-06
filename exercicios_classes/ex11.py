"""Crie uma classe Funcionario com os atributos nome e salario. 
Imprima o nome e o salário de dois funcionários. """


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    

funcionario1 = Funcionario("Alanna", 3500)
funcionario2 = Funcionario("Áurea", 2700)

print(f"O funcionario1 se chama {funcionario1.nome} e recebe R$: {funcionario1.salario}")
print(f"O funcionario2 se chama {funcionario2.nome} e recebe R$: {funcionario2.salario}")