"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue    # volta em Digite uma letra

    if letra_digitada in palavra_secreta:    # teste letra digitada estiver em palavra secreta
        letras_acertadas += letra_digitada    # letra acertadas armazena a letra

    palavra_formada = ''
    for letra_secreta in palavra_secreta:    # letra secreta percorre a plavra secreta letra por letra
        if letra_secreta in letras_acertadas:    # testa letra por letra percorrida pelo for
            palavra_formada += letra_secreta    # palavra formada
        else:
            palavra_formada += '*'    # letra errada

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0