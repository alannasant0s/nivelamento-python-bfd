"""Crie uma classe Motor com atributo ligado=False. 
Adicione método ligar_motor() e mude o estado para True. """


class Motor:
    def __init__(self):
        self.ligado = False

    def ligar_motor(self): 
        self.ligado = True


motor1 = Motor()
print(f"O motor está ligado? {motor1.ligado}")
motor1.ligar_motor()
print(f"O motor está ligado? {motor1.ligado}")
