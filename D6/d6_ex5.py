from random import choice
from time import sleep
import sys

def define_possibilidades():
    return ['pedra', 'papel', 'tesoura']

def computador_joga(possibilidades):
    return choice(possibilidades)

def jogador_joga(possibilidades):
    print('Escolha sua jogada abaixo: ')
    print('[1] - Pedra')
    print('[2] - Papel')
    print('[3] - Tesoura')
    jogada = ''
    while jogada not in possibilidades:
        escolha = input('Opção: ')
        while escolha not in ['1', '2', '3']:
            escolha = input('Algo deu errado. Tente novamente. Digite um número entre 1 e 3: ')
        jogada = possibilidades[int(escolha) - 1]

    return jogada

def define_vencedor(computador, jogador):
    sleep(1)
    print(f'O computador escolheu {computador}')
    sleep(1)
    print(f'Você escolheu {jogador}')
    sleep(1)
    if computador == jogador:
        print(f'{jogador} é igual a {computador} - deu empate!')
    else:
        if computador == 'pedra' and jogador == 'papel' \
            or computador == 'papel' and jogador == 'tesoura' \
                or computador == 'tesoura' and jogador == 'pedra':
            print(f"{jogador} ganha de {computador} - você venceu!")
        else:
            print(f"{computador} ganha de {jogador} - o computador venceu!")

def quer_jogar_de_novo():
    jogar_de_novo = ''
    while jogar_de_novo not in ['S', 'N']:
        jogar_de_novo = input('Você quer jogar novamente? Digite "S" se sim e "N" se não: ')

def jogo():
    possibilidades = define_possibilidades()
    jogada_computador = computador_joga(possibilidades)
    jogada_jogador = jogador_joga(possibilidades)
    define_vencedor(jogada_computador, jogada_jogador)
    jogar_de_novo = ''
    while jogar_de_novo not in ['S', 'N']:
        jogar_de_novo = input('Você quer jogar novamente? Digite "S" se sim e "N" se não: ')
    if jogar_de_novo == 'S':
        jogo()
    else:
        print('Obrigado por jogar. Nos vemos na próxima!')
        sys.exit()


jogo()