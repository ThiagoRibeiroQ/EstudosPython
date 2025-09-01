class Animal:
    def __init__(self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie

    def apresentar(self):
        print(f'Eu sou um {self.especie} e o meu nome é {self.nome}')

class gato(Animal):
    def som(self):
        print('Miau!')

    def ronrona(self):
        print('O gato está ronronando')

class cachorro(Animal):
    def som(self):
        print('Auuuuuuuuuuu')

    def late(self):
        print('O cachorro está latindo')

class dinossauro(Animal):
    def som(self):
        print('Rawr')

    def ruge(self):
        print('O dinossauro está rugindo')


gato1 = gato('pingo', 'branco', 'sphynx')
gato1.apresentar()
gato1.som()
gato1.ronrona()

cachorro1 = cachorro('Casimiro', 'marrom', 'salsicha')
cachorro1.apresentar()
cachorro1.som()
cachorro1.late()

cachorro2 = cachorro('Ed', 'dourado', 'Vira lata')
cachorro2.apresentar()

dinossauro1 = dinossauro('spino', 'azul', 'Espinossauro')
dinossauro1.apresentar()
dinossauro1.som()
dinossauro1.ruge()