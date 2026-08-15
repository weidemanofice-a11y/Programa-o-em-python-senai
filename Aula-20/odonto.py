

import streamlit as st
import pandas as pd
import sqlite3

def conecao():
    conn =  sqlite3.connect('banco')
    return conn

nome = st.text_input('nome: ')
cpf = st.number_input('Diite o numero do CPF CORRETAMENTE: ')
tel = st.number_input('Digite o numero telefone: ')
endereco = st.text_input('Digite o endereço: ')
telcont = st.number_input('Digite telefone para contato: ')
procedi = st.text_input('digite o procedimento: ')


def tabela():
    con = conecao()
    c =  con.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS dados(
                
                nome TEXT,
                cpf NUMBER,
                tel NUMBER,
                endereco TEXT,
                telcont TEXT,
                procedi TEXT
                                
                )''')
    con.commit()
    nome_ = nome
    cpf_ = cpf
    tel_ = tel
    endereco_ = endereco
    telcont_ = telcont
    procedi_ = procedi

    if st.button('Adicionar dados'):
        if nome_ and cpf_:
            con = conecao()
            c  =  con.cursor()
            
            c.execute('INSERT INTO dados values(?,?)',(nome_, cpf_, tel_, endereco_, telcont_, procedi_))  


            st.info('DADOS INSERIDOS COM SUCESSO! ')
            con.commit()
    if st.button('mostrar dados salvos') :       
       c.execute('SELECT * FROM dados')
       dados  =  c.fetchall()
       st.write(dados) 
       st.map()


tabela()




