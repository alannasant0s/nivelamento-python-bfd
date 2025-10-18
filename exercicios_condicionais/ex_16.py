tamanho = int(input('Insira o tamanho do triangulo: '))

for i in range(tamanho):
    contador_hashes = i + 1
    hashes = "#" * contador_hashes
    
    espacos_esquerda = tamanho - 1 - i
    espacos = " " * espacos_esquerda
    
    espaco_meio = " "
    
    print(f'{espacos}{hashes}{espaco_meio}{hashes}') 