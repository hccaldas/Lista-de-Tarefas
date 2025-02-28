tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa na lista.")
    else:
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

def remover_tarefa():
    listar_tarefas()
    indice = int(input("Digite o número da tarefa para remover: ")) - 1
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        print("Tarefa removida!")
    else:
        print("Índice inválido.")

while True:
    print("\n1 - Adicionar tarefa\n2 - Listar tarefas\n3 - Remover tarefa\n4 - Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        adicionar_tarefa()
    elif escolha == "2":
        listar_tarefas()
    elif escolha == "3":
        remover_tarefa()
    elif escolha == "4":
        break
    else:
        print("Opção inválida!")
