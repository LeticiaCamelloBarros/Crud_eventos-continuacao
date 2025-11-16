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
        

    dados = [nome_evento, tipo_evento, data_evento, local_evento, orcamento]
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
        for dado in dados:
            arquivo.write(dado + "\n")


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

    opcao = input("Qual informação que você deseja alterar: \n"
        "nome - Nome do evento\n"
        "tipo - Tipo do evento\n"
        "data - Data do evento\n"
        "local - Local do evento\n"
        "orc - Orçamento\n"
        "Escolha: ").lower().strip()

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
    dados = []

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
                    f"Digite o custo de {nome_tarefa}: ").strip()
                nomes_tarefas.append(nome_tarefa)
                valores_tarefas.append(float(valor_tarefa))
            except ValueError:
                print("Erro: digite no formato correto")

        elif desejo == "orc":
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
        escolha = input(
            "Deseja cadastrar esse evento primeiro? (sim/não): ").strip().lower()

        if escolha == "sim":
            nome_do_evento = input("Insira o nome do evento: ").capitalize().strip()

            tipo_do_evento = input("Insira o tipo de evento: ").capitalize().strip()

            data_do_evento = input("Insira a data desta forma (XX/YY/ZZZZ): ")

            local_do_evento = input("Insira o local do evento: ").capitalize().strip()

            orcamento = input("Insira o orçamento do evento: ")

            adicionar(nome_do_evento, tipo_do_evento, data_do_evento, local_do_evento,orcamento )

            print("\n Evento cadastrado com sucesso!")

            nome_evento_arquivo = nome_evento.replace(' ', '_')
            arquivo_nome = f"{nome_evento_arquivo}.txt"

            with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    dados_do_evento.append(linha.strip())

        elif escolha == "não":
            print("Voltando ao menu...")
            chamar_menu()
        else:
            print("Voltando ao menu...")
            chamar_menu()

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
        print("nao temos fornecedores cadastrados para esse tipo, volte ao menu e cadastro")


def oferecer_sugestoes(nome_evento):
    """
    Função usada para sugerir fornecedores, decorações e menus
    *Casamento, aniversario e reuniao são definidas como padrão, porem da para criar novas na função [Cadastrar fornecedores]
    """

    dados_do_evento = []
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"

    # --- TENTAR LER O ARQUIVO DO EVENTO ---
    try:
        with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados_do_evento.append(linha.strip())

    except FileNotFoundError:
        print("Cadastro não foi encontrado.")
        escolha = input(
            "Deseja cadastrar esse evento primeiro? (sim/não): "
        ).strip().lower()

        if escolha == "sim":
            nome_do_evento = input(
                "Insira o nome do evento: "
            ).capitalize().strip()
            tipo_do_evento = input(
                "Insira o tipo de evento: "
            ).capitalize().strip()
            data_do_evento = input("Insira a data desta forma (XX/YY/ZZZZ): ")
            local_do_evento = input(
                "Insira o local do evento: "
            ).capitalize().strip()

            criar_evento(nome_do_evento, tipo_do_evento,
                         data_do_evento, local_do_evento)
            orcamento_do_evento = tarefas_orcamento(nome_do_evento)
            print("\n Evento cadastrado com sucesso!")

            # AQUI TINHA UM BUG: estava usando nome_evento (antigo)
            nome_evento_arquivo = nome_do_evento.replace(' ', '_')
            arquivo_nome = f"{nome_evento_arquivo}.txt"

            try:
                with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
                    for linha in arquivo:
                        dados_do_evento.append(linha.strip())
            except Exception as e:
                print(f"Erro ao ler o evento recém-criado: {e}")
                return

        else:
            print("Voltando ao menu...")
            return  # IMPORTANTE: não seguir sem dados_do_evento

    # GARANTIR QUE TEM PELO MENOS 2 LINHAS (NOME E TIPO)
    if len(dados_do_evento) < 2:
        print("Arquivo do evento está em um formato inesperado (faltando tipo).")
        return

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

    # --- LER fornecedores.txt COM TRATAMENTO DE ERRO ---
    try:
        with open("fornecedores.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if "-" not in linha:
                    # linha mal formatada, ignora para não quebrar
                    continue
                parte1, parte2 = linha.split("-", 1)
                tipos_fornecedores_cadastrados.append(parte1)
                fornecedores_cadastrador.append(parte2)
    except FileNotFoundError:
        # Se não existir, só usa os fornecedores padrão
        pass
    except Exception as e:
        print(f"Erro ao ler fornecedores cadastrados: {e}")

    # --- JUNTAR FORNECEDORES CADASTRADOS COM OS PADRÕES ---
    for i in range(len(tipos_fornecedores_cadastrados)):
        tipo = tipos_fornecedores_cadastrados[i].lower()
        fornecedor = fornecedores_cadastrador[i]
        if tipo in sugestao_fornecedores:
            sugestao_fornecedores[tipo].append(fornecedor)
        else:
            sugestao_fornecedores[tipo] = [fornecedor]

    # --- SUGESTÕES DE ACORDO COM O TIPO DO EVENTO ---
    if tipo_evento in sugestao_fornecedores:
        if len(sugestao_fornecedores[tipo_evento]) > 0:
            fornecedor_aleatorio = random.choice(
                sugestao_fornecedores[tipo_evento]
            )
            print(f"fornecedor sugestao: {fornecedor_aleatorio}")
    else:
        print("Ainda não há fornecedores sugeridos para esse tipo de evento.")

    print("sugestões de decoração para o seu evento:")
    if tipo_evento in sugestao_decoracao:
        for item in sugestao_decoracao[tipo_evento]:
            print(item)

    print("sugestões de menu para o seu evento:")
    if tipo_evento in sugestao_menu:
        for item in sugestao_menu[tipo_evento]:
            print(item)



def cadastrar_fornecedores():
    """
    Função usada para cadastrar novos fornecedores e tipos de fornecedores.
    """

    arquivo_nome = "fornecedores.txt"
    fornecedores = []

    while True:
        tipo_fornecedor = input("Digite o tipo do fornecedor que deseja cadastrar (ou digite 'sair' para finalizar): ").strip().lower()

        if tipo_fornecedor.lower() == 'sair' or tipo_fornecedor.lower() == "s":
            break

        fornecedor = input("Digite o nome do fornecedor que deseja cadastrar (ou digite 'sair' para finalizar): ").strip().lower()
        
        if fornecedor.lower() == 'sair' or tipo_fornecedor.lower() == 'sair':
            break
        dados_fornecedor = tipo_fornecedor + "-" + fornecedor
        fornecedores.append(dados_fornecedor)

        if tipo_fornecedor in ("sair", "s"):
            break

        if not tipo_fornecedor:
            print("Tipo não pode ser vazio.")
            continue



def convidados_evento(nome_evento):
    
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}_convidados.txt"
    convidados = []

    while True:
        escolha = input("Deseja adicionar um convidado ou deseja remover um convidado? (adicionar/remover/sair): \n").strip().lower()
        if escolha == "sair":
            break

        elif escolha == "remover":
            nome_remover = input("Digite o nome do convidado que deseja remover: ").strip().lower()
            try:
                with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
                    for linha in arquivo:
                        convidados.append(linha.strip().lower())
                if nome_remover in convidados:
                    convidados.remove(nome_remover)
                    with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
                        for convidado in convidados:
                            arquivo.write(convidado + "\n")
                    print(f"{nome_remover} foi removido da lista de convidados.")
                else:
                    print("Opção inválida. Este nome não está na lista de convidados.")
            except FileNotFoundError:
                print("Arquivo não encontrado. Nenhum convidado foi cadastrado ainda.")

        elif escolha == "adicionar":

            convidado = input("Digite o nome do convidado que deseja adicionar (ou digite 'sair' para finalizar): ").strip()

            convidado = input("Digite o nome do convidado que deseja adicionar (ou digite 'sair' para finalizar): ").strip()

            if convidado.lower() == "sair":
                break
        convidados.append(convidado)

        with open(arquivo_nome, "a", encoding="utf-8") as arquivo:
            for convidado in convidados:
                arquivo.write(convidado + "\n")


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
    print()




