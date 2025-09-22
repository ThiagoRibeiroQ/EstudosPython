class Cafeteira:
    def __init__(self):
        self._capacidade_max_agua = 1000.0
        self._capacidade_max_cafe = 100.0  
        

        self.ligada = False
        self.nivel_agua_ml = 0.0
        self.nivel_cafe_gramas = 0.0
        
        print("Cafeteira pronta para uso!")

    def __str__(self):
        status_ligada = "Ligada" if self.ligada else "Desligada"
        return (f"--- Status da Cafeteira ---\n"
                f"Estado: {status_ligada}\n"
                f"Água:   {self.nivel_agua_ml:>5.1f}ml / {self._capacidade_max_agua:.1f}ml\n"
                f"Café:    {self.nivel_cafe_gramas:>5.1f}g / {self._capacidade_max_cafe:.1f}g")

    def ligar(self):
        if not self.ligada:
            self.ligada = True
            print("Cafeteira ligada.")
        else:
            print("A cafeteira já está ligada.")

    def desligar(self):
        if self.ligada:
            self.ligada = False
            print("Cafeteira desligada.")
        else:
            print("A cafeteira já está desligada.")

    def adicionar_agua(self, quantidade_ml):
        if quantidade_ml <= 0:
            print("ERRO: A quantidade de água deve ser positiva.")
            return

        novo_nivel = self.nivel_agua_ml + quantidade_ml
        if novo_nivel > self._capacidade_max_agua:
            adicionado = self._capacidade_max_agua - self.nivel_agua_ml
            self.nivel_agua_ml = self._capacidade_max_agua
            excesso = quantidade_ml - adicionado
            print(f"Reservatório de água cheio. {adicionado:.1f}ml adicionados. {excesso:.1f}ml de excesso.")
        else:
            self.nivel_agua_ml = novo_nivel
            print(f"{quantidade_ml:.1f}ml de água adicionados.")

    def adicionar_cafe(self, quantidade_gramas):
        if quantidade_gramas <= 0:
            print("ERRO: A quantidade de café deve ser positiva.")
            return
            
        novo_nivel = self.nivel_cafe_gramas + quantidade_gramas
        if novo_nivel > self._capacidade_max_cafe:
            adicionado = self._capacidade_max_cafe - self.nivel_cafe_gramas
            self.nivel_cafe_gramas = self._capacidade_max_cafe
            excesso = quantidade_gramas - adicionado
            print(f"Filtro de café cheio. {adicionado:.1f}g adicionados. {excesso:.1f}g de excesso.")
        else:
            self.nivel_cafe_gramas = novo_nivel
            print(f"{quantidade_gramas:.1f}g de café adicionados.")

    def fazer_cafe(self):
        if not self.ligada:
            print("ERRO: A cafeteira está desligada. Ligue-a primeiro.")
            return

        if self.nivel_agua_ml < 150:
            print("ERRO: Água insuficiente para fazer café.")
            return
        
        if self.nivel_cafe_gramas < 25:
            print("ERRO: Pó de café insuficiente.")
            return

        print("\nPreparando café...")
        self.nivel_agua_ml -= 150
        self.nivel_cafe_gramas -= 25
        print("Seu café está pronto e quentinho! ☕")

if __name__ == "__main__":

    minha_cafeteira = Cafeteira()
    print(minha_cafeteira)
    print("-" * 30)

    print("Tentando fazer café...")
    minha_cafeteira.fazer_cafe()
    print("-" * 30)

    print("Adicionando água e café...")
    minha_cafeteira.adicionar_agua(1000)
    minha_cafeteira.adicionar_cafe(50)
    print(minha_cafeteira)
    print("-" * 30)

    print("Tentando fazer café com ela desligada...")
    minha_cafeteira.fazer_cafe()
    print("-" * 30)

    print("Ligando a cafeteira e preparando o café...")
    minha_cafeteira.ligar()
    minha_cafeteira.fazer_cafe()
    print("\nStatus após fazer o primeiro café:")
    print(minha_cafeteira)
    print("-" * 30)

    print("Tentando fazer o segundo café...")
    minha_cafeteira.fazer_cafe()
    print("-" * 30)
    
    print("Tentando colocar 500ml de água a mais...")
    minha_cafeteira.adicionar_agua(500)
    print(minha_cafeteira)