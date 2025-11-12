import os
from datetime import datetime, timedelta
import random


def criar_evento(nome_evento, tipo_evento, data_evento, local_evento):
    """
    Função usada para criar arquivo com base nas informações:
    - Nome do evento
    - Tipo do evento
    - Data do evento
    - Local evento

    """
    try:
        dados = [nome_evento, tipo_evento, data_evento, local_evento]
        nome_evento_arquivo = nome_evento.replace(' ', '_')
        arquivo_nome = f"{nome_evento_arquivo}.txt"
        with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
            for dado in dados:
                arquivo.write(dado + "\n")
    except TypeError:
        print("Digite de forma correta e entendível")
    except ValueError:
        print("Digite palavras, use nmeros apenas na data do evento")
        


def visualizar(nome_evento):
    """
    Função usada para visualizar o evento com base no banco de dados
    """
    try:
        nome_evento_arquivo = nome_evento.replace(' ', '_')
        arquivo_nome = f"{nome_evento_arquivo}.txt"
        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                print(linha.strip())
    except FileNotFoundError:
        print("Esse arquivo não existe, tente criar um evento primeiro")


def excluir(nome_evento):
    """
    Função usada para remover o arquivo do banco de dados
    """
    try:
        nome_evento_arquivo = nome_evento.replace(' ', '_')
        arquivo_nome = f"{nome_evento_arquivo}.txt"
        os.remove(arquivo_nome)
    except FileNotFoundError:
        print(
            f"O evento '{nome_evento}' não foi encontrado. Verifique o nome e tente novamente.")
        return
        print("")


def editar(nome_evento):
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"

    if not os.path.exists(arquivo_nome):
        print(
            f"O evento '{nome_evento}' não foi encontrado. Verifique o nome e tente novamente.")
        print(f"O evento '{nome_evento}' não foi encontrado. Verifique o nome e tente novamente.")
        return

    dados_novos = []

    opcao = input(
        "Qual informação que você deseja alterar: \n"
        "nome - Nome do evento\n"
        "tipo - Tipo do evento\n"
        "data - Data do evento\n"
        "local - Local do evento\n"
        "orc - Orçamento\n"
        "Escolha: "
    ).lower().strip()

    with open(arquivo_nome, "r") as arquivo:
        for linha in arquivo:
            dados_novos.append(linha.strip())

    if opcao == "nome":
        novo_nome = input("Digite o novo nome: ")
        dados_novos[0] = novo_nome
        nome_evento_arquivo = novo_nome.replace(' ', '_')
        arquivo_nome_novo = f"{nome_evento_arquivo}.txt"

        os.remove(arquivo_nome)

        with open(arquivo_nome_novo, "w") as arquivo:
            for item in dados_novos:
                arquivo.write(item + '\n')

        print(f"Arquivo renomeado para: {arquivo_nome_novo}")
        print(f"Para acessar, use: {novo_nome}")

    elif opcao == "tipo":
        novo_tipo = input("Digite o novo tipo: ")
        dados_novos[1] = novo_tipo

    elif opcao == "data":
        nova_data = input("Digite a nova data (XX/YY/ZZZZ): ")
        dados_novos[2] = nova_data

    elif opcao == "local":
        novo_local = input("Digite o novo local: ")
        dados_novos[3] = novo_local

    elif opcao == "orc":
        nova_orc = input("Digite o novo orçamento: ")
        dados_novos[4] = nova_orc

    else:
        print("Opção inválida.")
        return

    if opcao != "nome":
        with open(arquivo_nome, "w") as arquivo:
            for item in dados_novos:
                arquivo.write(item + '\n')

        print("Dados atualizados com sucesso!")

        print("Dados atualizados com sucesso!")

            
def tempo_restante_evento(nome_evento):
    """
    Função usada para visualizar quantos dias faltam para o evento com base na data de hoje
    """
    dados_evento = []
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    try:
        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados_evento.append(linha.strip())
    except FileNotFoundError:

        print("Evento não encontrado - tente cadastrar o evento \nou verifique se você digitou o nome como no cadastro do evento")
        return

    data_evento = dados_evento[2]

    data_evento_brasileiro = datetime.strptime(data_evento, "%d/%m/%Y")
    data_atual = datetime.now()
    quanto_falta = data_evento_brasileiro - data_atual

    if quanto_falta > timedelta(0):
        print(f"Faltam {abs(quanto_falta.days)} dias para o evento!")
    elif quanto_falta == timedelta(0):
        print(f"O evento será hoje!!")
    else:
        print(f"Esse evento já aconteceu há {abs(quanto_falta.days)} dias")


