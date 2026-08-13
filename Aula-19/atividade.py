


import sqlite3
import tkinter as tk




# conectar ao banco de agencia (se o banco não existir, ele será criado)
c =  sqlite3.connect('nome.db')

# conectar ao banco de agencia (se o banco não existir, ele será criado)
cs = c.cursor()

# criando a  tabela chamada clientes
cs.execute('''CREATE TABLE IF NOT EXISTS agencia(
           
           nome TEXT,
           idade INTEGER,
           email TEXT NOT NULL,
           endereco TEXT NOT NULL,
           trabalho TEXT NOT NULL
           
           )''')

# salva comando
c.commit()

#recebe npme e idade
nome = input('Nome: ')
idade =  int(input('Idade:  '))
email = input('email: ')
endereco =  input('endereco:  ')
trabalho =  input('trabalho:  ')


cs.execute('INSERT INTO agencia values(?,?,?,?,?)', (nome, idade, email, endereco, trabalho))


nome = input('Nome: ')
idade =  int(input('Idade:  '))
email = input('email: ')
endereco =  input('endereco:  ')
trabalho =  input('trabalho:  ')


cs.execute('INSERT INTO agencia values(?,?,?,?,?)', (nome, idade,  email, endereco, trabalho))


nome = input('Nome: ')
idade =  int(input('Idade:  '))
email = input('email: ')
endereco =  input('endereco:  ')
trabalho =  input('trabalho:  ')


cs.execute('INSERT INTO agencia values(?,?,?,?,?)', (nome, idade,  email, endereco, trabalho))
c.commit()



cs.execute('SELECT * FROM agencia')
agencia =  cs.fetchall()






for d in agencia:
    print('nome:', d[0], 'idade:', d[1])


