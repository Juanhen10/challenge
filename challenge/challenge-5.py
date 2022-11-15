print(f'\033[32m-'*50)
print('\033[32m------- Desafio 5-1 / Challenge 5-1 --------')
print(f'\033[32m-'*50)
#challenge 5-1
'''
faça um programa que peça ao ususario para digitar um número inteiro
informe se este número é par ou impar. 
Caso o usuario não digite um número inteiro,
informe que não é um inteiro  
--------------------------------------------------------------------
Write a program that asks the user to enter an integer. 
Indicate whether this number is even or odd.
If the user does not enter an integer, inform that is not an interger
'''
try:
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        print(f'Esses número -->{numero}<-- é par')
    else:
        print(f'Esse número -->{numero}<-- é impar')
except ValueError:
    print('Esse número não é inteiro')

#challenge 5-2
print(f'\033[31m-'*50)
print('------- Desafio 5-2 / Challenge 5-2 --------')
print('-'*50)
'''
faça um programa que pergunte a hora ao usuario e, basendo-se no horário descrito, 
exiba a saudação apropriada.
Ex.
Bom dia 0-11, Boa tarde 12-18 e Boa noite 18-23
----------------------------------------------------------------------
Write a program that ask the user for the time and based on the time described displays the appropriate greeting
EX
Good morning 0-11 am, Good afternoon 12-18 am, Good night 18-23
'''

horas = float(input('Que horas são : '))
if horas >= 12.00 and horas <= 17.59:
    print(f'Boa tarde, agora são {horas:.2f} horas da tarde ') 
if horas <= 11.59:
    print(f'Bom dia, agora são {horas:.2f} horas da manhã')
if horas >=18.00 and horas <= 23.59 :
    print(f'Boa noite, agora são {horas:.2f} horas da noite')

#challenge 5-3
print(f'\033[33m-'*50)
print('------- Desafio 5-3 / Challenge 5-3 --------')
print('-'*50)
'''
Faça um programa que peça o primeiro nome do usuario, 
Se o nome tiver 4 letras ou menos "Seu nome é curto";
Se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
------------------------------------------------------------------------
Write a program that ask the first name of user, if the name have 4 letters or less "Your name is short;
if have in 5 and 6 letters, write "your name is normal"; 
if more 6 letters write "your name is very big"
'''
nome = str(input('Qual seu primeiro nome: '))
c = len(nome)
if c <= 3:
    print('Seu nome é muito curto')
if c == 5 or c <=6:
    print('seu nome é normal')
else:
    print('seu nome é muito grande')
