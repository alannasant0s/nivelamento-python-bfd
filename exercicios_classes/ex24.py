"""Crie uma classe Banco com atributo clientes (lista). 
Adicione três nomes à lista e imprima todos."""

class Banco:
    def __init__(self, clientes):
        self.clientes = clientes

cliente = 0
clientes = []
while cliente < 3:
   c = input("Insira seu nome: ")
   clientes.append(c)
   cliente += 1

pessoas = Banco(clientes)
print(pessoas.clientes)