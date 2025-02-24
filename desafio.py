

from collections import defaultdict

class Pessoa: 
    def __init__(self, identificador, nome, idade):  # Uma função para declarar os atributos do objeto "Pessoa"
        self.identificador = identificador
        self.nome = nome
        self.idade = idade

def cadastrar_pessoa(pessoas, identificador, nome, idade): # função que recebe 4 parâmetros
    if identificador in pessoas: # Se o identificador já estiver em pessoas, o programa irá mostrar que o identificador já foi cadastrado
        print('Identificador já cadastrado!')
    else:
        pessoas[identificador] = Pessoa(identificador, nome, idade) # Se não, vai criar uma nova instância, passando os parâmetros para a pessoa
        print('Pessoa {} cadastrada com sucesso!'.format(nome)) # Imprimir o nome da pessoa

class Transacao:
    def __init__(self, identificador, descricao, valor, tipo, pessoa_id): # função que recebe 6 parâmetros
        self.identificador = identificador
        self.descricao = descricao
        self.valor = valor
        self.tipo = tipo 
        self.pessoa_id = pessoa_id

def registrar_transacao(transacoes, pessoas, identificador, descricao, valor, tipo, pessoa_id):
    if pessoa_id not in pessoas:
        print('Pessoa não encontrada!') # Se o id da pessoa não estiver dentro do parâmetro pessoas, vai imprimir como "Pessoa não encontrada"
        return
    if pessoas[pessoa_id].idade < 18 and tipo == "receita": # Se no id da pessoa constatar que ela é menor de idade, irá informar que essa pessoa só pode ter despesas
        print('Menores de 18 anos só podem registrar despesas!')
        return
    transacoes.append(Transacao(identificador, descricao, valor, tipo, pessoa_id))
    print('Transação de {} registrada para {}'.format(valor, pessoa_id))



def consultar_total(transacoes, pessoas):
    totais = defaultdict(lambda: {'receita': 0, 'despesa': 0})
    
    for transacao in transacoes:
        totais[transacao.pessoa_id][transacao.tipo] += transacao.valor
    
    total_receita_geral = sum(valores['receita'] for valores in totais.values()) # Somando todas as receitas registradas 
    total_despesa_geral = sum(valores['despesa'] for valores in totais.values()) # Somando todas as despesas registradas
    saldo_geral = total_receita_geral - total_despesa_geral # Saldo geral é o valor total da receita - o total da despesa

    print("\nResumo por Pessoa:") # Resumo como se fosse um relatório, 
    for pessoa_id, valores in totais.items():
        receita, despesa = valores['receita'], valores['despesa']
        saldo = receita - despesa
        print('Pessoa {} - Receita: {}, Despesa: {}, Saldo: {:.2f}'.format(pessoa_id, receita, despesa, saldo))
    
    print("\nResumo Geral:")
    print('Total Receita: {}, Total Despesa: {}, Saldo Líquido: {:.2f}'.format(total_receita_geral, total_despesa_geral, saldo_geral))


def main():
    pessoas = {}
    transacoes = []
    while True:
        print('\nMenu')
        print('1- Cadastrar pessoa')
        print('2- Cadastrar transação')
        print('3- Consultar totais')
        print('4- Sair')
        
        opcao = int(input('Escolha uma opção: ')) 
        
        if opcao == '1': 
            identificador = int(input('Id: '))
            nome = input('Nome completo: ')
            idade = int(input('Idade: '))
            cadastrar_pessoa(pessoas, identificador, nome, idade)
        
        elif opcao == '2': 
            identificador = int(input('Id da transação: '))
            pessoa_id = int(input('Id da pessoa: '))
            descricao = input('Descrição: ')
            valor = float(input('Valor: '))
            tipo = input('Tipo (receita/despesa): ').strip().lower()
            if tipo not in ['receita', 'despesa']:
                print('Tipo inválido! Use "receita" ou "despesa".')
                continue
            registrar_transacao(transacoes, pessoas, identificador, descricao, valor, tipo, pessoa_id)
        
        elif opcao == '3':
            pessoa_id = input("ID da pessoa: ")
            if pessoa_id not in pessoas:
                print("Pessoa não encontrada!")
            else:
                consultar_total(transacoes, pessoa_id)
        
        elif opcao == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida!')

if __name__ == "__main__":
    main()
