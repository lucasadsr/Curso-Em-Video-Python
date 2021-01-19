'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a digitação novamente até ter uym valor correto.'''

sexo = str(input('DIGITE SEU SEXO M/F: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('DADOS INVÁLIDOS, DIGITE SEU SEXO M/F: ').upper())
print('okay.')
