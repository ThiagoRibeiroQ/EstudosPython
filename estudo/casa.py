class Casa:
    def __init__(self, cor, quartos, banheiros):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros

    def mostrarCor(self):
        print(f'A casa é da cor {self.cor}')    

    def mostrarQuartos(self):
        print(f'essa casa possui {self.quartos} quartos')

    def mostrarBanheiros(self):
        print(f'A casa possui {self.banheiros} banheiros')

    #adicionando um quarto
    def adicionarQuarto(self):
        self.quartos = self.quartos + 1
        print(f'Agora essa casa possui {self.quartos} quartos')

    #mudando a cor da casa
    def mudarCorDaCasa(self, novaCor):
        print(f'Pintando a casa de {self.cor} para {novaCor}')

#atributos das casas
casa1 = Casa('Azul', 2, 1)
casa2 = Casa('Amarela', 4, 2)
casa3 = Casa('Vermelha', 7, 4)
casa4 = Casa('Verde', 6, 4)

#informações da casa 1
print('\nCasa 1:')
casa1.mostrarCor()
casa1.mostrarQuartos()
casa1.mostrarBanheiros()
casa1.adicionarQuarto()
casa1.mudarCorDaCasa('preto')

#informações da casa 2
print('\nCasa 2:')
casa2.mostrarCor()
casa2.mostrarQuartos()
casa2.mostrarBanheiros()

#informações da casa 3
print('\nCasa 3:')
casa3.mostrarCor()
casa3.mostrarQuartos()
casa3.mostrarBanheiros()

#informações da casa 4
print('\nCasa 4:')
casa4.mostrarCor()
casa4.mostrarQuartos()
casa4.mostrarBanheiros()
