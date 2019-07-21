import os
import time
import banco
from pessoa import Pessoa
from cartao import Cartao
clear = lambda: os.system("clear")

#Menus de Principais:
def m_principal():
    clear()
    print "    MENU PRINCIPAL    "
    print "Bem Vindo sistema de cartao de credito"
    print "Selecione uma das opcoes abaixo:"
    print "Numero -   Opcao"
    print ""
    print "   1   -   Consultar"
    print "   2   -   Cadastrar"
    print "   3   -   Remover"
    print "   4   -   SAIR"
    op = raw_input("Numero(1/2/3/4): ")
    while (op != "1") and (op != "2") and (op != "3") and (op != "4"):
        print "Opcao Invalida!!!"
        op = raw_input("Numero(1/2/3/4): ")
    if op == "1":
        consultar()
    elif op == "2":
        cadastrar()
    elif op == "3":
        remover()
    else:
        sair()

def consultar():
    clear()
    print "    MENU PARA EFETUAR CONSULTAS    "
    print "Numero -   Opcao"
    print ""
    print "   1   -   Consultar Pessoas"
    print "   2   -   Consultar Cartoes"
    print "   3   -   Voltar"
    op = raw_input("Numero(1/2/3): ")
    while (op != "1") and (op != "2") and (op != "3"):
        print("Opcao Invalida!!!")
        op = raw_input("Numero(1/2/3): ")
    if op == "1":
        clear()
        print "Pessoas Cadastradas"
        print "ID --- Nome                --- D. Nascimento --- CPF"
        banco.command.execute("select * from Pessoa;")
        dados = banco.command.fetchone()
        while dados is not None:
            print str(dados[0])+"      "+dados[1]+" "+dados[2]+"   "+dados[3]+"    "+dados[4]
            dados = banco.command.fetchone()
        print "Pressione Enter para continuar..."
        op = raw_input()
        consultar()
    elif op == "2":
        clear()
        print "Cartoes Cadastrados"
        print "ID --- Nome   --- Proprietario --- N. Cartao"
        banco.command.execute("select Cartao.id_cartao, Cartao.nome_cartao, Pessoa.nome, Cartao.numero from Cartao inner join Pessoa on i_titular = id_titular;")
        dados = banco.command.fetchone()
        while dados is not None:
            print str(dados[0])+"     "+dados[1]+"     "+dados[2]+"     "+str(dados[3])
            dados = banco.command.fetchone()
        print "Pressione Enter para continuar..."
        op = raw_input()
        consultar()
    else:
        m_principal()

def cadastrar():
    clear()
    print "    MENU PARA CADASTROS    "
    print "Selecione uma das opcoes abaixo:"
    print "Numero -    Opcao"
    print ""
    print "   1   -    Cadastrar Pessoa"
    print "   2   -    Cadastrar Cartao"
    print "   3   -    Voltar"
    op = raw_input("Numero(1/2/3): ")
    while (op != "1") and (op != "2") and (op != "3"):
        print("Opcao Invalida!!!")
        op = raw_input("Numero(1/2/3): ")
    if op == "1":
        cad_pessoa()
    elif op == "2":
        cad_cartao()
    else:
        m_principal()

def remover():
    clear()
    print "MENU PARA DELETAR DE DADOS"
    print "Numero -   Opcao"
    print ""
    print "   1   -   Deletar Pessoas"
    print "   2   -   Deletar Cartoes"
    print "   3   -   Voltar"
    op = raw_input("Numero(1/2/3): ")
    while (op != "1") and (op != "2") and (op != "3"):
        print("Opcao Invalida!!!")
        op = raw_input("Numero(1/2/3): ")
    if op == "1":
        remove_pessoa()
    elif op == "2":
        remove_cartao()
    else:
        m_principal()

def sair():
    op = raw_input("Deseja realmente sair?(S/N): ")
    while (op != "s") and (op != "S") and (op != "n") and (op != "N"):
        print("Opcao Invalida!!!")
        op = raw_input("Somente 'S' ou 'N': ")
    if (op == "s") or (op == "S"):
        print "Finalizando Programa..."
        time.sleep(3)
        exit()
    else:
        m_principal()

