from abc import ABC, abstractmethod
import time 

#Classe de personagem
class Personagem(ABC):
    def __init__(self, nome, vida, nivel):
        self.nome = nome
        self.vida = vida
        self.nivel = nivel

    def exibir_status(self):
        print(f"Nome: {self.nome} | Vida: {self.vida} | Nível: {self.nivel}")

    @abstractmethod
    def atacar(self, alvo):
        pass

    @abstractmethod
    def defender(self, dano):
        pass


#Classe da classe guerreiro
class Guerreiro(Personagem):
   
    def __init__(self, nome, vida, nivel, forca):
        super().__init__(nome, vida, nivel)
        self.forca = forca

    def atacar(self, alvo):
       
        dano = int(self.nivel * self.forca * 1.2) 
        print(f"🗡️  {self.nome} ataca {alvo.nome} com sua espada, causando {dano} de dano!")
        alvo.defender(dano)

    def defender(self, dano):
        self.vida -= dano
        print(f"🛡️  {self.nome} recebeu {dano} de dano.")
        if self.vida < 0:
            self.vida = 0 


#classe da classe mago
class Mago(Personagem):
    def __init__(self, nome, vida, nivel, magia):
        super().__init__(nome, vida, nivel)
        self.magia = magia

    def atacar(self, alvo):
       
        dano = int(self.nivel * self.magia * 1.5)
        print(f"🔥 {self.nome} lança uma bola de fogo em {alvo.nome}, causando {dano} de dano!")
        alvo.defender(dano)

    def defender(self, dano):
        self.vida -= dano
        print(f"🛡️  {self.nome} recebeu {dano} de dano.")
        if self.vida < 0:
            self.vida = 0



#classe que gerencia a batalha
class Batalha:
    def iniciar_batalha(self, jogador1, jogador2):
        print(f"--- A BATALHA COMEÇA: {jogador1.nome} vs {jogador2.nome} ---")
        turno = 1
        
        while jogador1.vida > 0 and jogador2.vida > 0:
            print(f"\n--- Turno {turno} ---")
            
            # Jogador 1 ataca Jogador 2
            jogador1.atacar(jogador2)
            time.sleep(1) 

            
            if jogador2.vida > 0:
                jogador2.atacar(jogador1)
                time.sleep(1) # 

            # Exibe o status ao final do turno
            print("\n--- Status Pós-Turno ---")
            jogador1.exibir_status()
            jogador2.exibir_status()
            
            turno += 1

        # Declara o vencedor
        print("\n--- FIM DA BATALHA ---")
        if jogador1.vida > 0:
            print(f"🏆 O vencedor é {jogador1.nome}!")
        elif jogador2.vida > 0:
            print(f"🏆 O vencedor é {jogador2.nome}!")
        else:
            print("A batalha terminou em empate!")



if __name__ == "__main__":
    
    # Criando os personagens
    guerreiro = Guerreiro("Aragorn", 2000, 15, 8)
    mago = Mago("Gandalf", 2000, 20, 10)

    # Iniciando a batalha
    batalha = Batalha()
    batalha.iniciar_batalha(guerreiro, mago)

