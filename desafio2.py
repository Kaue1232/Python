# Sistema de controle de gastos residenciais, incluindo cadastro de pessoas, cadastro de transações e consulta totais

class Pessoa: #Classe pessoa serve para criar o objeto pessoa, para armazenas os dados
    def __init__(self, identificador, nome, idade): 
        self.idenficador = identificador
        self.nome = nome
        self. idade = idade

def cadastrar_pessoas(pessoas, identificador, nome, idade):
    if identificador in pessoas:
        print('Identificador já cadastrado!')

    else:
        pessoas[identificador] = pessoas(identificador,nome,idade)
        print('Pessoa {} cadastrada com sucesso!'.format(identificador))

class transacao:
    def __init__(self,identificador,descricao, valor, tipo, pessoa_id):
        self.identificador = identificador
        self.descricao = descricao
        self.valor = valor
        self. tipo = tipo
        self.pessoa_id = pessoa_id

def registrar_transacao(identificado,descricao,valor,tipo,pessoa_id):
    transacao.append(transacao(pessoa_id, valor, descricao))
    print("Transação de {} registrada para o ID {}".format(valor,pessoa_id))

def consultar_total_gastos(transacoes, pessoa_id):
    total = sum(t.valor for t in transacoes if t.pessoa_id == pessoa_id)
    print("Total gasto pela pessoa {}: {}".format(pessoa_id, total))
    return total

def main():
    pessoas = {}
    transacoes = [] 
    

    print('\nMenu')
    print('1- Cadastrar pessoa')
    print('2- Cadastrar transação')
    print('3- Consultar gastos totais')
    print('4- Sair')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        identificador = int(input('Id: '))
        nome = str(input('Nome completo: '))
        idade = int(input('idade: ')) 
    elif opcao == 2:
        identificador = int(input('Id:'))
        descricao = str(input('Descrição: '))
        valor = float(input('Valor'))
        tipo_transacao = {1:"receita", 2: "despesa"}
        tipo = int(tipo_transacao)
    elif opcao == 3:
        pessoa_id = input("Id da pessoa: ")
        if pessoa_id not in pessoas:
            print('Pessoa não encontrada!')
        else:
            consultar_total_gastos(transacoes, pessoa_id)
    elif opcao == "4":
            print('Volte sempre!')
    else:
        print("Opção inválida!")

      


        


