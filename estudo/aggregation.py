class Motor:
    def __init__(self, marca, potencia):
        self.marca = marca
        self.potencia = potencia

    

class Carro:
    def __init__(self):
        self.motores = []

    def adicionar_motor(self, motor):
        self.motores.append(motor)

    def listar_motores(self):
        for motor in self.motores:
            print(f'Marca: {motor.marca} | {motor.potencia} cavalos de potência')
    
#criando os objetos

motor_v6 = Motor('Ford', 3000)
motor_v8 = Motor('Ferrari', 6000)
motor_v12  = Motor('Porshe', 10000)

#criar o carro e adicionar o motor a ele

carro = Carro()
carro.adicionar_motor(motor_v6)
carro.adicionar_motor(motor_v8)
carro.adicionar_motor(motor_v12)

#Listar os motores
carro.listar_motores()

