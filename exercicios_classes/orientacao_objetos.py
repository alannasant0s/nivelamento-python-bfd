#Classes -> Representação
#Atributos -> Variáveis
#Métodos -> Funções


#carro
    #Modelo -> Ferrari
    #Ano -> 2020
    #Estado -> seminovo

    # modelo, ano, estado, -> Atributos

    #ligar()
    #acelerar()
    #frear()
    #Comprar()
    #teste_driver()

#ligar(), acelerar(), frear(), Comprar(), teste_driver() -> Métodos

#carro
    #Modelo -> BMW
    #Ano -> 2020
    #Estado -> seminovo

     #ligar()
    #acelerar()
    #frear()
    #Comprar()
    #teste_driver()

#ligar(), acelerar(), frear(), Comprar(), teste_driver() -> Métodos

class Carro(object):
    estado = 'novo'

fusca = Carro()
fusca.estado = 'novo'

ferrari = Carro()
ferrari.estado = 'usado'

print(fusca.estado) # valor do atributo estado do objeto
print(ferrari.estado) # valor do atributo estado do objeto
print(type(fusca)) # representação do objeto fusca
print(ferrari) #Representação do objeto ferrari

