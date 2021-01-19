'''Crie um programa que leia dois valores e mostre um menu como o ao lado na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
opção = ''
maior = 0

while opção != 5:
    opção = int(input('''ESCOLHA UMA OPÇÃO
    [ 1 ]SOMAR
    [ 2 ]MULTIPLICAR
    [ 3 ]MAIOR
    [ 4 ]NOVOS NÚMEROS
    [ 5 ]SAIR DO PROGRAMA
    ESCOLHA: '''))
    print('=-' * 15)
    if opção == 1:
        print(f'A soma de de {n1} + {n2} é: {n1 + n2}')
        print('=-' * 15)
    elif opção == 2:
        print(f'O produto de {n1} X {n2} é: {n1 * n2}')
        print('=-' * 15)
    elif opção == 3:
        if n1 > n2:
            maior += n1
            print(f'O maior número é {maior}')
            print('=-' * 15)
        else:
            maior += n2
            print(f'O maior número é {maior}')
            print('=-' * 15)
    elif opção == 4:
        n1 = float(input('Digite um novo número: '))
        n2 = float(input('Digite outro novo número: '))
    elif opção > 5 or opção < 1:
        print('Opção Inválida! Tente novamente.')
if opção == 5:
    print('Programa finalizado!')