def tarefas_orcamento(nome_evento):
    """
    Função usada para adicionar tarefas e calcular orçamento com base nas tarefas adicionadas
    """

    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    nomes_tarefas = []
    valores_tarefas = []

    while True:

        print("\n" + "-" * 60)
        print("                  GERENCIADOR DE EVENTOS ")
        print("-" * 60)
        print("Escolha a opção:")
        print("[1] - Adicionar tarefa        (add)\n[2] - Orçamento disponível    (orc)\n[3] - Sair                    (sair)")
        desejo = input("→ ").lower()

        if desejo == "sair" or desejo == "s" or desejo == 3:
            break

        elif desejo == "add" or desejo == "a" or desejo == 2 or desejo == "a":
            try:
                nome_tarefa = input("Digite o nome da tarefa: ").strip()
                valor_tarefa = input(
                    f"Digite o custo de {nome_tarefa}").strip()
                nomes_tarefas.append(nome_tarefa)
                valores_tarefas.append(float(valor_tarefa))
            except ValueError:
                print("Erro: digite no formato correto")

        elif desejo == "orc" or desejo == "o" or desejo == 1:
            print(valores_tarefas)
            valor_total = sum(valores_tarefas)
            orcamento_evento = valor_total * 1.25
            print(
                f'Orçamento previsto para o evento: R${orcamento_evento:.2f}')

            with open(arquivo_nome, "a", encoding="utf-8") as arquivo:
                arquivo.write(
                    f"Orçamento total (com margem 25%): R${orcamento_evento:.2f}")


