'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTO'''

cidade = input('Digite o nome da cidade: ').strip()
cidadesplit = cidade.split()[0]
cidadeup = cidadesplit.upper()
cidadefind = 'SANTO' in cidadeup
print(cidadefind)
