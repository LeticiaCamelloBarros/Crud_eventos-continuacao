from funcoes import *
import os
os.system("cls")


while True:
    print("--------------------MENU ORGANIZA FESTA--------------------")
    opcoes = input("Escolha o que você deseja fazer: \nAdicionar  \nVisualizar \nEditar \nLucro Bruto  \nExcluir \nTempo \nTarefa e Orcamento \nSair \nEscolha: ").lower()

    if opcoes == "sair":
        break

    elif opcoes == "adicionar" or opcoes == "add":
        nome_do_evento = input("Insira o nome do evento: ").capitalize().strip()
        tipo_do_evento = input("Insira o tipo de evento: ").capitalize().strip()
        data_do_evento = input("Insira a data desta forma (XX/YY/ZZZZ): ")
        local_do_evento = input("Insira o local do evento: ").capitalize().strip()
        orcamento_do_evento = input("Insira o orçamento utilizando digitos: ")
        adicionar(nome_do_evento, tipo_do_evento, data_do_evento, local_do_evento, orcamento_do_evento)
        
    elif opcoes == "visualizar" or opcoes == "visu":
        # captura a data de hoje 
        # pegando a data no formato gringo , transforma no brasileiro e atribui à uma variável o dia do mês , o mês e o ano em inteiro usando a função abaixo
        data_hj , dia_hj , mes_hj , ano_hj = retornando_data_str_E_in_var()
        nome_do_evento = input("Insira o nome do evento: ").capitalize().strip()
        print()
        visualizar(nome_do_evento)
        
    elif opcoes == "excluir" or opcoes == "exc":
        nome_do_evento = input("Insira o nome do evento que deseja apagar: ").capitalize().strip()
        excluir(nome_do_evento)

    elif opcoes == "lucro bruto" or opcoes == "lb":
        nome_do_evento = input("Insira o nome do evento que deseja editar: ").capitalize().strip()
        calcular_lucro_bruto(nome_do_evento)


    elif opcoes == "editar" or opcoes == "edit":
        nome_do_evento = input("Insira o nome do evento que deseja editar: ").capitalize().strip()
        editar(nome_do_evento)

    elif opcoes == "tempo" or opcoes == "time":
        nome_do_evento = input("Insira o nome do evento que deseja ver quanto tempo falta: ").capitalize().strip()
        tempo_restante_evento(nome_do_evento)
        