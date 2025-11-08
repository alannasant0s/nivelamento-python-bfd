"""Crie uma classe Conta com saldo = 0.
Crie um método depositar(valor) que soma ao saldo.
Teste com dois depósitos diferentes"""


class Conta:
    def __init__(self, saldo = 0):
        self.saldo = float(saldo)
        

    def depositar(self):
        valor = float(input("Insira o valor a ser depositado: "))
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor inválido, digite um valor válido")

cliente1 = Conta()
print(f"O saldo do cliente1 é: {cliente1.saldo}")
cliente1.depositar ()
print(f"O saldo do cliente1 é: {cliente1.saldo}")
