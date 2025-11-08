"""Crie uma classe Conta com saldo = 0.
Crie um método depositar(valor) que soma ao saldo.
Teste com dois depósitos diferentes"""


class Conta:
    def __init__(self, saldo = 0):
        self.saldo = saldo
        

    def depositar(self):
        self.saldo = int(input("Insira o valor a ser depositado: "))

cliente1 = Conta()
print(f"O saldo do cliente1 é: {cliente1.saldo}")
cliente1.depositar()
print(f"O saldo do cliente1 é: {cliente1.saldo}")
