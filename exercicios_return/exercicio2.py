class Motor:
	def __init__(self, estado = False):
		self.estado = estado

	def ligar_motor(self):
	    self.estado = True


motor1 = Motor()
motor2 = Motor()

motor1.ligar_motor()

print(f"O estado do motor1 é {motor1.estado} e o estado do motor2 é {motor2.estado}")   