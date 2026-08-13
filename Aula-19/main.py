



import sqlite3
import tkinter as tk




# conectar ao banco de dados (se o banco não existir, ele será criado)
c =  sqlite3.connect('nome.db')

# conectar ao banco de dados (se o banco não existir, ele será criado)
cs = c.cursor()

# criando a  tabela chamada clientes
cs.execute('''CREATE TABLE IF NOT EXISTS dados(
           
           nome TEXT,
           idade INTEGER           
           
           )''')

# salva comando
c.commit()

#recebe npme e idade
nome = input('Nome: ')
idade =  int(input('Idade:  '))


cs.execute('INSERT INTO dados values(?,?)', (nome, idade))


nome = input('Nome: ')
idade =  int(input('Idade:  '))


cs.execute('INSERT INTO dados values(?,?)', (nome, idade))


nome = input('Nome: ')
idade =  int(input('Idade:  '))


cs.execute('INSERT INTO dados values(?,?)', (nome, idade))
c.commit()



cs.execute('SELECT * FROM dados')
dados =  cs.fetchall()






for d in dados:
    print('nome:', d[0], 'idade:', d[1])


