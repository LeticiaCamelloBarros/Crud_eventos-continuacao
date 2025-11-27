# Projeto: “Organiza Festa” – Sistema de Planejamento de Eventos

Este é um projeto para a matéria de fundamentos de programação do curso de Ciência da Computação da Cesar School.

### Membros do Grupo 7:

- Antônio Gabriel Batista Orrico - CC-A;  
- Guilherme Silva Guimarães - CC-A;
- José Milton Batista Neto - CC-A;  
- Letícia Soares do Nascimento de Camello Barros - CC-A;  
- Luis Henrique Alves Sampaio Santos - CC-A;  
- Luiz Henrique Lins da Costa - CC-A;

## Objetivos do projeto

Esse projeto tem como função criar um CRUD de eventos utilizando funçoes e manipulação de arquivos em python. Onde o usuário pode criar, visualizar, editar e excluir eventos. Além do nome do evento, sua classificação (aniversário, reunião, etc.), data de acontecimento, local demarcado e orçamento estipulado.

# Manual de uso do programa

## Funcionalidades  do programa:

- Funcionalidade Adicionar:  
É uma função que cria um arquivo com base nas informações que serão adicionadas pelo usuário.  
  - Nome do evento;
  - Tipo de evento (aniversário, reunião, etc.);
  - Data do evento;
  - Local do evento;  

- Funcionalidade Visualizar:  
É uma função usada para visualizar o evento com base no banco de dados criado pela função adicionar.

- Funcionalidade Editar:  
É uma função usada para editar as informações do evento criado anteriormente.  
  - Nome do evento;
  - Tipo de evento (aniversário, reunião, etc.);
  - Data do evento;
  - Local do evento;

- Funcionalidade Excluir:  
É uma função criada para excluir eventos do banco de dados.

- Funcionalidade Tempo Restante:  
É uma função que mostra quantos dias faltam para o evento ocorrer.

- Funcionalidade Tarefas/Orçamento:  
É uma função que você pode adicionar tarefas a serem feitas para o seu evento e o orçamento disponível para realização dessas atividades.

- Funcionalidade Oferecer Sugestões:  
É uma função usada para sugerir decorações, comidas e músicas para o evento. __*Casamentos e aniversários são tratados como eventos padrão*__.

- Funcionalidade Cadastras Fornecedor:  
É uma função que permite cadastrar fornecedores para o evento, como buffet, decoração, música, etc.

- Funcionalidade extra : painel de eventos .
  * mostra todos os eventos atualmente cadastrados ( excluso os deletados )  

## Como executar o programa:

No menu principal, o usuário tem que escollher entre as funções disponíveis. 

```python
---------------MENU ORGANIZA FESTA------------
    Escolha o que você deseja fazer:  
    Adicionar  
    Visualizar  
    Editar  
    Excluir
```

Para selecionar a função desejada, o usuário deve digitar o nome da função (pode ser em letras minúsculas ou maiúsculas) como esta sendo mostrada. Após selecionar a função, o usuário será guiado por perguntas para completar a ação escolhida.
Exemplo:  
```python
    Escolha o que você deseja fazer: 
    Adicionar

    Nome do evento: Aniversário do João
    Tipo de evento: Aniversário
    Data do evento (DD/MM/AAAA): 10/11/2025
    Local do evento: Salão de festas
    Evento 'Aniversário do João' adicionado com sucesso!
```
