'''Crie uma classe ContaBancaria com o atributo saldo.
Crie duas contas com saldos diferentes e mostre ambos.'''

class ContaBancaria():
    

    def __init__(self, saldo):
        self.saldo = saldo

usuario1 = ContaBancaria(1000)
usuario2 = ContaBancaria(70)

print(f'O saldo do usuário1 é {usuario1.saldo} e o saldo do usuário2 é {usuario2.saldo} ')