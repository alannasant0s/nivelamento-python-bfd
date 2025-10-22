class Pessoa:

        def __init__(self, nome, tamanho):
                self.nome = nome
                self.tamanho = tamanho

#Os objetos passam a existir a partir do momento que são criados abaixo
p1 = Pessoa('Alanna', 1.63)
p2 = Pessoa('Áurea', 1.74)

print(f'A primeira pessoa se chama: {p1.nome} e tem {p1.tamanho} centimetros.')
print(f'A segunda pessoa se chama: {p2.nome} e tem {p2.tamanho} centimetros.')