import os
from datetime import datetime, timedelta
import random

def adicionar(nome_evento, tipo_evento, data_evento, local_evento, orcamento):
    dados = [nome_evento, tipo_evento, data_evento, local_evento, orcamento]
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
        for dado in dados:
            arquivo.write(dado + "\n")

def visualizar(nome_evento):
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            print(linha.strip())

def excluir(nome_evento):
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

def calcular_lucro_bruto(nome_evento):
    buscar_orcamento = []
    nome_evento_arquivo = nome_evento.replace(' ', '_')
    arquivo_nome = f"{nome_evento_arquivo}.txt"
    with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            buscar_orcamento.append(linha.strip())
    orcamento_do_evento = float(buscar_orcamento[4])

    while True:
        try:
            opcao = int(input("Opção[1] Adicionar os custos um a um\nOpção[2] Já tenho os custos somados\nOpção[3] Sair\n"))

            if opcao == 1:
                custos_do_evento = 0
                while True:
                    custo = input("\nPara ver o resultado digite [sair]\nInsira o número usando apenas digitos:  ")
                    os.system('cls')
                    print(f"O valor de {custo} foi inserido com sucesso!!")

                    if custo == "sair":
                        lucro_bruto = orcamento_do_evento - custos_do_evento
                        print(f"O lucro bruto do evento {nome_evento} é de R${lucro_bruto}\n")

                    elif custo != "sair":
                        custo = float(custo)
                        custos_do_evento = custos_do_evento + custo

            elif opcao == 2:
                custo_somado = float(input("\nPara ver o resultado digite [sair]\nInsira o custo somado do evento utilizando digitos:  "))
                os.system('cls')
                lucro_bruto = orcamento_do_evento - custo_somado
                print(f"O lucro bruto do evento {nome_evento} é de R${lucro_bruto}\n")
                break
            elif opcao == 3:
                print("Voltando ao menu. ")
                os.system('cls')
                break
        except ValueError:
            print("Escolha a opção usando digitos 1 ou 2.")
            
def tempo_restante_evento(nome_evento):
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


def retornando_data_str_E_in_var():
    # essa função retornar a data de hoje (na ordem certa e sem o tempo exato que a data foi requerida ) e o dia 
    # o mes e o ano armazenado como inteiros dentro de variáveis 
    # teste essa função usando a biblioteca datetime e pedindo para printar 
    #dia_hj , mes_hj , ano_hj
    date_today_gr = (datetime.now())
    # vai sair no formato gringo 2025-11-06
    # precisa-se transformar no formato brasileiro em formato brasileiro 06-11-2025
    date_today_gr = str(date_today_gr)
    # por isso vai ser feito um macete para transformar o formato gringo em br
    # 1.pegando o date today e fazendo dele uma lista para
    # separarmos cada parte da data pelo separador '-'
    date_today_list = date_today_gr.split("-")

    # obs : o último item da lista , correspondente ao dia , vem tambem com o
    # os segundos , horas e minutos que essa data foi requerida , por isso vamos ter que
    # capturar só os dois primeiros caracteres do último item da lista e colocalos
    # no lugar da string com o tempo que a pessoa
    #  requeriu essa data (tipo: "06 23:06:56.012503")
    datetoday_Br = ""
    #  =============isolando só o dia
    item_dois_lista = list(date_today_list[2])
    item_dois_lista = item_dois_lista[0:2]
    item_dois_lista = "".join(item_dois_lista)
    date_today_list[2] = item_dois_lista
    # a seguir vai ser usado join , por que o date_today_list[0:2] , sem ele ,
    # iria ser guardado na forma de lista
    date_today_list[2] = "".join(date_today_list[2])
    # ====================
    datetoday_Br += date_today_list[2]
    dia_hj = int(date_today_list[2])
    # colocando a parte dia do mês
    datetoday_Br += "-"
    datetoday_Br += date_today_list[1]
    mes_hj = int(date_today_list[1])
    # colocando a parte do mês do ano
    datetoday_Br += "-"
    # colocando a parte do ano
    datetoday_Br += date_today_list[0]
    ano_hj = int(date_today_list[0])
    return datetoday_Br, dia_hj, mes_hj, ano_hj


date_hj, dia_hj, mes_hj, ano_hj = retornando_data_str_E_in_var()

def tarefas_orcamento(nome_evento):
    nome_evento_arquivo = nome_evento.replace(' ', '')
    arquivo_nome_tarefas = f"{nome_evento_arquivo}_tarefas.txt"
    nomes_tarefas = []
    valores_tarefas = []

    while True:

        desejo = input("Escolha a opção: \n[Adcionar tarefa (add)] \n[Orçamento disponível (orc)] \n[Sair (sair)] ").lower()

        if desejo == "sair" or desejo == "s":
            break

        elif desejo == "add":
            with open(arquivo_nome_tarefas, "a", encoding="utf-8") as arquivo:
                nome_tarefa , valor_tarefa = input("Digite o nome da tarefa e o valor da tarefa [nome,valor]").split(",")
                nomes_tarefas.append(nome_tarefa)
                valores_tarefas.append(float(valor_tarefa))
                for i in range(len(nomes_tarefas)):
                    arquivo.write(f"{nomes_tarefas[i]} - {valores_tarefas[i]}" + "\n")


        elif desejo == "orc":
            dados = []
            buscar_orcamento = []
            arquivo_nome = f"{nome_evento_arquivo}.txt"

            with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    linha = linha.strip()
                    buscar_orcamento.append(linha)

            with open(arquivo_nome_tarefas, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    linha = linha.strip()

                    if not linha:
                        continue  

                    partes = linha.split(" - ")
                    
                    if len(partes) == 2:
                        valor_em_string = partes[1].strip()
                        try:
                            valor = float(valor_em_string)
                            dados.append(valor)
                        except ValueError:
                            print(f"Valor inválido na linha: {linha}")

            valor_total = sum(dados)

                
            orcamento_evento = buscar_orcamento[4]    
            print(f"Orçamento disponivel para o evento {nome_evento}: R$ {orcamento_evento}")
            print(f"Valor restante apos as tarefas: R$ {float(orcamento_evento) - valor_total}")
            break

def oferecer_sugestoes(nome_evento):
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

    if tipo_evento in sugestao_fornecedores:
        fornecedores = sugestao_fornecedores[tipo_evento]
        decoracao = sugestao_decoracao[tipo_evento]
        sugestao_decoracao = random.choice(decoracao)
        sugestao_fornecedores = random.choice(fornecedores)
        print(f"sugestao forn para o evento {nome_evento}: {sugestao_fornecedores}")
        print(f"sugestao decoracao e cadapio para o evento {nome_evento}: {sugestao_decoracao}")
        
    else:
        print(f"nao temos sugestoees no momento.")
