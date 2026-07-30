

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferent


# l1=  int(input('Lado 1 '))
# l2=  int(input('Lado 2 '))
# l3=  int(input('Lado 3 '))



# if l1 == l2  == l3  == l1:
#     print('equilatero')
# elif l1 != l2 != l3 != l1:
#     print('escaleno')    
# else:
#     print('Iscosceles')    




# # Um triângulo é chamado de escaleno se todos os lados possuem medidas diferent


# idade =  int(input('Idade:  '))


# if idade >= 16 and idade <=17:
#     print('Pode votar')
# elif idade >= 18 and idade <= 65:
#     print('Deve votar')
# else:
#     print('Não precisa votar')   



# numero = int(input('numero>> '))


# match numero:
#     case x if x  % 2 ==0:
#         print('par')
#     case _:
#         print('impar')     


# 3: Verificando se uma string é vazia ou não



# #informacao = ('')
# informacao =  str(input('Informacao:  '))

# match informacao:
#     case x if x  == (''):
#         print('vazio')
#     case _:
#         print('preenchido')  


 #  Verificando se um número é maior, menor ou igual a 10  
 
# numero =  int(input('Digite um numero:  '))

# match numero:
#     case x if x  > 10:
#         print('Maior que 10')
#     case x if x  == 10:
#         print('numero 10')
#     case _:
#         print('Menor que 10')
 
 

 #5: Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)
 
 
# idade =  int(input('Digite um numero:  '))

# match idade:
#     case idade if idade  =< 12:
#         print('crianca')
#     case idade if idade  == 10:
#         print('numero 10')
#     case _:
#         print('Menor que 10')
     


#  Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)  



# idade =  int(input('Idade: '))


# match idade:


#     case idade if idade <= 12:
#         print('Criança')
#     case idade if idade >= 13 and idade <=17:
#         print('Adolescente')
#     case idade if idade >= 18  and idade <= 35:
#         print('Jovem')
#     case idade if idade > 35 and idade <= 65:
#         print('Adulto')
#     case _:
#         print('Idoso')            




# import random




# #escolha_pc = random.choice(opcao_pc)
# # print(escolha_pc)
    
# for chance in range(1,4):
#     opcao_pc  =  ['✂️','🪨', '🧻']
#     escolha_pc = random.choice(opcao_pc)
#     # print(escolha_pc)
#     minha_escolha = input('Escolha>>')
#     if escolha_pc == minha_escolha:
#         print('Acertou vc escolheu', minha_escolha)
#         print('A maquina escolheu ',escolha_pc)
#         break
#     else:
#         print('Errou feio, vc escolheu...', minha_escolha)
#         print('A maquina escolheu ',escolha_pc)
# else:
#     print('Chances esgotadas')            



#======================================================



# import random

# meus_pontos = 0
# pontas_maquina = 0

# # escolha_pc = random.choice(opcao_pc)
# # print(escolha_pc)
    
# add  =  [3,2,1]

# for chance in add:
#     opcao_pc  =  ['✂️', '🧻', '🪨' ]
#     escolha_pc = random.choice(opcao_pc)
#     # print(escolha_pc)
#     minha_escolha = input('Escolha>>')
#     if escolha_pc == minha_escolha:
#         print('Empate')
#         pontas_maquina = pontas_maquina + 1
#         meus_pontos = meus_pontos + 1
#         add.append(1)
#         print(add)
        
        
#     elif escolha_pc == '✂️' and minha_escolha == '🧻':
#         print('Maquina ganhou')
#         pontas_maquina = pontas_maquina + 1
#         print(add)
#     elif escolha_pc == '🧻' and minha_escolha == '🪨':
#         print('Maquina ganhou')
#         pontas_maquina = pontas_maquina + 1
#         print(add)  
#     elif escolha_pc == '🪨' and minha_escolha == '✂️':
#         print('Maquina ganhou')  
#         pontas_maquina = pontas_maquina  + 1
#         print(add)             
#     else:
#         print('Você ganhou!!!!')
#         meus_pontos =  meus_pontos + 1

# else:
   
#     if meus_pontos > pontas_maquina:
#         print('Vc é o vencedor do jogo 🏆')
#     elif  meus_pontos == pontas_maquina:
#         print('EMPATE GERAL')    
#     else:
#         print('A MÁQUINA É O VENCEDOR!! 🏆')    

