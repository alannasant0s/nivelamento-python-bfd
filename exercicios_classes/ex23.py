"""Crie uma classe Pessoa e adicione um atributo idade. 
Crie um método maior_de_idade() que retorna True se idade ≥ 18."""


class Pessoa:
    def __init__(self, idade):
        self.idade = idade
    
    def maior_idade(self):
        if self.idade >= 18:
            return True
        else:
            return False

idade = int(input("Insira a sua idade: "))
pessoa1 = Pessoa(idade)
print(pessoa1.maior_idade())