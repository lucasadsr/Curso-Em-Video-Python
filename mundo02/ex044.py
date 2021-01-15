'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
-À vista dinheiro/cheque: 10% de desconto
-À vista no cartão: 5% de desconto
-Em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros'''

preçoinicial = float(input('Digite o preço do produto: R$'))
pagamento = int(input('''QUAL O MÉTODO DE PAGAMENTO?
[1]A VISTA NO DINHEIRO/CHEQUE
[2]A VISTA NO CARTÃO
[3]ATÉ 2 VEZES NO CARTÃO
[4]3 VEZES OU MAIS NO CARTAO
'''))

if pagamento == 1:
    preçofinal = preçoinicial - (preçoinicial * 0.1)
elif pagamento == 2:
    preçofinal = preçoinicial - (preçoinicial * 0.05)
elif pagamento == 3:
    preçofinal = preçoinicial
elif pagamento == 4:
    preçofinal = preçoinicial + (preçoinicial * 0.2)
else:
    print('ALTERNATIVA INVÁLIDA')

print(f'O preço do produto com o método de pagamento {pagamento} ficará por R${preçofinal:.2f}')