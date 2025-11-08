class Celular:
    def __init__(self):
        self.estado = False
    
    def carregar(self):
        self.estado = True
        print(f"A bateria do celular está carregando")

celular = Celular()
celular.carregar()


