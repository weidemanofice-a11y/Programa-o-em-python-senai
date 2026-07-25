# # ESTRUTURAS DE DADOS 4  TIPOS DE DADOS PRIMITIVOS
# # PALAVRA = 


# variaveis  =  10 
# lista  =  [1,2,3]
# tuplas =  (1,2,3,6)
# conjuntos  = {1,2,3,6}



# e-commerce 


# loja = {


#     'livros':{
#             'a':100.0,
#             'b':250.0,
#             'c':315.55
#         },
#     'tablets':{
#             'a': 1500.0,
#             'b':3500.0,
#             'c':5000.0
#     },
#     'fones':{
#             'x': 350.0,
#             'y':250.0,
#             'z':1500.0,
#     }


# }




# carrinho = []
# valores  = []



# print('Bem vindo(a) a loja xyz')


# se1 = input(f'Seção do produto {loja.keys()} >>')
# prod1 = input(f'Escolha o produto: {loja[se1]} ')


# carrinho.append(prod1)
# valores.append(loja[se1][prod1])


# se2 = input(f'Seção do produto {loja.keys()}>>')
# prod2 = input(f'Escolha o produto: {loja[se2]}')


# carrinho.append(prod2)
# p = loja[se2][prod2]
# valores.append(p)


# print('Carrinho  de compras: ', carrinho)
# print('Total', sum(valores))



# pag = input('escolha a forma de pagamento: pix, cc, cd')
# print('Sua forma de pagamento é', pag)
# print('Obrigada volte sempre! ')


# estruturas de fluxo de controle 



# estruturas de fluxo de controle 


# if condição == Verdade(True):
#     vai fazer isso
 


# numero = int(input('nº: '))


# if numero > 0 :
#    print('positivo')
# elif numero < 0:
#    print('negativo')   
# else:
#    print('zero')



# re =  (numero > 0 and ('posiitvo') or (numero < 0 and ('negativo')) or ('zero'))   
# print(re)


# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.

# idade = int(input('Informe a sua idade: '))
# if idade >= 16:
#   if idade >= 18:
#     print('Voto Obrigatório')
#   else:
#     print('Voto Opcional')
# else:
#   print('Não pode votar')



# 3*

# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.

# numero = int(input('digite um numero: '))

# if numero % 2 == 0:
#     print("O número não é par.")
# else:
#     print("O número impar.")



# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.



# numero1 = int(input('digite um numero 1: '))
# numero2 = int(input('digite um numero 2: '))
# numero3 = int(input('digite um numero 3: '))

# if numero1 == numero2  == numero3:
#     print("equiláter.")
# elif numero1 == numero2 !=  numero3 or numero1 == numero3 !=  numero2: 
#     print("isósceles.")   
# else:
#    if numero1 != numero2 !=  numero3:
#       print("escaleno.")



# 5*

	# Determine se um número é múltiplo de 5 e 7.

# numero = int(input('digite um numero: '))

# resultado = numero / 5 
   
# # if numero % 5 == 0:
# if numero % 5 :
#     print("mutiplo de 5. ")
# # elif (numero * 7) and % 2 == 0:
# #     print("mutiplo de 7. ")
# # else:
# #     print("O número impar.")

# 6*

# Verifique se um número é positivo e maior que 10

# numero = int(input('numero: '))
# if numero > 0:
#   if numero >= 11:
#     print('positivo mior que 10')
#   else:
#     print('positivo menor ou igual a 10')
# else:
#   print('Negativo')


# 7*

# Verifique se um número é divisível por 3 ou 5.

   
numero = int(input('digite um numero: '))

resultado = (numero * 3)


print(resultado)


# if (numero * 3) and numero % == 0:
#     print("mutiplo de 3. ")


# if numero % 5 :
#     print("mutiplo de 5. ")
# elif (numero * 7) and % 2 == 0:
#     print("mutiplo de 7. ")
# else:
#     print("O número impar.")

# 6*