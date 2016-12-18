#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3
import os, platform
''' 
	Cria as tabelas do banco de dados do Banco Pythonico
'''
class bank_data():
    def bank_connect():
        conn = sqlite3.connect('bankydata.db')
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE clientes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            cliente_nome TEXT NOT NULL,
            email TEXT NOT NULL,
            criado_em DATE NOT NULL
        );
        """)
        cursor.execute("""
        CREATE TABLE contas (
        	id INTEGER PRIMARY KEY AUTOINCREMENT,
        	numero_conta INTEGER,
        	clientes_id INTEGER,
        	FOREIGN KEY(clientes_id) REFERENCES clientes(id)
        );
        """)
        cursor.execute("""
        CREATE TABLE ops (
        	id INTEGER PRIMARY KEY AUTOINCREMENT,
        	clientes_id INTEGER,
        	contas_id INTEGER,
        	operation TEXT NOT NULL,
        	valor REAL,
        	FOREIGN KEY(clientes_id) REFERENCES clientes(id),
        	FOREIGN KEY(contas_id) REFERENCES contas(id)
        );
        """)
        conn.close()
        print("Tabelas criadas!")

def tela_inicial():
    if platform.system()=='Linux':
        os.system("clear")
    print("Banco Pythonico 0.1!")
    print("Digite seu primeiro nome:")
    cliente = input()
    return cliente.upper()
class operacao_banky():
    def escolher_ops(chamado):
        os.system("clear")
        print("----Banco Py do %s----" % (chamado))
        ops_list = ['Saque','Saldo', 'Extrato', 'Depósito', 'Transferência', 'Sair']
        charesc = ['G', 'S', 'E', 'D', 'T', 'X']
        print("Escolha Operação: ")
        for opesc in range(0,len(ops_list)):
            print("%s - Para %s" % (charesc[opesc],ops_list[opesc]))
        print("----------------------------")
        print("Commando:")
        while True:
            ops_escol = input().upper()
            if ops_escol in charesc:
                print("%s selecionado!" % (ops_escol))
            else:
                print("Não identifiquei sua escolha,")
                print("Tente de novo.")
            if ops_escol=='X':
                print("Até logo!")
                exit()
    # def saque():

    # def saldo():

    # def extrato():

    # def deposito():

    # def transferencia():

# bank_data.bank_connect()
chamado = tela_inicial()
print("Bem vindo, %s!" %(chamado))
operacao_banky.escolher_ops(chamado)
