class Produto():
    def __init__(self, nome, preco, codigo):
        self.nome = nome
        self.preco = preco
        self.codigo = codigo


    def exibir_detalhes(self):
        print(f'Nome: {self.nome} | Preço: R${self.preco} | Código do produto: {self.codigo}')



class Livro(Produto):
    def __init__(self, nome, preco, codigo, autor):
        super().__init__(nome, preco, codigo)
        self.autor = autor


    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f'Autor: {self.autor}')



class Eletronico(Produto):
    def __init__(self, nome, preco, codigo, marca):
        super().__init__(nome, preco, codigo)
        self.marca = marca

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f'Marca: {self.marca}')


class CarrinhoDeCompras():
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f'O produto: {produto.nome} foi adicionado ao carrinho.')
    
    def listar_produtos(self):
        if not self.produtos:
            print("O carrinho está vazio.")
            return
            
        for produto in self.produtos:
            produto.exibir_detalhes()
            print("-" * 25) 

    def calcular_total(self):
        total = 0.0
        for produto in self.produtos:
            total += produto.preco
        return total
    

livro1 = Livro('O Hobbit', 40, 123232, 'J.R.R Tolkien')
eletronico1 = Eletronico('PlayStation 5', 3500, 1823784, 'Sony')
livro2 = Livro('Arruinados pelo amor de Deus', 40, 1234345, 'Yago Martins')

carrinho = CarrinhoDeCompras()

carrinho.adicionar_produto(livro1)
carrinho.adicionar_produto(livro2)
carrinho.adicionar_produto(eletronico1)

print('-' * 25)

print('PRODUTOS NO CARRINHO: ')
carrinho.listar_produtos()

total = carrinho.calcular_total

print(f'Total da compra: R${total}')

print('-' * 25)

