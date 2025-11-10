import os
from datetime import datetime, timedelta
import random

def adicionar(nome_evento, tipo_evento, data_evento, local_evento):
    """
    Função usada para criar arquivo com base nas informações:
    - Nome do evento
    - Tipo do evento
    - Data do evento
    - Local evento

    """

    dados = [nome_evento, tipo_evento, data_evento, local_evento]
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
        for dado in dados:
            arquivo.write(dado + "\n")

def visualizar(nome_evento):
    """
    Função usada para visualizar o evento com base no banco de dados
    """

    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            print(linha.strip())

def excluir(nome_evento):
    """
    Função usada para remover o arquivo do banco de dados
    """

    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    os.remove(arquivo_nome)

def editar(nome_evento):
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    dados_novos = []

    opcao = input("Qual informação que você deseja alterar: \nNome do evento \nTipo do evento \nData do evento \nLocal do evento \nOrçamento \nEscolha: ")

    arquivo = open(arquivo_nome, "r")
    for linha in arquivo:
            dados_novos.append(linha.strip())
    arquivo.close()
                               
    if opcao == "nome":
        novo_nome = input("Digite o novo nome: ")
        dados_novos[0] = novo_nome
        nome_evento_arquivo = novo_nome.replace(' ', '_')
        arquivo_nome_novo = f"{nome_evento_arquivo}.txt"
        os.remove(arquivo_nome)

        with open(arquivo_nome_novo, "w") as arquivo:
            for itens in dados_novos:    
                arquivo.write(itens + '\n')
        print(f"Arquivo com novo nome {arquivo_nome_novo}")
        print(f"Para acessar use: {novo_nome}")
                 

    elif opcao == "tipo":
        novo_tipo = input("Digite o novo tipo: ")
        dados_novos[1] = novo_tipo

    elif opcao == "data":
        nova_data = input("Digite a nova data desta forma (XX/YY/ZZZZ): ")
        dados_novos[2] = nova_data
            
    elif opcao == "local":
        novo_local = input("Digite o novo local: ")
        dados_novos[3] = novo_local

    elif opcao == "orc":
        nova_orc = input("Digite o novo orçamento: ")
        dados_novos[4] = nova_orc

    if opcao != "nome":
        with open(arquivo_nome, "w") as arquivo:
            for itens in dados_novos:
                arquivo.write(itens + '\n')
            
def tempo_restante_evento(nome_evento):
    """
    Função usada para visualizar quantos dias faltam para o evento com base na data de hoje
    """

    dados_evento = []
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados_evento.append(linha.strip())
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
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    nomes_tarefas = []
    valores_tarefas = []

    while True:

        desejo = input("Escolha a opção: \n[Adicionar tarefa (add)] \n[Orçamento disponível (orc)] \n[Sair (sair)] ").lower()

        if desejo == "sair" or desejo == "s":
            break

        elif desejo == "add":
            try:
                nome_tarefa = input("Digite o nome da tarefa: ").strip()
                valor_tarefa = input(f"Digite o custo de {nome_tarefa}").strip()
                nomes_tarefas.append(nome_tarefa)
                valores_tarefas.append(float(valor_tarefa))
            except ValueError: 
                print("Erro: digite no formato correto")

        elif desejo == "orc":
            print(valores_tarefas)
            valor_total = sum(valores_tarefas)
            orcamento_evento = valor_total * 1.25  
            print(f'Orçamento previsto para o evento: R${orcamento_evento:.2f}')

            with open(arquivo_nome, "a", encoding="utf-8") as arquivo:
                arquivo.write(f"\nOrçamento total (com margem 25%): R${orcamento_evento:.2f}\n")

def oferecer_sugestoes(nome_evento):
    """
    Função usada para sugerir fornecedores e decorações
    *Casamento, aniversario e reuniao são definidas como padrão, porem da para criar novas na função [Cadastrar fornecedores]
    """

    dados_do_evento = []   
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados_do_evento.append(linha.strip())
    
    tipo_evento = dados_do_evento[1].lower()

    sugestao_fornecedores = {
        "casamento": ["buffet salgueiro", "barreiros eventos", "recife casamentos"],
        "aniversario": ["festas salgueirinho", "niver recife", "niver & cia"],
        "reuniao": ["ceo eventos", "sei la nao sei", "cesar eventos"]
    }

    sugestao_decoracao = {
        "casamento": ["flores", "bolo de noiva", "buques"],
        "aniversario": ["doces", "sorvete", "animadores"],
        "reuniao": ["cafe", "brindes", "lanches"]
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
        
    else:
        print("nao temos fornecedores cadastrados para esse tipo, volte ao menu e cadastr")

def cadastrar_fornecedores():
    """
    Função usada para cadastrar novos fornecedores e novos tipos de festas
    """

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