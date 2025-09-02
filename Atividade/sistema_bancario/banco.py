# Parte 1: Classe Conta
class Conta:
    # Método construtor
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0.0
        self.limite = 1000.0
        print(f"Conta nº {self.numero} criada para o titular {self.titular}.")

    # Método para adicionar valor ao saldo
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido. Por favor, insira um valor positivo.")

    # Método para retirar valor do saldo
    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido. Por favor, insira um valor positivo.")
            return False
            
        if valor > (self.saldo + self.limite):
            print(f"Saque não autorizado. Saldo e limite insuficientes.")
            print(f"Saldo disponível: R$ {self.saldo:.2f} | Limite: R$ {self.limite:.2f}")
            return False
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            return True

    # Método para mostrar o saldo atual
    def extrato(self):
        print(f"Conta nº {self.numero} | Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")

    # Método do Desafio Extra
    def transferir(self, valor, conta_destino):
        print("-" * 20)
        print(f"Iniciando transferência de R$ {valor:.2f}")
        print(f"De: {self.titular} (Conta {self.numero})")
        print(f"Para: {conta_destino.titular} (Conta {conta_destino.numero})")
        
        # Tenta sacar o valor da conta de origem (self)
        saque_bem_sucedido = self.sacar(valor)

        # Se o saque foi possível, deposita na conta de destino
        if saque_bem_sucedido:
            conta_destino.depositar(valor)
            print("Transferência concluída com sucesso.")
        else:
            # A mensagem de erro já é impressa pelo método sacar()
            print("Transferência não realizada.")
        print("-" * 20)


# Parte 2: Classe Cliente
class Cliente:
    # Método construtor
    def __init__(self, nome, cpf, numero_conta):
        self.nome = nome
        self.cpf = cpf
        # Aqui acontece a COMPOSIÇÃO:
        # O Cliente "tem uma" Conta. O objeto Conta é criado DENTRO do Cliente.
        self.conta = Conta(numero_conta, nome)


# Parte 3: Código de Exemplo e Teste

# A verificação `if __name__ == "__main__":` garante que este bloco de código
# só será executado quando este arquivo for rodado diretamente.
if __name__ == "__main__":
    
    # --- Demonstração Básica ---
    print("--- CRIANDO CLIENTE 1 ---")
    cliente1 = Cliente("João Silva", "123.456.789-00", 1001)
    print("\n") # Linha em branco para separar

    # Acessando o objeto 'conta' dentro do 'cliente1' para realizar operações
    print(f"--- OPERAÇÕES: {cliente1.nome} ---")
    cliente1.conta.extrato()
    cliente1.conta.depositar(350.50)
    cliente1.conta.extrato()

    # Tentando sacar um valor que não pode
    cliente1.conta.sacar(2000.0)

    # Sacando um valor permitido
    cliente1.conta.sacar(150.0)
    cliente1.conta.extrato()
    print("\n")

    # --- Demonstração do Desafio (Transferência) ---
    print("--- CRIANDO CLIENTE 2 ---")
    cliente2 = Cliente("Maria Souza", "987.654.321-11", 2002)
    cliente2.conta.depositar(1000.0)
    print("\n")
    
    print("--- EXTRATOS INICIAIS ---")
    cliente1.conta.extrato()
    cliente2.conta.extrato()

    # Cliente 2 transfere 400 para o Cliente 1
    cliente2.conta.transferir(400.0, cliente1.conta)

    print("--- EXTRATOS FINAIS ---")
    cliente1.conta.extrato()
    cliente2.conta.extrato()