"""Crie uma classe Conta com método sacar(valor) que diminui o saldo. 
Teste o saque com valores válidos e inválidos (maiores que o saldo)."""



class Conta:
    def __init__(self, saldo = 600):
        self.saldo = float(saldo)

    
    def sacar(self):
        valor_sacado = float(input("Insira o valor que deseja sacar: "))
        if valor_sacado > self.saldo:
            print("Saldo insuficiente, tente outro valor")
        else:
            print("Operação realizada com sucesso")
            self.saldo -= valor_sacado


cliente1 = Conta()
cliente1.sacar()
cliente1.sacar()

print(f"O saldo atual é: {cliente1.saldo :.2f}")
