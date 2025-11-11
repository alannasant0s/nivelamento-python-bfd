"""Crie uma classe Carro com método mostrar_estado() que imprime o valor atual do 
atributo estado. 
Teste com dois carros. """


class Carro:
    def __init__(self):
        self.estado = "Novo"


    def mostrar_estado(self):
        print(self.estado)

carro1 = Carro()
carro2 = Carro()

carro1.mostrar_estado()
carro2.mostrar_estado()