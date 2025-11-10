def media(nota1, nota2):
	media_aluno = (nota1 + nota2) / 2
	return media_aluno


nota1 = float(input("Insira a primeira nota: ")) 
nota2 = float(input("Insira a segunda nota: ")) 



resultado = media(nota1, nota2)
print(f"O aluno possui média de {resultado}")
