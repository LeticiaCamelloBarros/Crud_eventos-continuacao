import os
from datetime import datetime, timedelta
import random


def adicionar(nome_evento, tipo_evento, data_evento, local_evento, orcamento):
    """
    Função usada para criar arquivo com base nas informações:
    - Nome do evento
    - Tipo do evento
    - Data do evento
    - Local evento
    - Orçamento evento
    """

    while True:
        try:
            data_evento = datetime.strptime(data_evento, "%d/%m/%Y")
            break  
        except ValueError:
            print("Data inválida! Digite novamente no formato DD/MM/AAAA.")
            data_evento = input("Data do evento: ")  

    dados = [nome_evento, tipo_evento, data_evento, local_evento, orcamento]
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"

    with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
        for dado in dados:
            arquivo.write(str(dado) + "\n")


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
        print(f"Evento '{nome_evento}' removido com sucesso!")

    except FileNotFoundError:
        print(f"O evento '{nome_evento}' não foi encontrado. Verifique o nome e tente novamente.")

def editar(nome_evento):
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"

    if not os.path.exists(arquivo_nome):
        print(f"O evento '{nome_evento}' não foi encontrado. Verifique o nome e tente novamente.")
        return

    dados_novos = []

    opcao = input("Qual informação que você deseja alterar: \nnome - Nome do evento\ntipo - Tipo do evento\ndata - Data do evento\n local - Local do evento\norc - Orçamento\nEscolha: ").lower().strip()

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
    if not os.path.exists(arquivo_nome):
        print(f"O evento '{nome_evento}' não foi encontrado. Verifique o nome e tente novamente.")
        return

    nomes_tarefas = []
    valores_tarefas = []
    dados = []

    while True:

        print("\n" + "-" * 60)
        print("                  GERENCIADOR DE EVENTOS ")
        print("-" * 60)

        print("Escolha a opção:")
        print("[1] - Adicionar tarefa        (add)\n[2] - Orçamento disponível    (orc)\n[3] - Sair                    (sair)")
        desejo = input("→ ").lower()

        if desejo == "sair" or desejo == "s" or desejo == "3":
            break

        elif desejo == "add" or desejo == "1":
            try:
                nome_tarefa = input("Digite o nome da tarefa: ").strip()
                valor_tarefa = input(f"Digite o custo da tarefa [{nome_tarefa}]: ").strip()
                nomes_tarefas.append(nome_tarefa)
                valores_tarefas.append(float(valor_tarefa))
            except ValueError:
                print("Erro: digite no formato correto")
            except TypeError: 
                print("Erro: digite no formato correto")

        elif desejo == "orc" or desejo == "2":
            with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    dados.append(linha.strip())
            orcamento_total = int(dados[4])

            print(valores_tarefas)
            custo_total = sum(valores_tarefas)
            orcamento_evento = orcamento_total - custo_total
            dados[4] = orcamento_evento 
            print(f'Orçamento restante para o evento: R${orcamento_evento:.2f}')

            with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
                for linha in dados:
                    arquivo.write(str(linha) + "\n")

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
        fornecedor_aleatorio = random.choice(sugestao_fornecedores[tipo_evento])

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
    arquivo_nome = "fornecedores.txt"
    fornecedores = []

    while True:
        tipo_fornecedor = input("Digite o tipo do fornecedor que deseja cadastrar (ou digite 'sair' para finalizar): ").strip().lower()
        if tipo_fornecedor.lower() == 'sair':
            break

        fornecedor = input("Digite o nome do fornecedor que deseja cadastrar (ou digite 'sair' para finalizar): ").strip().lower()

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
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}_convidados.txt"
    convidados = []
    try:
        while True:
            convidado = input("Digite o nome do convidado que deseja adicionar (ou digite 'sair' para finalizar): ").strip()
            if convidado.lower() == 'sair':
                break
            convidados.append(convidado)

        with open(arquivo_nome, "a", encoding="utf-8") as arquivo:
            for convidado in convidados:
                arquivo.write(convidado + "\n")
    except TypeError:
        print("Erro de digitação")
    except ValueError:
        print("Erro de valor")

def chamar_menu():
    print()
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
    print("10 - Painel geral")
    print("11 - Sair")
    print("------------------------------------------------------------")

def dashboard():
    """
    Função usada para mostrar um painel geral dos eventos cadastrados
    """

    pasta_eventos = "." 
    arquivos = []
    for arquivo in os.listdir(pasta_eventos):
        if arquivo.endswith(".txt") and not arquivo == "fornecedores.txt" and not arquivo.endswith("_convidados.txt"):
            arquivos.append(arquivo)

    total_eventos = 0
    proximos_eventos = 0
    eventos_passados = 0
    eventos_futuros = 0

    gastos_totais = 0
  

    evento_mais_perto = None
    data_mais_perto = None

    evento_mais_longe = None
    data_mais_longe = None

    hoje = datetime.now()

    lista_eventos_passados = []

    for arquivo in arquivos:
        nome_evento = arquivo.replace(".txt", "")
        total_eventos += 1
        linhas = []

        with open(arquivo, "r", encoding="utf-8") as file:
            for linha in file:
                linhas.append(linha.strip())
            print(linhas)
            data_arquivo = (linhas[2])
            valor_orca = float(linhas[4])

        data_evento_dashboard = datetime.strptime(data_arquivo, "%d/%m/%Y")
        gastos_totais += valor_orca

        if data_evento_dashboard:
            if data_evento_dashboard.date() == hoje.date():
                proximos_eventos += 1
            elif data_evento_dashboard < hoje:
                eventos_passados += 1
            else:
                eventos_futuros += 1

            if data_evento_dashboard > hoje:
                if data_mais_perto is None or data_evento_dashboard < data_mais_perto:
                    data_mais_perto = data_evento_dashboard
                    evento_mais_perto = nome_evento

            if data_evento_dashboard > hoje:
                if data_mais_longe is None or data_evento_dashboard > data_mais_longe:
                    data_mais_longe = data_evento_dashboard
                    evento_mais_longe = nome_evento


    print("\n==================== PAINEL GERAL ====================")
    print(f"Total de eventos cadastrados: {total_eventos}")
    print(f"Eventos próximos (hoje): {proximos_eventos}")
    print(f"Eventos futuros: {eventos_futuros}")
    print(f"Eventos passados: {eventos_passados}")
    print("------------------------------------------------------")
    print(f"Gastos totais estimados: R$ {gastos_totais:.2f}")
    print("------------------------------------------------------")

    if evento_mais_perto:
        print(f"Próximo evento: {evento_mais_perto} - {data_mais_perto.strftime("%d/%m/%Y")}")
    else:
        print("Nenhum evento futuro encontrado.")

    if evento_mais_longe:
        print(f"Evento mais distante: {evento_mais_longe} - {data_mais_longe.strftime("%d/%m/%Y")}")
    else:
        print("Nenhum evento futuro encontrado.")

    if eventos_passados:
        print("Eventos passados:")
        for i in range(len(lista_eventos_passados)):
            print(lista_eventos_passados[i])

    print("======================================================\n")