


# import streamlit as st

# # st.title('Isso é um titulo')
# # st.header('Teste')   


# #==================================================


# # import streamlit as st



# # st.title('CALCULADORA')
# # # st.header('teste')


# # n1 =  st.number_input('nº', value=0.1 )
# # n2 =  st.number_input('nº', value=0.0)


# # if st.button('Calcular...') :   
# #    if n1 and n2:
# #       soma  =  n1 + n2


# #       st.info( soma)
# #    else:
# #       print('Digite algo ')  
# # 
# # +++++++++++++++++++++++++++++++++++++++++++++++
# # 
# import streamlit as st
# import pandas as pd



# # st.title('CALCULADORA')
# # st.header('teste')


# # dados  =  pd.read_csv('dados.csv')


# # df = pd.DataFrame(dados)


# # st.dataframe(df)


# # st.bar_chart(df, x = 'nome', y = 'nota')


# # n1 =  st.number_input('nº' )
# # n2 =  st.number_input('nº', value=0.0)


# # if st.button('Calcular...') :   
# #    if n1 and n2:
# #       soma  =  n1 + n2


# #       st.info( soma)
# #    else:
# #       print('Digite algo ')      



# import streamlit as st
# import pandas as pd
# import sqlite3




# def conecao():
#     conn =  sqlite3.connect('banco')
#     return conn


# nome = st.text_input('nome: ')
# email = st.text_input('E-mail: ')


# def tabela():
#     con = conecao()
#     c =  con.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS dados(
                
#                 nome TEXT,
#                 email TEXT
                
#                 )''')


#     con.commit()
#     nome_ = nome
#     email_ = email
    
#     if st.button('Adicionar dados'):
#         if nome_ and email_:
#             con = conecao()
#             c  =  con.cursor()
            
#             c.execute('INSERT INTO dados values(?,?)',(nome_, email_))  


#             st.info('DADOS INSERIDOS COM SUCESSO! ')
#             con.commit()
#     if st.button('mostrar dados salvos') :       
#        c.execute('SELECT * FROM dados')
#        dados  =  c.fetchall()
#        st.write(dados) 
#        st.map()


# tabela()




# # inserir()
   


# # st.title('CALCULADORA')
# # st.header('teste')


# dados  =  pd.read_csv('dados.csv')


# df = pd.DataFrame(dados)


# st.dataframe(df)


# st.bar_chart(df, x = 'nome', y = 'nota')


# n1 =  st.number_input('nº' )
# n2 =  st.number_input('nº', value=0.0)





# if st.button('Calcular...') :   
#    if n1 and n2:
#       soma  =  n1 + n2


#       st.info( soma)
#    else:
#       print('Digite algo ')    





import streamlit as st
import pandas as pd
import sqlite3

def conecao():
    conn =  sqlite3.connect('banco')
    return conn

nome = st.text_input('nome: ')
cpf = st.number_input('Diite o numero do CPF CORRETAMENTE: ')
tel = st.number_input('Digite o numero telefone: ', value == 99999999999)
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




