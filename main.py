from funcoes import *
import os
os.system("cls")

while True:
    print("--------------------MENU ORGANIZA FESTA--------------------")
    opcoes = input(
        "escolha o que você deseja fazer: \nAdicionar Eventos \nVisualizar Eventos \nEditar Eventos \nExcluir Eventos \nSair \nEscolha: ").lower()

    if opcoes == "sair":
        break

    elif opcoes == "adicionar" or opcoes == "add":
        nome_do_evento = input("Insira o noem do evento: ").capitalize().strip()
        tipo_do_evento = input("Insira o tipo de evento: ").capitalize().strip()
        data_do_evento = input("Insira a data desta forma (XX/YY/ZZZZ): ")
        local_do_evento = input("Insira o local do evento: ").capitalize().strip()
        orcamento_do_evento = input("Insira o orçamento utilizando digitos: ")
        adicionar(nome_do_evento, tipo_do_evento, data_do_evento, local_do_evento, orcamento_do_evento)
        continue

    elif opcoes == "visualizar" or opcoes == "visu":
        nome_do_evento = input("Insira o nome do evento: ").capitalize().strip()
        print()
        visualizar(nome_do_evento)
        continue

    elif opcoes == "excluir" or opcoes == "exc":
        continue

    elif opcoes == "editar" or opcoes == "edt":
        continue
