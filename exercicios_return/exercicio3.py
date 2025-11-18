

class Banco:
	def __init__(self, clientes):
		self.clientes = clientes
		

clientes = ["Alanna", "Karina", "moura"]
cliente1 = Banco(clientes)
print(cliente1.clientes)
