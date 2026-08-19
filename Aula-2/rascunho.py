import sqlite3 # banco de dados
import tkinter as tk # interface 
from tkinter import messagebox # caixas de mensagens
from tkinter import ttk # interface grafica tb

def conectar():
    return sqlite3.connect('teste.db')


def criar_tabela():
    conn = conectar()
    c= conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS dados(
                nome TEXT,
                cpf NUMBER,
                tel NUMBER,
                endereco TEXT,
                telcont TEXT,
                procedi TEXT              
        )       
    ''')
    conn.commit()
    conn.close()
  


# CREATE
def inserir_usuario():
    nome = entry_nome.get()
    cpf =  entry_cpf.get()
    tel =  entry_tel.get()
    endereco = entry_endereco.get()
    telcont = entry_telcont.get()
    procedi =  entry_procedi.get()
    if  nome and cpf:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO usuarios(id,nome, cpf, tel, endereco, telcont, procedi) VALUES(?,?,?,?,?,?,?)', (nome, cpf, tel, endereco, telcont, procedi))
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'DADOS INSERIDOS COM SUCESSO!') 
        mostrar_usuario()
    else:
        messagebox.showerror('ERRO', 'ALGO DEU ERRADO!') 

# READ
def mostrar_usuario():
    for row in tree.get_children():   
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()    
    c.execute('SELECT * FROM usuarios')
    usuarios = c.fetchall()
    for usuario in usuarios:
        tree.insert("", "end", values=(usuario[0], usuario[1],usuario[2]))
    conn.close()    


# DELETE
def delete_usuario():
    dado_del = tree.selection()
    if dado_del:
       user_id = tree.item(dado_del)['values'][0]
       conn = conectar()
       c = conn.cursor()    
       c.execute('DELETE FROM usuarios WHERE id = ? ',(user_id,))
       conn.commit()
       conn.close()
       messagebox.showinfo('', 'DADO DELETADO')
       mostrar_usuario()

    else:
       messagebox.showerror('', 'OCORREU UM ERRO')  

# UPDATE 
       
def editar():
     selecao = tree.selection()
     if selecao:
         user_id = tree.item(selecao)['values'][0]
         novo_nome = entry_nome.get()
         novo_cpf = entry_cpf.get()
         novo_tel = entry_tel.get()
         novo_endereco = entry_endereco.get()
         novo_telcont = entry_telcont.get()
         novo_procedi = entry_procedi.get()

         if novo_nome and novo_cpf:
            conn = conectar()
            c = conn.cursor()    
            c.execute('UPDATE usuarios SET nome = ? , cpf = ?, tel = ?, endereco = ?, telcont = ?, procedi = ? WHERE id = ? ',(novo_nome,novo_cpf,novo_tel,novo_endereco,novo_tel,novo_procedi,user_id))
            conn.commit()
            conn.close()  
            messagebox.showinfo('', 'DADOS ATUALIZADOS')
            mostrar_usuario()

         else:
             messagebox.showwarning('', 'PREENCHA TODOS OS CAMPOS')

     else:
            messagebox.showerror('','ALGO DEU ERRADO!')


janela = tk.Tk()
janela.title('CRUD')

label_nome = tk.Label(janela, text='Nome:')
label_nome.grid(row=0, column=0, padx=10, pady=10)

entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_CPF = tk.Label(janela, text = 'CPF:')
label_CPF.grid(row=2, column=0, padx=10, pady=10)

entry_cpf = tk.Entry(janela, text = 'CPF:')
entry_cpf.grid(row=2, column=1, padx=10, pady=10)

label_tel = tk.Label(janela, text = 'N° Telefone:')
label_tel.grid(row=1, column=0, padx=10, pady=10)

entry_tel = tk.Entry(janela, text = 'N° Telefone:')
entry_tel.grid(row=1, column=1, padx=10, pady=10)

label_endereco = tk.Label(janela, text = 'Endereço:')
label_endereco.grid(row=1, column=0, padx=10, pady=10)

entry_endereco = tk.Entry(janela, text = 'Endereço:')
entry_endereco.grid(row=1, column=1, padx=10, pady=10)

label_telcont = tk.Label(janela, text = 'Telefone de contato:')
label_telcont.grid(row=1, column=0, padx=10, pady=10)

entry_telcont = tk.Entry(janela, text = 'Telefone de contato:')
entry_telcont.grid(row=1, column=1, padx=10, pady=10)


label_procedi = tk.Label(janela, text = 'Procedimento:')
label_procedi.grid(row=1, column=0, padx=10, pady=10)

entry_procedi = tk.Entry(janela, text = 'procedimento:')
entry_procedi.grid(row=1, column=1, padx=10, pady=10)








btn_salvar = tk.Button(janela, text='Salvar', command=inserir_usuario)
btn_salvar.grid(row=3, column=0, padx=10, pady=10)

btn_deletar = tk.Button(janela, text='deletar', command=delete_usuario )
btn_deletar.grid(row=4, column=0, padx=10, pady=10)

btn_atualizar = tk.Button(janela, text='atualizar', command=editar)
btn_atualizar.grid(row=5, column=0, padx=10, pady=10)



columns = ('ID', 'NOME', 'E-MAIL')
tree = ttk.Treeview(janela, columns=columns, show='headings')
tree.grid(row=6,column=0,columnspan=2,padx=10, pady=10)


for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_usuario()


janela.mainloop()