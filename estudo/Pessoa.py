class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'O meu nome é {self.nome} e tenho {self.idade} anos de idade')

    
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def trabalhar(self):
        print(f'{self.nome} está trabalhando como {self.cargo}')

class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome, idade)
        self.saldo = saldo

    def compra(self, valorCompra):
        if valorCompra <= self.saldo:
            self.saldo -= valorCompra
            print(f'Compra efetuada! Seu saldo restante é de R${self.saldo}')
        else:
            print(f'Compra negada! Seu saldo é de R${self.saldo}')


funcionario1 = Funcionario('Maria', 48, 'gerente')
funcionario1.apresentar()
funcionario1.trabalhar()
   
cliente1 = Cliente('Casimiro', 4, 100000000000000000)
cliente1.apresentar()
cliente1.compra(30)
cliente1.compra(30000000000000)