#Entrada e Saida de dados:
def cad_pessoa():
    clear()
    print "   CADASTRO DE PESSOAS   "
    op = raw_input("Deseja Iniciar o cadastro de pessoa? (S/N): ")
    #Confirmando se o usuario realmente quer efetuar um cadastro
    while (op != "s") and (op != "S") and (op != "n") and (op != "N"):
        print "Opcao Invalida!!!"
        op = raw_input("Somente 'S' ou 'N': ")
    if (op == "S") or (op == "s"):
        nome = raw_input("Insira o primeiro nome: ")
        sobrenome = raw_input("Insira o sobrenome: ")
        d_nasc = raw_input("Insira a data de Nascimento: ")
        cpf = raw_input("Insira o CPF: ")
        clear()
        print nome + " " + sobrenome
        print "Data de Nascimento: " + d_nasc
        print "CPF: " + cpf
        op = raw_input("Deseja confirmar o cadastro com as seguintes informacoes?(S/N): ")
        # Confirmando dados antes de o cadastro ser efeutado
        while (op != "s") and (op != "S") and (op != "n") and (op != "N"):
            print "Opcao Invalida!!!"
            op = raw_input("Somente 'S' ou 'N': ")
        if (op == "S") or (op == "s"):
            pessoa = Pessoa(nome, sobrenome, d_nasc, cpf)
            try:
                banco.cadPessoa(pessoa.nome, pessoa.sobrenome, pessoa.d_nasc, pessoa.cpf)
            except NameError:
                print "erro " + NameError
            print "---Cadastro efetuado com sucesso---"
            op = raw_input("Deseja efetuar outro cadastro?(S/N): ")
            while (op != "s") and (op != "S") and (op != "n") and (op != "N"):
                print "Opcao Invalida!!!"
                op = raw_input("Somente 'S' ou 'N': ")
            if (op == "S") or (op == "s"):
                clear()
                cad_pessoa()
            else:
                clear()
                m_principal()
        else:
            print "Cadastro cancelado, retornando ao inicio..."
            time.sleep(2)
            m_principal()
    else:
        print "Retornando ao menu principal..."
        time.sleep(2)
        m_principal()

def cad_cartao():
    clear()
    print "   CADASTRO DE CARTOES   "
    # Confirmando se o usuario realmente quer efetuar um cadastro
    op = raw_input("Deseja Iniciar o cadastro de um cartao? (S/N): ")
    while (op != "s") and (op != "S") and (op != "n") and (op != "N"):
        print "Opcao Invalida!!!"
        op = raw_input("Somente 'S' ou 'N': ")
    if (op == "S") or (op == "s"):
        nome = raw_input("Insira o nome de identificacao para o cartao: ")
        numero = raw_input("Insira o numero do cartao (somente numero): ")
        d_validade = raw_input("Insira o vencimento do cartao (MM/YYYY): ")
        c_verificacao = raw_input("Insira o codigo de verificacao atras do cartao: ")
        clear()
        print "Nome do cartao: " + nome
        print "Numero do cartao: " + numero[0:4] + " " + numero[4:8] + " " + numero[8:12] + " " + numero[12:16]
        print "Validade (MM/YYYY)" + d_validade
        print "Codigo Verificador: " + c_verificacao
        op = raw_input("Deseja confirmar o cadastro com as seguintes informacoes?(S/N): ")
        #Confirmando os dados do cartao
        while (op != "s") and (op != "S") and (op != "n") and (op != "N"):
            print "Opcao Invalida!!!"
            op = raw_input("Somente 'S' ou 'N': ")
        if (op == "S") or (op == "s"):
            #exibindo dados para linkar com a pessoa
            print "Selecione uma pessoa para atribuir o cartao"
            dados = banco.listarPessoa() #Select em 'Pessoa'
            print "ID ---- Nome ---- CPF"
            while dados is not None:
                print str(dados[0])+"       "+dados[1]+"     "+dados[4]
                dados = banco.command.fetchone()
            id_titular = raw_input("Insira o ID para ser linkado: ")
        else:
            print "Retornando ao Cadastro de Cartoes..."
            time.sleep(2)
            clear()
            cad_cartao()
        cartao = Cartao(nome, id_titular, numero, d_validade, c_verificacao)
        banco.cadCartao(cartao.nome, cartao.id_titular, cartao.numero, cartao.d_validade, cartao.c_verificacao)
        print "Cartao cadastrado com sucesso..."
        time.sleep(3)
        m_principal()

