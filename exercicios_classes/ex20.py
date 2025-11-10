"""Crie uma classe Retangulo que receba largura e altura. 
Crie um método area() que retorne o valor da área. 
Teste com um objeto."""


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = float (largura)
        self.altura = float (altura)


    def area(self):
        tamanho = self.largura * self.altura
        print(f"A área do objeto possui largura de {self.largura} cm e altura de {self.altura} cm e um tamanho total de {tamanho}")


largura = input("Insira a largura do objeto: ")
altura = input("Insira a altura do objeto: ")

obj1 = Retangulo(largura, altura)
obj1.area()