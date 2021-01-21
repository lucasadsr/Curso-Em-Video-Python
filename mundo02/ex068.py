'''Faça um programa que joga par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
print('PAR OU IMPAR')
print('-=' * 15)
iar = 0
while True:
    num = int(input('Escolha um valor: '))
    opcao = str(input('PAR OU IMPAR? [P/I] ')).upper().strip()
    pc = randint(0, 11)
    total = pc + num
    par = total % 2 == 0
    impar = total % 2 != 0
    print(f'Você escolheu {num} e o computador {pc}')
    print('-=' * 15)
    if opcao == 'P' and par:
        print('Você venceu!')
        iar += 1
    elif opcao == 'I' and impar:
        print('Você venceu!')
        iar += 1
    else:
        print('Você Perdeu')
        break
print(f'Você venceu {iar} vezes consecutivas')
