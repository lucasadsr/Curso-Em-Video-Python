'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do aumento.
Para salários superiores à R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''

sal = float(input('Qual o seu salário? R$'))
if sal > 1250:
    print(f'Com um aumento de 10%, seu novo salário será de: R${sal * 1.1:.2f}')
else:
    print(f'Com um aumento de 15%, seu novo salário será de: R${sal * 1.15:.2f}')
