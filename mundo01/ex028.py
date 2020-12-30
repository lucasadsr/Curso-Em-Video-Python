'''Escreva uim programa que faça o computador pensar em número inteiroentre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu'''

from random import randint
adivinhar = int(input('Em que número entre 0 e 5 eu pensei? '))
lrandom = randint(0, 5)
if lrandom == adivinhar:
    print('Parabéns você acertou :)')
else:
    print('Você errou :(\n'
          f'O número em que pensei foi: {lrandom}')
