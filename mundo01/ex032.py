'''Faça um programa que eia um ano qualquer e mostre se ele é bissexto.'''
ano = int(input('ANO: '))
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('O ano é bissexto')
else:
    print('Ano comum')