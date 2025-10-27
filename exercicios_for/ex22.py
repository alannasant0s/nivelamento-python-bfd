#Soma dos números pares de 1 a 50 

somatorio = 0
for i in range(1, 51):
    if i % 2 == 0:
        somatorio += i 
print(f'A soma dos números pares é: {somatorio}')