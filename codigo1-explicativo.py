# _*_ coding: utf-8 _*_
__author__ = "Tulio Dias"
__copyright__ = "Copyright 2019, Túlio Vilela Dias"
__credits__ = "Túlio"
__license__ = "MIT"
__maintainer__ = "Tulio Dias"
__email__ = "tuliovilela7@hotmail.com"

####################################################################################################
#################
## COMENTÁRIOS ##
#################
# Comentários são trechos do código que não serão executados, servem apenas para orientar sobre algo.
# Um comentário em python começa com '#' ou entre 3 aspas simples '''comentário2'''
# Olá, eu sou um COMENTÁRIO.


####################################################################################################
###############
## Variáveis ##
###############
# Variáveis são utilizadas para atribuir algum valor. Elas podem ser alteradas a qualquer momento
# Na maioria das linguagens é necessário declarar o tipo da variável anteriormente, já no Python não.
variavel1 = "Aba"
variavel2 = "caxi"
variavel3 = 100
variavel4 = 200

variavel12 = variavel1 + variavel2
variavel34 = variavel3 + variavel4

print(variavel1)
print(variavel2)
print(variavel3)
print(variavel4)
print(variavel12)
print(variavel34)

####################################################################################################
###########################
## Estrutura Condicional ##
###########################
# Estruturas condicionais são utilizadas para exercer condições ao código.
# Ou seja, se acontecer algo, então faça algo.
variavel_teste = 100
if(variavel_teste < 100): #SE ...
    print("A variavel é menor que 100.")

elif(variavel_teste == 100): #SENÃO SE...
    print("A variavel é igual a 100")

else: #SENÃO
    print("A variável é maior que 100")

# Abaixo, seguem algumas condições comparativas:
# >   : Maior
# >=  : Maior Igual
# <   : Menor
# <=  : Menor Igual
# ==  : Igual
# !=  : Diferente
# ||  : OU
# &&  : E

####################################################################################################
###########################
## Estrutura Condicional ##
###########################
#Repetições são loops para fazer algo até que seja atendido uma condição

for i in range(10): #Utilizando o for (percorrer por algo...)
    print(i)

x=0
while(x<=5): #Repetição utilizando while (enquanto algo...)
    print(x)
    x = x+1

####################################################################################################
#############
## Funções ##
#############
# Utilizamos funções para preparar para alguma rotina sempre que chamá-la. 
# Estas funções podem receber e devolver valores, vejamos os exemplos a seguir
# Utilizamos "def" para iniciar uma função

def valor_de_pi(): #Função que devolve um valor
    return 3.14159265359

def mes(mes): #Função que recebe um valor
    if(mes==1):
        return "Janeiro"
    elif(mes==2):
        return "Fevereiro"
    elif(mes==3):
        return "Março"
    elif(mes==4):
        return "Abril"
    elif(mes==5):
        return "Maio"
    else:
        return "Ops, só sei até Maio"

teste_funcao1 = valor_de_pi()
teste_funcao2 = mes(5)

print(teste_funcao1)
print(teste_funcao2)