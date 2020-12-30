'''Desenvolva um programa que pergunte a deistância de uma viagem em Km. Calcule o preço sa passagem. Cobrando R$0.50 por Km para viagens de até 200Km e 0.45 para viagens mais longas.'''

dist = float(input('Qual a distância da viagem? KM'))
if dist > 200:
    print(f'O preço da passagem é de: R${dist * 0.45}')
else:
    print(f'O preço da passgem é de: R${dist * 0.5}')