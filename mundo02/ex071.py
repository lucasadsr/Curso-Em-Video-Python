'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considera que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('=' * 10)
print('BANCO 24/7')
print('=' * 10)

valor = int(input('digite o valor a ser sacado: R$'))
cedulas = 0
valorcedula = 50

while True:
    if valor >= valorcedula:
        valor -= valorcedula
        cedulas += 1
    else:
        if cedulas > 0:
            print(f'Você vai receber {cedulas} cedulas de R${valorcedula}.')
        if valorcedula == 50:
            valorcedula = 20
        elif valorcedula == 20:
            valorcedula = 10
        elif valorcedula == 10:
            valorcedula = 1
        cedulas = 0
        if valor == 0:
            break
