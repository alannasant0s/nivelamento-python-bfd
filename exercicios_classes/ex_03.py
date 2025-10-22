class Carro():
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado

carro1 = Carro('Gol', 'Novo')
carro2 = Carro('Vectra', 'Usado')

print(f'O primeiro carro é um {carro1.marca} e sua situação é {carro1.estado}')
print(f'O segundo carro é um {carro2.marca} e sua situação é {carro2.estado}')

