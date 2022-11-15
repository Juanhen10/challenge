''' Calculadora com while '''
while True:
    num1=  (input('Digite um número: '))
    num2 = (input('Digite outro número: '))
    op = input('Digite o operador (+-/*): ')
    
    numeros_validos = None
    try:
        num_float1 = float(num1)
        num_float2 = float(num2)
        numeros_validos = True
    except Exception as error:
        numeros_validos = None

    if numeros_validos is None:
        print('Números invalidos.')
        continue
    
    operadores_permitidos = '+-/*'

    if op not in operadores_permitidos:
        print('operador invalido')
        continue
    if len(op) > 1:
        print('digite apenas um operador.')
        continue

    if op == '+':
        soma = num_float1 + num_float2
        print(f'as somas dos números é \033[32m{soma}\033[m')
    elif op == '-':
        sub = num_float1 - num_float2
        print(f'subtração dos número é \033[31m{sub}\033[m')
    elif op == '/':
        div = num_float1 / num_float2
        print(f'A divisão dos números é \033[32m{div}\033[m')
    elif op == '*':
        mult = num_float1 * num_float2
        print(f'A mutiplicação dos número é \033[31m{mult}\033[m ')
    else:
        print('Não deve chegar aqui')

    while True:
        resp = str(input('Quer continuar?[s/n]: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Escreva S/N: ')
    if resp == 'N':
        print('volte sempre')
        break
        
     