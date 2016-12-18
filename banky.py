#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3
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
    print("Banco Pythonico 1.0")
    print("Digite seu primeiro nome:",end=" ")
    cliente = input()
    return cliente.upper()
# class operacao_banky():
#     def saldo():


#     def extrato():


#     def deposito():


#     def transferencia():

# bank_data.bank_connect()
chamado = tela_inicial()
print("Bem vindo, %s!" %(chamado))
