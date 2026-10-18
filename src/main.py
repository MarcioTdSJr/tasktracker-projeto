def exibir_menu():
    print("\n" + "="*30)
    print("       TASKTRACKER CLI")
    print("="*30)
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")
    print("="*30)

def cadastrar_tarefa(tarefas):
    print("\n--- [Cadastro de Nova Tarefa] ---")
    
    # Validação do Título: Impede strings vazias ou apenas espaços
    titulo = ""
    while not titulo.strip():
        titulo = input("Título da tarefa (Obrigatório): ")
        if not titulo.strip():
            print("Erro: O título não pode ser vazio. Tente novamente.")
            
    descricao = input("Descrição detalhada (Opcional): ")
    
    # Validação da Prioridade: Restringe entradas
    prioridades_validas = ["Alta", "Média", "Media", "Baixa"]
    prioridade = ""
    while prioridade not in prioridades_validas:
        prioridade = input("Nível de Prioridade (Alta, Média ou Baixa): ")
        if prioridade not in prioridades_validas:
            print("Erro: Prioridade inválida. Digite exatamente Alta, Média ou Baixa.")
            
    data_limite = input("Data Limite para conclusão (ex: DD/MM/AAAA): ")
    
    # Criação do dicionário com status automático
    nova_tarefa = {
        "titulo": titulo.strip(),
        "descricao": descricao.strip(),
        "prioridade": prioridade.strip(),
        "data_limite": data_limite.strip(),
        "status": "Pendente"
    }
    
    tarefas.append(nova_tarefa)
    print("\n>>> Tarefa salva com sucesso!")

def visualizar_tarefas(tarefas):
    print("\n--- [Lista de Tarefas] ---")
    
    # Regra de exibição para lista vazia ou preenchida
    if not tarefas:
        print(">>> Não existem tarefas cadastradas no momento.")
    else:
        for i, tarefa in enumerate(tarefas, 1):
            print(f"\nTarefa {i}:")
            print(f"  [-] Título:     {tarefa['titulo']}")
            print(f"  [-] Descrição:  {tarefa['descricao']}")
            print(f"  [-] Prioridade: {tarefa['prioridade']}")
            print(f"  [-] Prazo:      {tarefa['data_limite']}")
            print(f"  [-] Status:     {tarefa['status']}")
        print("-" * 26)

def main():
    tarefas = [] # Estrutura de dados principal em memória
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção do menu (1-3): ")
        
        if opcao == '1':
            cadastrar_tarefa(tarefas)
        elif opcao == '2':
            visualizar_tarefas(tarefas)
        elif opcao == '3':
            print("\nEncerrando o TaskTracker. Até a próxima!\n")
            break
        else:
            print("\nErro: Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()