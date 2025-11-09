"""Crie uma classe Carro que tenha marca, modelo e ano. 
Peça ao usuário para preencher e depois exiba as informações."""


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


marca = input("Qual o nome do carro? ")
modelo = input("Qual o modelo do carro? ")
ano = int(input("Qual o ano do carro? "))

carro1 = Carro(marca, modelo, ano) 

print(f"A marca do carro é {carro1.marca} do modelo {carro1.modelo} fabricado no ano {carro1.ano}")