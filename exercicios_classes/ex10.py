"""Crie uma classe Lampada com o atributo estado (acesa ou apagada). 
Implemente um método ligar() que altera o estado. 
Mostre o resultado."""


class Lampada:
    def __init__(self):
        self.estado = False

    def ligar(self):
        self.estado = True

lampada1 = Lampada()
lampada1.ligar()

print(f"A lâmpada agora esta {lampada1.estado}")
