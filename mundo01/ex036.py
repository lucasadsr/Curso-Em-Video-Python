'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar '''

valor_casa = int(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor de seu salário? R$'))
anos = int(input('Em quantos anos deseja pagar? '))
mensalidade = valor_casa / (anos * 12)

if mensalidade < salario * 0.3:
    print(f'O valor das mensalidade é de: R${mensalidade:.2f}')
else:
    print('O empréstimo foi negado!')