def oferecer_sugestoes(nome_evento):
    """
    Função usada para sugerir fornecedores, decorações e menus
    *Casamento, aniversario e reuniao são definidas como padrão, porem da para criar novas na função [Cadastrar fornecedores]
    """

    dados_do_evento = []
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    try:
        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados_do_evento.append(linha.strip())
    except FileNotFoundError:
        print(f"Cadastro não foi encontrado.")
        escolha = input(
            "Deseja cadastrar esse evento primeiro? (sim/não): ").strip().lower()

        if escolha == "sim":
            nome_do_evento = input(
                "Insira o nome do evento: ").capitalize().strip()
            tipo_do_evento = input(
                "Insira o tipo de evento: ").capitalize().strip()
            data_do_evento = input("Insira a data desta forma (XX/YY/ZZZZ): ")
            local_do_evento = input(
                "Insira o local do evento: ").capitalize().strip()
            criar_evento(nome_do_evento, tipo_do_evento,
                         data_do_evento, local_do_evento)
            orcamento_do_evento = tarefas_orcamento(nome_do_evento)
            print("\n Evento cadastrado com sucesso!")

            nome_evento_arquivo = nome_evento.replace(' ', '_')
            arquivo_nome = f"{nome_evento_arquivo}.txt"

            with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    dados_do_evento.append(linha.strip())

        elif escolha == "não":
            print("Voltando ao menu...")
        else:
            print("Voltando ao menu...")

    tipo_evento = dados_do_evento[1].lower()

    sugestao_fornecedores = {
        "casamento": ["buffet salgueiro", "barreiros eventos", "recife casamentos"],
        "aniversario": ["festas salgueirinho", "niver recife", "niver & cia"],
        "reuniao": ["ceo eventos", "sei la nao sei", "cesar eventos"],
        "festa adulto": ["vitrine", "lounge", "life"]
    }

    sugestao_decoracao = {
        "casamento": ["flores", "musica ao vivo", "buques"],
        "aniversario": ["brinquedos", "baloes", "animadores"],
        "reuniao": ["cartoes de visita", "brindes", "decoracao corporativa"],
        "festa adulto": ["luzes", "dj", "camarotes"]
    }

    sugestao_menu = {
        "casamento": ["jantar completo", "open bar", "coquetel"],
        "aniversario": ["buffet infantil", "doces e salgados", "bolo personalizado"],
        "reuniao": ["coffee break", "almoço executivo", "jantar formal"],
        "festa adulto": ["vodka", "whisky", "gelo"]
    }

    fornecedores_cadastrador = []
    tipos_fornecedores_cadastrados = []

    with open("fornecedores.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            parte1, parte2 = linha.split("-")
            tipos_fornecedores_cadastrados.append(parte1)
            fornecedores_cadastrador.append(parte2)

    for i in range(len(tipos_fornecedores_cadastrados)):
        tipo = tipos_fornecedores_cadastrados[i]
        fornecedor = fornecedores_cadastrador[i]
        if tipo in sugestao_fornecedores:
            sugestao_fornecedores[tipo].append(fornecedor)
        elif tipo not in sugestao_fornecedores:
            sugestao_fornecedores[tipo] = [fornecedor]

    if tipo_evento in sugestao_fornecedores:
        fornecedor_aleatorio = random.choice(
            sugestao_fornecedores[tipo_evento])
        print(f"fornecedor sugestao {fornecedor_aleatorio}")
        print("sugestões de decoração para o seu evento:")
        if tipo_evento in sugestao_decoracao:
            for item in sugestao_decoracao[tipo_evento]:
                print(item)
        print("sugestões de menu para o seu evento:")
        if tipo_evento in sugestao_menu:
            for item in sugestao_menu[tipo_evento]:
                print(item)

    else:
        print("nao temos fornecedores cadastrados para esse tipo, volte ao menu e cadastr")


def cadastrar_fornecedores():
    """
    Função usada para cadastrar novos fornecedores e novos tipos de festas
    """

    arquivo_nome = "fornecedores.txt"
    fornecedores = []

    while True:
        tipo_fornecedor = input(
            "Digite o tipo do fornecedor que deseja cadastrar (ou digite 'sair' para finalizar): ").strip().lower()
        if tipo_fornecedor.lower() == 'sair' or tipo_fornecedor.lower() == "s":
            break
        fornecedor = input(
            "Digite o nome do fornecedor que deseja cadastrar (ou digite 'sair' para finalizar): ").strip().lower()
        if fornecedor.lower() == 'sair' or tipo_fornecedor.lower() == 'sair':
            break
        dados_fornecedor = tipo_fornecedor + "-" + fornecedor
        fornecedores.append(dados_fornecedor)

    with open(arquivo_nome, "a", encoding="utf-8") as arquivo:
        for forn in fornecedores:
            arquivo.write(forn + "\n")


def convidados_evento(nome_evento):
    """
    Função usada para gerenciar a lista de convidados de um evento
    """
    try:
        nome_evento_arquivo = nome_evento.replace(' ', '_')
        arquivo_nome = f"{nome_evento_arquivo}_convidados.txt"
        convidados = []

        while True:
            escolha = input(
                "Deseja adicionar um convidado ou deseja remover um convidado? (adicionar/remover/sair): \n").strip().lower()
            escolha = input("Deseja adicionar um convidado ou deseja remover um convidado? (adicionar/remover/sair): \n").strip().lower()
            if escolha == "sair":
                break

            elif escolha == "remover":
                nome_remover = input(
                    "Digite o nome do convidado que deseja remover: ").strip().lower()
                nome_remover = input("Digite o nome do convidado que deseja remover: ").strip().lower()
                with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
                    for linha in arquivo:
                        convidados.append(linha.strip())
                if nome_remover in convidados:
                    convidados.remove(nome_remover)
                    with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
                        for convidado in convidados:
                            arquivo.write(convidado + "\n")
                    print(f"{nome_remover} foi removido da lista de convidados.")
                else:
                    print(f"{nome_remover} não está na lista de convidados.")

            elif escolha == "adicionar":
                convidado = input(
                    "Digite o nome do convidado que deseja adicionar (ou digite 'sair' para finalizar): ").strip()
                convidado = input("Digite o nome do convidado que deseja adicionar (ou digite 'sair' para finalizar): ").strip()
                if convidado.lower() == "sair":
                    break
                convidados.append(convidado)
        with open(arquivo_nome, "a", encoding="utf-8") as arquivo:
            for convidado in convidados:
                arquivo.write(convidado + "\n")
    except FileNotFoundError:
        print("Esse arquivo não existe. Siga a ordem certa")


def chamar_menu():
    print("------------------------------------------------------------")
    print("                 GERENCIADOR DE EVENTOS                    ")
    print("------------------------------------------------------------")
    print("1 - Adicionar evento")
    print("2 - Visualizar evento")
    print("3 - Editar evento")
    print("4 - Excluir evento")
    print("5 - Ver tempo restante")
    print("6 - Tarefas e orçamento")
    print("7 - Cadastrar fornecedor")
    print("8 - Sugestão de evento")
    print("9 - Lista de convidados do evento")
    print("10 - Sair")
    print("------------------------------------------------------------")
