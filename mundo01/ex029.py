'''Escreva um programa queleia a velocidade de um carro.
Se ele ultrapassar 80KM/h, mostre um mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = float(input('Qual a sua velocidade atual? KM/H'))
multa = float(velocidade-80)*7
if velocidade>80:
    print('Você foi multado!\n'
          f'Valor: R${multa:.2f}')
else:
    print('Velocidade permitida')