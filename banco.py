#!/usr/bin/env python2

import sqlite3

bancoconect = sqlite3.connect('cartao.db')
command = bancoconect.cursor()

#Inseri Pessoas no banco de dados
def cadPessoa(nome, sobrenome, d_nasc, cpf):
    command.execute("Insert into Pessoa values(null, '%s', '%s', '%s', '%s');" % (nome, sobrenome, d_nasc, cpf))
    bancoconect.commit()

#Lista Pessoas cadastradas
def listarPessoa():
    command.execute("Select * from Pessoa;")
    dados = command.fetchone()
    return dados

#Inseri Cartoes do banco de dados
def cadCartao(nome, id_titular, numero, d_validade, c_verificacao):
    command.execute("insert into cartao values(null, %s, '%s', %s, '%s', %s);" % (id_titular, nome, numero, d_validade, c_verificacao))
    bancoconect.commit()

#Selecionar pessoa especifica
def selectPessoa(op):
    command.execute("select id_titular, nome, cpf from Pessoa where id_titular=%s;" % (int(op)))
    dados = command.fetchone()
    return dados

#Deletar pessoa do banco
def deletePessoa(op):
    command.execute("delete from Pessoa where id_titular=%s;" % (op))
    bancoconect.commit()

#Lista de cartao com o titular do mesmo 'lP = Listar Pessoa'
def lPCartao():
    command.execute("select Cartao.id_cartao, Pessoa.nome, Pessoa.cpf, Cartao.numero, Cartao.d_vencimento from Cartao inner join Pessoa on i_titular = id_titular;")
    dados = command.fetchone()
    return dados

#Selecionar cartao especifico
def selectCartao(op):
    command.execute("select id_cartao, nome_cartao, numero from Cartao where id_cartao=%s;" % (str(op)))
    dados = command.fetchone()
    return dados

#Deletar cartao do banco
def deleteCartao(op):
    command.execute("delete from Cartao where id_cartao=%s;" % (op))
    bancoconect.commit()