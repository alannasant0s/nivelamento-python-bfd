"""Na classe ContaBancaria, adicione um método mostrar_saldo().
Chame esse método em dois objetos."""

class ContaBancaria():
    

    def __init__(self, saldo, extrato):
        self.saldo = saldo
        self.extrato = extrato

    def mostrar_saldo(self):
        print(f"O saldo do usuário é {self.saldo}")

    def mostrar_extrato(self):
        print(f"O extrato do usuário é {self.extrato}")
        

usuario1 = ContaBancaria(1000, 5000)
usuario2 = ContaBancaria(70, 150)

usuario1.mostrar_saldo()
usuario2.mostrar_saldo()

usuario1.mostrar_extrato()
usuario2.mostrar_extrato()
