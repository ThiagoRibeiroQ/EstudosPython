#classes pai
class Animal():
    def __init__(self, nome):
        self.nome = nome

class Predador(Animal):
    def cacando(self):
        print(f'O animal {self.nome} está caçando')

class Presa(Animal):
    def fugindo(self):
        print(f'O animal {self.nome} está sendo caçado')

#classes filho
class Coelho(Presa):
    pass

class Tigre(Predador):
    pass

class Cobra(Predador, Presa):
    pass


coelho1 = Coelho('Pernalonga')
tigre1 = Tigre('Tigrão')
cobra1 = Cobra('Serpe')



coelho1.fugindo()
tigre1.cacando()
cobra1.cacando()



