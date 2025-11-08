"""Crie uma classe Livro com os atributos titulo e autor.
Crie dois livros diferentes e imprima as informações."""

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor



livro1 = Livro("O caçador de ossos", "Brown lee")
livro2 = Livro("A bela adormecida", "Desconhecido")

print(f"O livro1 possui o título {livro1.titulo} e foi escrito por {livro1.autor}")
print(f"O livro2 possui o título {livro2.titulo} e foi escrito por {livro2.autor}")