#     print('Chances esgotadas')       
#     print(f'''
#              PLACAR
# ----------------------------------             
# seus pontos{meus_pontos}
# pontos da maquina {pontas_maquina} 
# ----------------------------------

# ''')     




# #===========================



# import random

# meus_pontos = 0
# pontas_maquina = 0
# add  =  [3,2,1]

# for chance in add:
#     opcao_pc  =  ['✂️','🧻', '🪨']
#     escolha_pc = random.choice(opcao_pc)
#     # print(escolha_pc)
#     minha_escolha = input('Escolha>>')
#     if escolha_pc == minha_escolha:
#         print('Empate')
#         pontas_maquina = pontas_maquina + 1
#         meus_pontos = meus_pontos + 1
#         add.append(1)
#         print('Você ainda tem ', len(add), 'chances')
        
        
#     elif escolha_pc == '✂️' and minha_escolha == '🧻':
#         print('Maquina ganhou')
#         pontas_maquina = pontas_maquina + 1
#         print('Chances', add)
#         add.pop()
#     elif escolha_pc == '🧻' and minha_escolha == '🪨':
#         print('Maquina ganhou')
#         pontas_maquina = pontas_maquina + 1
#         add.pop()
#         print('Chances',add)  
#     elif escolha_pc == '🪨' and minha_escolha == '✂️':
#         print('Maquina ganhou')  
#         pontas_maquina = pontas_maquina  + 1
#         print('Chances',add)  
#         add =  add.pop()      
#     else:
#         print('Você ganhou!!!!')
#         meus_pontos =  meus_pontos + 1
#         # add.pop()
# else:
   
#     if meus_pontos > pontas_maquina:
#         print('Vc é o vencedor do jogo 🏆')
#     elif  meus_pontos == pontas_maquina:
#         print('EMPATE GERAL')    
#     else:
#         print('A MÁQUINA É O VENCEDOR!! 🏆')    

#     print('Chances esgotadas')       
#     print(f'''
#              PLACAR
# ----------------------------------             
# seus pontos{meus_pontos}
# pontos da maquina {pontas_maquina} 
# ----------------------------------

# ''')     



# escolha =  input('Deseja acessar o sistema?')


# while escolha == 'sim'.upper():
#     print('Seja bem vindo ao sistema')
#     dado = input('Dado: ')
#     l.append(dado)
#     print(l)
#     escolha =  input('Deseja CONTINUAR?')
# else:
#     print('obrigada volte sempre')   



#  1 - Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.

# c = 0

# while c <= 1000:
# #      c = c + 1 
#       print(c)
#       c = c + 1 
      
#  2 -  Faça um sistema, utilizando while e listas, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

# Contador = 0
# lista_nome = []

# while Contador <= 9:
#       nome = (input('digite nome: '))
#       lista_nome.append(nome) 
#       Contador = Contador + 1 
# print('total de nomes', lista_nome) 





#  Crie um sistema de notas alunos, com as seguintes operações:
#  Utilize While ou for 



###outra maneira




# notas  = []
# while True:


#     chances = 3


#     for chance  in range(chances):


        
#         p  =  input('Deseja registrar notas? ')
#         while p == 'sim':
#             login = input('Usuario: ')
#             senha =  input('Senha: ') 
#             if login == 'bea' and senha == '123':
#                 print('Seja bem vindo sistema de notas')
#                 nota1 = float(input('Nota: '))
#                 nota2 = float(input('Nota: '))
#                 nota3 = float(input('Nota: '))
#                 notas.extend([nota1, nota2, nota3])
#                 media  =  sum(notas)/len(notas)
#                 print('Média', media)
#                 if media >= 7:
#                     print('Aprovado')
#                 elif media >= 5 and media <= 6:
#                     print('Recuperação') 
#                 else:
#                     print('Reprovado')        


#                 p = input('Deseja continuar? ')
#             else:
#                 print('senha incorreta... ')    
#     else:   
#         print('SENHA BLOQUEADA ... ')        
   




#     input('Clique enter para sair....')


##  outro  conteudo


# reconhecendo msg de erro

# try:
#     n  =  float(input('>>>'))
#     c =  n + 10
#     x  =  [1,2,3]
#     print(x[5])



# except ValueError as erro:
#     print(erro)    
# except TypeError as erro:
#     print(erro)
# except IndexError as erro:
#     print(erro)    
# else:
#     print('erro não identificado')
# finally:
#     print('Fim de carregamento ....')



try:
    n  =  int(input())
    c =   n + 10
    x  =  [1,2,3]
    print(x[5])