def dashboard():

    pasta_eventos = "." 
    arquivos = []
    for arquivo in os.listdir(pasta_eventos):
        if arquivo.endswith(".txt"):
            arquivos.append(arquivo)

    total_eventos = 0
    proximos_eventos = 0
    eventos_passados = 0
    eventos_futuros = 0

    gastos_totais = 0
    lucro_estimado = 0

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
            valor_orca = int(linhas[4])

        try:
            data_evento = datetime.strptime(data_arquivo, "%d/%m/%Y")
        except ValueError:
            print(f"Data inválida encontrada no arquivo '{arquivo}'!")
            continue
        gastos_totais += valor_orca

        if data_evento.date() == hoje.date():
            proximos_eventos += 1

        elif data_evento < hoje:
            eventos_passados += 1
            lista_eventos_passados.append(nome_evento)
        else:
            eventos_futuros += 1

            if data_evento > hoje:
                if data_mais_perto is None or data_evento < data_mais_perto:
                    data_mais_perto = data_evento
                    evento_mais_perto = nome_evento

            if data_evento > hoje:
                if data_mais_longe is None or data_evento > data_mais_longe:
                    data_mais_longe = data_evento
                    evento_mais_longe = nome_evento


    print("\n==================== PAINEL GERAL ====================")
    print(f"Total de eventos cadastrados: {total_eventos}")
    print(f"Eventos próximos (hoje): {proximos_eventos}")
    print(f"Eventos futuros: {eventos_futuros}")
    print(f"Eventos passados: {eventos_passados}")
    print("------------------------------------------------------")
    print(f"Gastos totais estimados: R$ {gastos_totais:.2f}")
    print(f"Lucro líquido estimado: R$ {lucro_estimado:.2f}")
    print("------------------------------------------------------")

    if evento_mais_perto:
        print(f"Próximo evento: {evento_mais_perto} - {data_mais_perto.strftime('%d/%m/%Y')}")
    else:
        print("Nenhum evento futuro encontrado.")

    if evento_mais_longe:
        print(f"Evento mais distante: {evento_mais_longe} - {data_mais_longe.strftime('%d/%m/%Y')}")
    else:
        print("Nenhum evento futuro encontrado.")

    if eventos_passados:
        print("Eventos passados:")
        for i in range(len(lista_eventos_passados)):
            print(lista_eventos_passados[i])

    print("======================================================\n")
