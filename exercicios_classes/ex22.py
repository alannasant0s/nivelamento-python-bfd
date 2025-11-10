"""Crie uma classe Produto com método desconto(percentual) que reduz o preço. 
Teste com um valor de 10%"""

class Produto:
    def __init__(self, preco):
        self.preco = preco

    def desconto(self, percentual = 10):
        desconto_aplicado = (self.preco / 100) * percentual

        self.preco -= desconto_aplicado
        return self.preco
    
preco = float(input("Insira o valor do produto para que seja aplicado o desconto: "))
produto1 = Produto(preco)

valor_desconto = produto1.desconto()
print(f"O valor do produto com desconto é: {valor_desconto}")

