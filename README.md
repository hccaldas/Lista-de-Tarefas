# Lista de Tarefas em Python

Este repositório contém um script em Python que implementa uma simples lista de tarefas. O usuário pode adicionar, listar e remover tarefas da lista.

## Funcionalidades

- Adicionar tarefas à lista.
- Listar todas as tarefas.
- Remover tarefas da lista.

## Pré-requisitos

- Python 3.x

## Como usar

1. Clone este repositório ou copie o código para o seu ambiente local.
2. Certifique-se de ter o Python 3.x instalado no seu sistema.
3. Execute o script.
4. Escolha uma das opções do menu:
   - (1) Adicionar tarefa
   - (2) Listar tarefas
   - (3) Remover tarefa
   - (4) Sair

## Exemplo de Uso

```python
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
