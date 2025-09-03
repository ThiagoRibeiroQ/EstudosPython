class Classes():
    def falar(self):
        print(f'Eu sou um personagem')

class Guerreiro(Classes):
    def falar(self):
        print(f'Minha classe é guerreiro')

class Mago(Classes):
    def falar(self):
        print(f'Minha classe é mago')

class Druida(Classes):
    def falar(self):
        print(f'Minha classe é druida')

#criar os objetos

personagens = [Guerreiro(), Mago(), Druida()]

for p in personagens:
    p.falar()