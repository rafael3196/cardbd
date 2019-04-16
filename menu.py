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
    op = raw_input()
    if op == "1":
        consultar()
    elif op == "2":
        cadastrar()
    elif op == "3":
        remover()
    elif op == "4":
        sair()
    else:
        print "+++ Insira uma opcao valida +++"
        time.sleep(5)
        m_principal()

def consultar():
    clear()
    print "    MENU PARA EFETUAR CONSULTAS    "
    print "Numero -   Opcao"
    print ""
    print "   1   -   Consultar Pessoas"
    print "   2   -   Consultar Cartoes"
    print "   3   -   Voltar"
    op = raw_input()
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
    elif op == "3":
        print "Retornando ao Menu principal..."
        time.sleep(3)
        m_principal()
    else:
        print "Opcao Invalida..."
        time.sleep(2)
        consultar()

def cadastrar():
    clear()
    print "    MENU PARA CADASTROS    "
    print "Selecione uma das opcoes abaixo:"
    print "Numero -    Opcao"
    print ""
    print "   1   -    Cadastrar Pessoa"
    print "   2   -    Cadastrar Cartao"
    print "   3   -    Voltar"
    op = raw_input()
    if op == "1":
        cad_pessoa()
    elif op == "2":
        cad_cartao()
    elif op == "3":
        m_principal()
    else:
        print "+++ Insira uma opcao valida +++"
        time.sleep(5)
        cadastrar()

def remover():
    print "MENU PARA DELETAR DE DADOS"
    print "Numero -   Opcao"
    print ""
    print "   1   -   Deletar Pessoas"
    print "   2   -   Deletar Cartoes"
    print "   3   -   Voltar"
    op = raw_input()
    if op == "1":
        print "Pessoas a serem DELETADAS"
        print "ID --- Nome Completo --- D.Nascimento --- CPF"
        banco.command.execute("select * from pessoa;")
        dados = banco.command.fetchone()
        while dados is not None:
            print str(dados[0])+"      "+dados[1]+" "+dados[2]+"    "+dados[3]+"    "+dados[4]
            dados = banco.command.fetchone()
        op = raw_input("Insira o ID da pessoa que deseja deletar: ")
        banco.command.execute("select id_titular, nome, cpf from Pessoa where id_titular=%s;" % (int(op)))
        dados = banco.command.fetchone()
        clear()
        print "Deseja DELETAR a seguinte pessoa(S/N): "
        print "ID: "+str(dados[0])
        print "Nome: "+dados[1]
        print "CPF: "+dados[2]
        op = raw_input()
        if op == "S":
            print "Apos executado sera impossivel restaurar os dados dessa pessoa"
            print "Deseja realmente prosseguir?(SIM/NAO)"
            op = raw_input()
            if op == "SIM":
                try:
                    banco.command.execute("delete from Pessoa where id_titular=%s;" % (dados[0]))
                    banco.bancoconect.commit()
                    print "Dados deletados com sucesso!"
                    time.sleep(2)
                    m_principal()
                except:
                    print "Ocorreu um erro"
            elif op == "NAO":
                print "Retornando ao Menu principal: "
                time.sleep(3)
                clear()
                m_principal()
            else:
                print "Opcao invalida"
                time.sleep(2)
                clear()
                m_principal()
        elif op == "N":
            print "Retornando ao inicio..."
            time.sleep(3)
            m_principal()
        else:
            print "Opcao Invalida!"
            time.sleep(2)
            m_principal()
    elif op == "2":
        print "Cartoes a serem DELETADOS"
        print "ID --- Titular --- Cartao --- Vencimento"
        banco.command.execute("select Cartao.id_cartao, Pessoa.nome, Pessoa.cpf, Cartao.numero, Cartao.d_vencimento from Cartao inner join Pessoa on i_titular = id_titular;")
        dados = banco.command.fetchone()
        while dados is not None:
            print str(dados[0])+"    "+dados[1]+"   "+dados[2]+"   "+str(dados[3])+"   "+dados[4]
            dados = banco.command.fetchone()
        op = raw_input("Insira o ID do cartao que deseja deletar: ")
        banco.command.execute("select id_cartao, nome_cartao, numero from Cartao where id_cartao=%s;" % (str(op)))
        dados = banco.command.fetchone()
        clear()
        print "Deseja DELETAR o seguinte cartao(S/N): "
        print "ID: "+str(dados[0])
        print "Nome: "+dados[1]
        print "Numero: "+str(dados[2])
        op = raw_input()
        if op == "S":
            print "Apos executado sera impossivel restaurar os dados do cartao"
            print "OBS: E necessario deletar o titular antes de deletar o cartao do mesmo"
            print "Deseja realmente prosseguir?(SIM/NAO)"
            op = raw_input()
            if op == "SIM":
                try:
                    banco.command.execute("delete from Cartao where id_cartao=%s;" % (dados[0]))
                    banco.bancoconect.commit()
                    print "Cartao deletado com sucesso!"
                    time.sleep(2)
                    m_principal()
                except NameError:
                    print "Ocorreu um Erro"
            elif op == "NAO":
                print "Retornando ao inicio..."
                time.sleep(2)
                m_principal()
            else:
                print "Opcao invalida!"
                m_principal()
        elif op == "N":
            print "Retornando ao inicio..."
            time.sleep(2)
            m_principal()
        else:
            print "Retornando ao inicio..."
            time.sleep(2)
            m_principal()
    elif op == "3":
        m_principal()
    else:
        print "Opcao invalida!"
        time.sleep(2)
        m_principal()

