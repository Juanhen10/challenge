'''
faça uma lista de compras com lista. 
O usuario deve ter a possiblidade de inserir, apagar e listar valores da sua lista. 
Não prmita que o programa quebre  com erros de índices inexistentes na lista.
-----------------------------------------------------------------------------------

make a shopping list with list. 
The user must be able to insert, delete and list values 
from his list. 
Don't allow the program to break with errors for non-existent indexes in the list.
'''
lista_compras = []
while True:
    try:
        print(f'\n[1] - adicionar item da sua lista' 
        f'\n[2] - apagar item da lista'
        f'\n[3] - listar valores'
        f'\n[4] - para sair') 
        p = int(input('qual opção: '))
        if p == 1:
            item = str(input('O que você deseja adicionar: '))
            lista_compras.append(item)
            print('item adicionado')

        elif p == 2:
            for i,p in enumerate(lista_compras):
                print(f'{i}', p)
            remove = int(input('Qual item você quer remover(coloque o número): '))
            for i,p in enumerate(lista_compras): 
                if remove == i:
                    lista_compras.pop(i)
                    print('item removido!')
                else:
                    print('Não exite esse item.')
                    
        elif p == 3:
            print(f'itens no carrinho.')
            for p, i in enumerate(lista_compras):
                print(f'{p}----{i}')
        elif p == 4:
            print('obrigado, volte sempre')
            break
        else:
            print('Coloque o valor 1,2,3 ou 4.')
    except ValueError:
        print('Digite uma das opções ou aperte 4 para sair!'):
        ...
        
