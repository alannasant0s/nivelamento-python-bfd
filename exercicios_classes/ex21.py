"""Crie uma classe Aluno que tenha método media(n1, n2) e retorne a média. 
Mostre o resultado."""

class Aluno:
    def __init__(self):
        pass


    def media(self, n1, n2):
        calculo = (n1 + n2) / 2

        return calculo

n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))

aluno1 = Aluno()
media = aluno1.media(n1, n2)

print(f"A média do aluno é {media}")

    
