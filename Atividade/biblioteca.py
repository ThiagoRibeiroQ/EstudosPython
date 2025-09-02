# classe Livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True  


    def emprestar(self):
  
        if self.disponivel:
            self.disponivel = False 
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' não está disponível no momento.")


    def devolver(self):
        self.disponivel = True  
        print(f"O livro '{self.titulo}' foi devolvido.")

  
    def verificar_disponibilidade(self):
        
        if self.disponivel:
            return f"O livro '{self.titulo}' está disponível."
        else:
            return f"O livro '{self.titulo}' está emprestado."
            
   
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}"

# --- Exemplo de Uso da Classe ---


livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)


print("Detalhes do livro:")
print(livro1)
print("-" * 20) 


print(livro1.verificar_disponibilidade())


livro1.emprestar()


livro1.emprestar()


print(livro1.verificar_disponibilidade())


livro1.devolver()


print(livro1.verificar_disponibilidade())