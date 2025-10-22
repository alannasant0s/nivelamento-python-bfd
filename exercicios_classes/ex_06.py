'''Na classe ContaBancaria, adicione um método mostrar_saldo().
Chame esse método em dois objetos.'''

class ContaBancaria():
    

    def __init__(self, saldo):
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f'O saldo do usuário1 é {self.saldo}')
        

usuario1 = ContaBancaria(1000)
usuario2 = ContaBancaria(70)

usuario1.mostrar_saldo()
usuario2.mostrar_saldo()
