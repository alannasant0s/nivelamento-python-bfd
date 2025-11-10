class Carro():
    def __init__(self, marca, estado, cor):
        self.marca = marca
        self.estado = estado
        self.cor = cor

carro1 = Carro('Gol', 'Novo', 'Azul')
carro2 = Carro('Vectra', 'Usado', 'Verde')

print(f'O primeiro carro é um {carro1.marca} da cor {carro1.cor} e sua situação é {carro1.estado}')
print(f'O segundo carro é um {carro2.marca} da cor {carro2.cor} e sua situação é {carro2.estado}')



