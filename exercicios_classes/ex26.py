"""Crie uma classe Casa com atributos cor e tamanho. 
Crie duas casas com valores diferentes e exiba os dados."""

class Casa:
    def __init__(self, cor, tamanho):
        self.cor = cor
        self.tamanho = tamanho


casa1 = Casa("Azul", "100x30")
casa2 = Casa("Bege", "50x20")

print(f"A casa1 é da cor {casa1.cor} e tem o tamanho {casa1.tamanho}")
print(f"A casa2 é da cor {casa2.cor} e tem o tamanho {casa2.tamanho}")