'''Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
adivinhar = int(input('Em que número entre 0 e 10 eu pensei? '))
lrandom = randint(0, 10)
tentativas = 0

while adivinhar != lrandom:
    adivinhar = int(input('Você errou, tente novamente: '))
    tentativas += 1

if lrandom == adivinhar:
    print('Parabéns você acertou :)')
else:
    print('Você errou :(\n'
          f'O número em que pensei foi: {lrandom}')

print(f'Você precisou de {tentativas + 1} tentativas para acertar.')
