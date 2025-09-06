
class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    def __str__(self):
        marcador = "[X]" if self.concluida else "[ ]"
        return f"{marcador} {self.descricao}"

    def marcar_como_concluida(self):
        self.concluida = True


class TarefaComPrazo(Tarefa):
    def __init__(self, descricao, data_prazo):
        super().__init__(descricao)
        self.data_prazo = data_prazo

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} - Prazo: {self.data_prazo}"
    

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __str__(self):
        return self.nome

    def adicionar_tarefa(self, tarefa_nova):
        if isinstance(tarefa_nova, Tarefa):
            self.tarefas.append(tarefa_nova)
            print("Tarefa adicionada com sucesso!")
        else:
            print("Erro: Apenas objetos do tipo Tarefa podem ser adicionados.")
            
    def listar_tarefas(self):
        print(f"\n--- Tarefas do Projeto: {self.nome} ---")
        
        pendentes = [t for t in self.tarefas if not t.concluida]
        concluidas = [t for t in self.tarefas if t.concluida]

        if not self.tarefas:
            print("Este projeto ainda não tem tarefas.")
            return

        if pendentes:
            print("\n>> Pendentes:")
            for i, tarefa in enumerate(pendentes):
                print(f"  {i + 1}. {tarefa}")
        
        if concluidas:
            print("\n>> Concluídas:")
            for tarefa in concluidas:
                print(f"  - {tarefa}")


class Gerenciador:
    def __init__(self):
        self.projetos = {}

    def adicionar_projeto(self, nome_projeto):
        if nome_projeto in self.projetos:
            print(f"Erro: O projeto '{nome_projeto}' já existe.")
        else:
            self.projetos[nome_projeto] = Projeto(nome_projeto)
            print(f"Projeto '{nome_projeto}' adicionado com sucesso!")

    def selecionar_projeto(self, nome_projeto):
        return self.projetos.get(nome_projeto)

    def listar_projetos(self):
        print("\n--- Projetos Cadastrados ---")
        if not self.projetos:
            print("Nenhum projeto cadastrado.")
        else:
            for nome in self.projetos:
                print(f"- {nome}")

    def menu_principal(self):
        while True:
            print("\n===== GERENCIADOR DE TAREFAS =====")
            print("1. Adicionar Novo Projeto")
            print("2. Selecionar um Projeto")
            print("3. Listar todos os Projetos")
            print("4. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                nome_proj = input("Digite o nome do novo projeto: ")
                self.adicionar_projeto(nome_proj)
            elif escolha == '2':
                nome_proj = input("Digite o nome do projeto que deseja selecionar: ")
                projeto_selecionado = self.selecionar_projeto(nome_proj)
                if projeto_selecionado:
                    self.menu_do_projeto(projeto_selecionado)
                else:
                    print("Erro: Projeto não encontrado.")
            elif escolha == '3':
                self.listar_projetos()
            elif escolha == '4':
                print("Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def menu_do_projeto(self, projeto):
        while True:
            print(f"\n--- Gerenciando Projeto: {projeto.nome} ---")
            print("1. Adicionar Tarefa Simples")
            print("2. Adicionar Tarefa com Prazo")
            print("3. Marcar Tarefa como Concluída")
            print("4. Listar Tarefas do Projeto")
            print("5. Voltar ao Menu Principal")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                desc = input("Descrição da tarefa: ")
                projeto.adicionar_tarefa(Tarefa(desc))
            elif escolha == '2':
                desc = input("Descrição da tarefa: ")
                prazo = input("Data de prazo (ex: 25/12/2025): ")
                projeto.adicionar_tarefa(TarefaComPrazo(desc, prazo))
            elif escolha == '3':
                pendentes = [t for t in projeto.tarefas if not t.concluida]
                if not pendentes:
                    print("Nenhuma tarefa pendente para marcar.")
                    continue
                
                print("\nQual tarefa pendente você deseja concluir?")
                for i, tarefa in enumerate(pendentes):
                    print(f"  {i + 1}. {tarefa.descricao}")
                
                try:
                    num_tarefa = int(input("Digite o número da tarefa: "))
                    if 1 <= num_tarefa <= len(pendentes):
                        pendentes[num_tarefa - 1].marcar_como_concluida()
                        print("Tarefa marcada como concluída!")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")

            elif escolha == '4':
                projeto.listar_tarefas()
            elif escolha == '5':
                break
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":

    app = Gerenciador()

    app.menu_principal()