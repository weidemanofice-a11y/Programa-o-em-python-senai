

#  Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.

# def atividade_5():
#     n  =  int(input('Numero: '))
#     l = []
#     for x  in range(2,n,2):
#         l.append(x)
#     s  =  sum(l)
#     print(l)
#     return s    


# def atividade_5():
#     n  =  int(input('Numero: '))
#     l = 0
#     for x  in range(2,n,2):
#         l  =  l + x
    
#     return l    


# Criar um arquivo  "with"
#Exercício 1: Criar e ler um Arquivo
import os

with open('weideman', 'w') as weideman:
    os.mkdir('weideman')

# import os

# # Criar um arquivo  "with"
# with open('novo_diretorio', 'w') as novo_arquivo:
#     os.mkdir('novo_arquivo')
    
# # Um arquivo é criado e automaticamente fechado após 
# # sair do bloco "with"



# with open('exemplo.txt', 'r') as arquivo:
#     conteúdo = arquivo.read()
#     print(conteúdo)





# **Exemplo 2: Cria um Diretório**


#  Exemplo 1: Criar um novo Arquivo


# import os
# with os.scandir('c:/Users/aluno/Desktop/aula12/') as entrada:
#       for arquivo in entrada:
#          print(f'Diretório encontrado: {arquivo.name}')


# # **Exercício 3: Renomear um Diretório**

# os.rename('arquivo.txt', 'novo_nome.txt')



# MANIPULANDO O DIRETÓRIO
# Exemplo 1: Criar um novo Arquivo


# import os
# with os.scandir('c:/Users/aluno/Desktop/aula12/') as entrada:
#       for arquivo in entrada:
#          print(f'Diretório encontrado: {arquivo.name}')



# # **Exercício 4:  Listar Arquivos em um Diretório** 

# import os
#  with os.scandir('C:/caminho da pasta(barra ao contrário)') as entrada:
#     for arquivo in entrada:
#          if arquivo.is_file():
#              print(f'Arquivo encontrado: {arquivo.name}')



# with os.scandir('C:/Users/aluno/Downloads/teste') as entrada :
#        for n in entrada: 
#            if 'teste.txt':
#                with open('C:/Users/aluno/Downloads/teste/teste.txt', 'r')  as t:
#                     content = t.read()

# print(content) # fora do with, caso contrário ele irá se comportar
# # como o loop    


# **Exercício 5:  Copiar Arquivos em um Diretório**

import shutil
shutil.copytree('original', 'nome da copia')
# serve para pastas -> diretórios




# **Exercício 6:  Remover**


import shutil
shutil.rmtree('c:/Users/aluno/Desktop/aula12/')


Exemplo 5: Listar Arquivos em um Diretório
import os
with os.scandir('meu_diretorio') as entrada:
    for arquivo in entrada:
        if arquivo.is_file():
            print(f'Arquivo encontrado: {arquivo.name}')
