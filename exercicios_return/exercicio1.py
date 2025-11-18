class Carro:
    def __init__(self, estado):
	    self.estado = estado

	def mostrar_estado(self):
          return self.estado 


carro1 = Carro("Novo")
carro2 = Carro("Usado")

carro1.mostrar_estado()
carro2.mostrar_estado()

