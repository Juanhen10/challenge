#exercicio-4
'''
Peça ao usuario para digitar seu nome 
Peça ao usuario para digitar sua idade
Se nome e idade forem digitados, Exiba:
        Seu nome
        Seu nome invertido
        A primeira letra do seu nome 
        A ultima letra do seu nome 
------------------------------------------
Ask the user to enter their name
Ask the user to enter their age
If name and age are entered, Display:
        Your name
        Your name inverted
        The first letter of your name
        The last letter of your name
'''
nome = str(input('Nome:'))
idade = input('Idade:')
if nome == '' and idade == '':
    print(f'os campos estão vazios!')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[3]}')
