from time import sleep
import json

# Tenho que abrir uma lista vazia pois vou armazenar os valores dentro dela (empresas cadastradas esse caso)
empresas = []

def escolha():
    continuar = True
    while continuar:
        opcao = int(input('\n[1] CADASTRAR EMPRESA \n[2] EDITAR EMPRESA \n[3] MOSTRAR EMPRESAS \n[4] EXCLUIR EMPRESA \n[5] FAZER BACKUP \n[0] SAIR \n \nQual dessas opções você desejar utilizar? '))

        if opcao == 1:
            cadastrar_empresas()
        elif opcao == 2:
            editar_empresa()
        elif opcao == 3:
            mostrar_empresas()
        elif opcao == 4:
            excluir_empresa()
        elif opcao == 5:
            fazer_backup()
        elif opcao == 0:
            continuar = sair()
        else:
            print('Digite uma opção válida! \n', opcao)

def cadastrar_empresas():
    nome = input('Digite o nome da empresa: ')
    cnpj = input('Digite o CNPJ da empresa (apenas números): ')

    # Criando um dicionário para representar a empresa   
    empresa = {'nome': nome, 'cnpj': cnpj}    # O uso de ':' denomina que você está associando o valor da variável nome à chave 'nome'
    empresas.append(empresa)
    print('Empresa',nome,'cadastrada com sucesso!')

def editar_empresa():
    # Chama a função mostrar_empresas() para exibir todas as empresas cadastradas
    mostrar_empresas()

    # Solicita ao usuário o índice da empresa que deseja editar
    indice = int(input('Digite o índice da empresa que deseja editar: '))

    # Verifica se o valor de indice é maior ou igual a 1 e ao mesmo tempo menor ou igual ao comprimento (número de elementos) da lista empresas
    if 1 <= indice <= len(empresas):  
        # Obtém a empresa correspondente ao índice informado
        empresa = empresas[indice - 1] 

        # Solicita ao usuário o novo nome e CNPJ para a empresa
        print(indice)
        novo_nome = input('Digite o novo nome da empresa: ')
        novo_cnpj = input('Digite o novo CNPJ da empresa (apenas números):')
        
        # Atualiza as informações da empresa com os novos valores
        empresa['nome'] = novo_nome # -> Acessa o valor associado à chave 'nome' e muda
        empresa['cnpj'] = novo_cnpj # -> Acessa o valor associado à chave 'cnpj' e muda

        # Informa ao usuário que os dados foram atualizados com sucesso
        print('Dados da empresa {} foram atualizados com sucesso.'.format(novo_nome))
    else:
        # Caso o indice seja inválido, informa ao usuário
        print('Índice inválido!')

def mostrar_empresas():

    # Verifica se a lista não está vazia
    if empresas:
        # Itera sobre a lista de EMPRESAS usando 'enumerete' e começa do indice 1 pois foi fornecido o start=1. (Iterar é percorrer os elementos de uma sequencia)
        for i, empresa in enumerate(empresas, start=1):
            print(f'{i}. Nome: {empresa["nome"]}\n   CNPJ: {empresa["cnpj"]}')
    else:
        print('Nenhuma empresa cadastrada.')

def excluir_empresa():

    mostrar_empresas()

    indice = int(input('Digite o índice da empresa que você quer excluir: '))

    if 1 <= indice <= len(empresas):
            
            # O código acessa a lista (empresas) no índice correspondente (indice - 1) e obtém o valor associado à chave 'nome'. Esse valor (o nome da empresa) é armazenado na variável empresa_excluida.
            empresa_excluida = empresas[indice - 1]['nome']
            del empresas[indice - 1]

            print('A empresa {} foi excluída com sucesso!'.format(empresa_excluida))
    else:
        print('Índice inválido. Nenhuma empresa foi excluída.')

def fazer_backup():
    # Verifica se há empresas para fazer backup
    try:
        if empresas:

            # Solicita ao usuário o nome do arquivo de backup (exemplo: backup.json)
            nome_arquivo = input('Digite o nome do arquivo de backup: ')

            # Adiciona a extensão .json se o usuário não a incluiu
            if not nome_arquivo.endswith('.json'):
                nome_arquivo += '.json'
            
            # Abre o arquivo em modo de escrita (w) e escreve os dados no arquivo
            with open(nome_arquivo, 'w') as arquivo_backup: # Esta linha faz uso do gerenciador de contexto with para abrir um arquivo em modo de escrita ('w'), e depois utiliza a função json.dump() para escrever o conteúdo da lista empresas nesse arquivo.
                json.dump(empresas, arquivo_backup) # Essa linha de código está escrevendo o conteúdo da lista empresas em um arquivo especificado pelo usuário em formato JSON. Esse arquivo JSON pode ser posteriormente lido e utilizado para recuperar os dados da lista empresas em uma execução futura do programa.

            print('Backup realizado com sucesso no arquivo {}!'.format(nome_arquivo))
        else:
            print('Não há empresas para fazer backup.')
    except Exception as e:
        print('Ocorreu um erro durante o backup: {}'.format(e))

def sair():
    print('Saindo...')
    sleep(1.2)
    print('Volte Sempre!')
    return False