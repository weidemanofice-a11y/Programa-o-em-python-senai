

# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

# try:
#     n1  =  int(input('nº: '))
#     n2  =  int(input('nº: '))
#     n1 / n2
#     l = [1,2,3]
#     print(l[n1])


# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

# except   ZeroDivisionError as erro:
#     print(erro)


# except IndexError as erro:
#     print(erro)    


# except ValueError as erro: 
#     print(erro)  

# Exercício 3:
# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).    


# try:
#     n1  =  int(input('nº: '))
#     n2  =  int(input('nº: '))
#     n1 / n2
#     l = [1,2,3]
#     print(l[n1])





# 4  tipos de dados primitivos


# str int float bool


# estruturas de dados 
# guardando dados na memoria ram(mutavel do pc )


# v =  12
# lis = [1,2,3]
# tupla = (12,3)
# conj =  {1,2,3}
# dicio = {'a':10, 'a':5}




# estruturas de fluxo de controle 
# repetições e toma decisões 




# if else elif 
# for 
# while 
# match
# try
# del 


# ------------------------------


# funções


# 3
# funções imbutidas na linguagem  -  print () input() len() ...
# bibliotecas externas pandas numpy tensorflow 
# da sua criação


# # definition -  incapsulamento e  organização
# def nome(): 
#     print('teste')
    
# nome()




# 4  tipos de dados primitivos


# str int float bool


# estruturas de dados 
# guardando dados na memoria ram(mutavel do pc )


# v =  12
# lis = [1,2,3]
# tupla = (12,3)
# conj =  {1,2,3}
# dicio = {'a':10, 'a':5}




# estruturas de fluxo de controle 
# repetições e toma decisões 




# if else elif 
# for 
# while 
# match
# try
# del 


# ------------------------------


# funções


# 3
# funções imbutidas na linguagem  -  print () input() len() ...
# bibliotecas externas pandas numpy tensorflow 
# da sua criação


# # definition -  incapsulamento e  organização
# def nome(): 
#     print('teste')
    


# nome()



#==================================


# def cadastro(quantidade, nomes, idades):
#     for x in range(quantidade):
#         nome = input('nome: ')
#         idade  = input('idade: ')
#         nomes.append(nome)
#         idades.append(idade)
#     return nomes, idades,
    


# def reservas():
#     lista_quartos = ['', "Simples", "Duplo" , "Luxo"]
#     valores  =  [0,100.0,150.0,250.0]
#     print(lista_quartos)
#     print(valores)
#     escolha  =  int(input('Escolha quarto >>>'))
#     quantidade_dias = int(input('Quantidade de dias:  '))
#     print(escolha)
#     c =  quantidade_dias * valores[escolha]
#     print('R$', c)
#     l =  ['','pix','cc','cd']
#     print(l)
#     formapag =  int(input('digite a forma de pagamento: '))
   
#     print(l[formapag]) 
#     print('Obrigada volte sempre!')
    


# def hotel_main():    

#     nomes = []
#     idades = []
#     q =  int(input('Digite a quantidade de pessoas: '))
#     dados_nomes, dados_idade = cadastro(q,nomes, idades)
#     quantidade_pessoas = len(dados_nomes)
#     print('quantidade de pessoas:', quantidade_pessoas)
#     for n in range(quantidade_pessoas):
#         print(f'Reserva do cliente {dados_nomes[n]}')
#         reservas()


# hotel_main()    

    


# CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***

# def soma(): 
#     n1 = int(input('Numero 1:  '))
#     n2 = int(input('Numero 2:  '))
#     if n1 % 2 == 0:
#        print('numero 1 é par', n1)
#     else:
#        print('numero 1 é impar', n1)     
#     if n2 % 2 == 0:
#        print('numero 2 é par', n2)
#     else:
#        print('numero 2 é impar', n2)     

# soma() 


#  CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.



#  ***CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.***

# def soma(): 
#     n1 = int(input('Numero 1:  '))
#     soma  = n1 ** 2
#     print('elevado a dois: ', soma)

# soma()    

# CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.

# def soma(): 
#     n1 = int(input('digite sua idade:  '))
#     if n1 == 18:
#        print('quem te esta idade já pode trabalhar: ', n1)
#     else:
#        print('ok, boa idade: ', n1)

# soma()    


# DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.

def idade(): 
    n1 = int(input('ano que nasceu:  '))
    idade = 2026 - n1
    print('Sua idade é: ', idade, 'anos' )
idade()    


