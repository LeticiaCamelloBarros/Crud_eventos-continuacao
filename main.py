from funcoes import *
import os
os.system("cls")


while True:

    chamar_menu()

    opcoes = input("Escolha a opção desejada: ").lower()

    if opcoes == "sair" or opcoes == "11":
        break

    elif opcoes == "adicionar" or opcoes == "add" or opcoes == "1":

        print("\n" + "-" * 60)
        print("  CADASTRAR NOVO EVENTO".center(60))
        print(("-" * 60) + "\n")

        nome_do_evento = input("Insira o nome do evento: ").capitalize().strip()

        if not nome_do_evento:
            print("voce não pode deixar um campo vazio, tente de novo.\n")
            break
        
        tipo_do_evento = input("Insira o tipo de evento: ").capitalize().strip()

        if not tipo_do_evento:
            print("voce não pode deixar um campo vazio, tente de novo.\n")
            break

        data_do_evento = input("Insira a data desta forma (XX/YY/ZZZZ): ")

        local_do_evento = input("Insira o local do evento: ").capitalize().strip()

        orcamento = input("Insira o orçamento do evento: ").capitalize().strip()

        adicionar(nome_do_evento, tipo_do_evento, data_do_evento, local_do_evento, orcamento)
        print("\nEvento cadastrado com sucesso!")

    elif opcoes == "visualizar" or opcoes == "visu" or opcoes == "2":
        print("\n" + "-" * 60)
        print("  VISUALIZAR EVENTOS".center(60))
        print(("-" * 60) + "\n")

        nome_do_evento = input("Insira o nome do evento: ").capitalize().strip()

        print()
        visualizar(nome_do_evento)

    elif opcoes == "editar" or opcoes == "edit" or opcoes == "3":
        print("\n" + "-" * 60)
        print("  EDITAR UM EVENTO".center(60))
        print(("-" * 60) + "\n")

        nome_do_evento = input("Insira o nome do evento que deseja editar: ").capitalize().strip()

        editar(nome_do_evento)

    elif opcoes == "excluir" or opcoes == "exc" or opcoes == "4":
        print("\n" + "-" * 60)
        print("  EXCLUIR UM EVENTO".center(60))
        print(("-" * 60) + "\n")

        arquivos_txt = []
        for f in os.listdir():
            if f.endswith(".txt"):
                arquivos_txt.append(f)

        if not arquivos_txt:  
            print("Não existe nenhum evento salvo para excluir.")
            continue

        nome_do_evento = input("Digite o nome do evento que deseja excluir: ")

        excluir(nome_do_evento)

    elif opcoes == "tempo" or opcoes == "time" or opcoes == "5":
        print("\n" + "-" * 60)
        print("  VISUALIZAR QUANTO TEMPO FALTA PARA UM EVENTO".center(60))
        print(("-" * 60) + "\n")

        nome_do_evento = input("Insira o nome do evento que deseja ver quanto tempo falta: ").capitalize().strip()

        tempo_restante_evento(nome_do_evento)

    elif opcoes == "tarefa e orcamento" or opcoes == "to" or opcoes == "6":
        print("\n" + "-" * 60)
        print("  CADASTRAR UM ORÇAMENTO".center(60))
        print(("-" * 60) + "\n")

        nome_do_evento = input("Insira o nome do evento que deseja adcionar as tarefas e atualizar o orçamento: ").capitalize().strip()

        tarefas_orcamento(nome_do_evento)

    elif opcoes == "cadastrar" or opcoes == "forn" or opcoes == "7":
        print("\n" + "-" * 60)
        print("  CADASTRAR FORNECEDORES".center(60))
        print(("-" * 60) + "\n")

        cadastrar_fornecedores()

    elif opcoes == "sugestao" or opcoes == "sug" or opcoes == "8":
        print("\n" + "-" * 60)
        print("  SUGESTÕES DE EVENTOS".center(60))
        print(("-" * 60) + "\n")

        nome_do_evento = input("Insira o nome do evento que deseja ter uma sugestao ").capitalize().strip()
        oferecer_sugestoes(nome_do_evento)

    elif opcoes == "convidados" or opcoes == "9":
        print("\n" + "-" * 60)
        print("  LISTA DE CONVIDADOS".center(60))
        print(("-" * 60) + "\n")

        nome_do_evento = input("Insira o nome do evento que deseja ver a lista de convidados: ").capitalize().strip()
        convidados_evento(nome_do_evento)

    elif opcoes == "painel" or opcoes == "pain" or opcoes == "10":
        print("\n" + "-" * 60)
        print("  PAINEL DE EVENTOS".center(60))
        print(("-" * 60) + "\n")
    
        dashboard()

    else:
        print("Opção inválida.\n")