def sair():
    op = raw_input("Deseja realmente sair?(S/N)")
    if op == "S":
        print "Finalizando programa..."
        time.sleep(4)
        exit()
    elif op =="N":
        m_principal()
    else:
        print "Opcao Invalida!"
        time.sleep(2)
        m_principal()

#Entrada e Saida de dados:
def cad_pessoa():
    print "   CADASTRO DE PESSOAS   "
    print "Deseja Iniciar o cadastro de pessoa? (S/N)"
    op = raw_input()
    #Confirmando se o usuario realmente quer efetuar um cadastro
    if op == "S":
        nome = raw_input("Insira o primeiro nome: ")
        sobrenome = raw_input("Insira o sobrenome: ")
        d_nasc = raw_input("Insira a data de Nascimento: ")
        cpf = raw_input("Insira o CPF: ")
        clear()
        print "Deseja confirmar o cadastro com as seguintes informacoes?(S/N)"
        print nome + " " + sobrenome
        print "Data de Nascimento: " + d_nasc
        print "CPF: " + cpf
        op = raw_input()
        # Confirmando dados antes de o cadastro ser efeutado
        if op == "S":
            pessoa = Pessoa(nome, sobrenome, d_nasc, cpf)
            try:
                banco.command.execute("Insert into Pessoa values(null, '%s', '%s', '%s', '%s');" % (pessoa.nome, pessoa.sobrenome, pessoa.d_nasc, pessoa.cpf))
                banco.bancoconect.commit()
            except NameError:
                print "erro " + NameError
            print "---Cadastro efetuado com sucesso---"
            print "Deseja efetuar outro cadastro?(S/N)"
            op = raw_input()
            if op == "S":
                clear()
                cad_pessoa()
            elif op == "N":
                clear()
                m_principal()
            else:
                print "+++Opcao Invalida, retornando ao menu principal...+++"
                time.sleep(5)
                m_principal()
        elif op == "N":
            print "Cadastro cancelado, retornando ao inicio"
            time.sleep(3)
            clear()
            m_principal()
        else:
            print "+++ Opcao Invalida, retornando ao menu principal...+++"
            time.sleep(5)
            m_principal()
    elif op == "N":
        print "Retornando ao menu principal..."
        time.sleep(5)
        clear()
        m_principal()

def cad_cartao():
    print "   CADASTRO DE CARTOES   "
    print "Deseja Iniciar o cadastro de um cartao? (S/N)"
    op = raw_input()
    # Confirmando se o usuario realmente quer efetuar um cadastro
    if op == "S":
        nome = raw_input("Insira o nome de identificacao para o cartao: ")
        numero = raw_input("Insira o numero do cartao (somente numero): ")
        d_validade = raw_input("Insira o vencimento do cartao (MM/YYYY): ")
        c_verificacao = raw_input("Insira o codigo de verificacao atras do cartao")
        clear()
        print("Deseja confirmar o cadastro com as seguintes informacoes?(S/N)")
        print "Nome do cartao: " + nome
        print "Numero do cartao: " + numero[0:4] + " " + numero[4:8] + " " + numero[8:12] + " " + numero[12:16]
        print "Validade (MM/YYYY)" + d_validade
        print "Codigo Verificador: " + c_verificacao
        op = raw_input()
        #Confirmando os dados do cartao
        if op == "S":
            #exibindo dados para linkar com a pessoa
            print "Selecione uma pessoa para atribuir o cartao"
            banco.command.execute("Select * from Pessoa;")
            dados = banco.command.fetchone()
            print "ID ---- Nome ---- CPF"
            while dados is not None:
                print str(dados[0])+"       "+dados[1]+"     "+dados[4]
                dados = banco.command.fetchone()
            id = raw_input("Insira o ID para ser linkado: ")
        elif op == "N":
            print "Retornando ao cadastro de cartoes..."
            time.sleep(3)
            clear()
            cad_cartao()
        else:
            print "Opcao invalida, retornando ao inicio..."
            time.sleep(3)
            m_principal()
        cartao = Cartao(nome, id, numero, d_validade, c_verificacao)
        banco.command.execute("insert into cartao values(null, %s, '%s', %s, '%s', %s);" % (cartao.id_titular, cartao.nome, cartao.numero, cartao.d_validade, cartao.c_verificacao))
        banco.bancoconect.commit()
        print "Cartao cadastrado com sucesso..."
        time.sleep(3)
        m_principal()











