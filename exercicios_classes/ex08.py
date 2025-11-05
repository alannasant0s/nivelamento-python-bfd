class Produto():

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produto1 = Produto("isqueiro", 3.50)
produto2 = Produto("faca", 5.47)

print(f"O {produto1.nome} custa {produto1.preco}")
print(f"A {produto2.nome} custa {produto2.preco}")