def remove_pessoa():
    print "Pessoas a serem DELETADAS"
    print "ID --- Nome Completo --- D.Nascimento --- CPF"
    dados = banco.listarPessoa()
    while dados is not None:
        print str(dados[0])+"      "+dados[1]+" "+dados[2]+"    "+dados[3]+"    "+dados[4]
        dados = banco.command.fetchone()
    op = raw_input("Insira o ID da pessoa que deseja deletar: ")
    dados = banco.selectPessoa(op)
    clear()
    print "ID: "+str(dados[0])
    print "Nome: "+dados[1]
    print "CPF: "+dados[2]
    op = raw_input("Deseja DELETAR a seguinte pessoa(S/N): ")
    while (op != "S") and (op != "s") and (op != "N") and (op != "n"):
        print "Opcao Invalida!!!"
        op = raw_input("Somente 'S' ou 'N': ")
    if op == "S" or op == "s":
        print "Apos executado sera impossivel restaurar os dados dessa pessoa"
        op = raw_input("Deseja realmente prosseguir?(SIM/NAO): ")
        while (op != "SIM") and (op != "NAO"):
            print "Opcao Invalida!!!"
            op = raw_input("Somente 'SIM' ou 'NAO': ")
        if op == "SIM":
            try:
                banco.deletePessoa(dados[0])
                print "Dados deletados com sucesso!"
                time.sleep(2)
                m_principal()
            except:
                print "Ocorreu um erro"
        else:
            print "Retornando ao Menu Principal..."
            time.sleep(3)
            m_principal()
    else:
        print "Retornando ao Menu Principal..."
        time.sleep(3)
        m_principal()

def remove_cartao():
    print "Cartoes a serem DELETADOS"
    print "ID --- Titular --- Cartao --- Vencimento"
    dados = banco.lPCartao()
    while dados is not None:
        print str(dados[0])+"    "+dados[1]+"   "+dados[2]+"   "+str(dados[3])+"   "+dados[4]
        dados = banco.command.fetchone()
    op = raw_input("Insira o ID do cartao que deseja deletar: ")
    dados = banco.selectCartao(op)
    clear()
    print "ID: "+str(dados[0])
    print "Nome: "+dados[1]
    print "Numero: "+str(dados[2])
    op = raw_input("Deseja DELETAR o seguinte cartao(S/N): ")
    while (op != "S") and (op != "s") and (op != "N") and (op != "n"):
        print "Opcao Invalida!!!"
        op = raw_input("Somente 'S' ou 'N': ")
    if op == "S" or op == "s": #menu-remover-cartao-firstconfirmation
        print "Apos executado sera impossivel restaurar os dados do cartao"
        op = raw_input("Deseja realmente prosseguir?(SIM/NAO): ")
        while (op != "SIM") and (op != "NAO"):
            print "Opcao Invalida!!!"
            op = raw_input("Somente 'SIM' ou 'NAO': ")
        if op == "SIM":
            try:
                banco.deleteCartao(dados[0])
                print "Cartao deletado com sucesso!"
                time.sleep(2)
                m_principal()
            except NameError:
                print "Ocorreu um Erro"
        else:
            print "Retornando ao inicio..."
            time.sleep(2)
            m_principal()
    else:
        print "Retornando ao inicio..."
        time.sleep(2)
        m_principal()