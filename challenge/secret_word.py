'''
Make a game for the user to guess the secret word.
- You will propose any secret word and will give the possibility for the user to type only one letter.
- When the user types a letter, you will check if the typed letter is in the secret word.
 1-if the typed letter is in the secret word; display the letter;
 2-If the typed letter is not in the secret word; display *
Make the attempt count of your user
-------------------------------------------------------------------------------------------------------
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuario digitar apenas uma letra.
- Quando o usuario digitarr uma letra, você vai conferir se a letra digitada está na palavra secreta.
 1-se a letra digitada estiver na palavra secreta; exiiba a letra;
 2-Se a letra digitada não estiver na palavra secreta; exiba *
Faça a contagem de tentativa do seu usuario
'''
palavra_selecionada = str(input('Digite uma palavra: ')).upper()
cont = palavra_selecionada
letras_acertadas = ''
tentativa = 0
while True:
    palavra = str(input(f'\nTente adivinha qual palavra é com uma letra: ')).strip().upper()[0]
    tentativa += 1
    for letra in palavra_selecionada:
        palavra_certa = letra
        cont += ''
    if palavra in cont:
        letras_acertadas += palavra
    
    palavra_formada = ''
    for letra in palavra_selecionada:
        if letra in letras_acertadas:
            palavra_formada+= letra
        else:
            palavra_formada += "*"
    
    print('Palavra formada', palavra_formada)

    if palavra_formada == palavra_selecionada:
        print('Você Ganhou!!')
        print('A palavra  era', palavra_formada)
        print('Tentativas:', tentativa)
        break
    
            
            

    

    