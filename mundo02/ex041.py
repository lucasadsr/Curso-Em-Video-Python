'''A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
-Até 9 anos: MIRIM
-Até 14 anos: INFANTIL
-Até 19 anos: JUNIOR
-Até 25 anos: SÊNIOR
-Acima: MASTER'''

from datetime import date
ano = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = ano - nasc
print(f'Você tem {idade} ano(s).')
if idade <= 9:
    print('Você é MIRIM.')
elif 10 <= idade <= 14:
    print('você é INFANTIL.')
elif 15 <= idade <=19:
    print('Você é JUNIOR.')
elif 20 == idade:
    print('Você é SÊNIOR.')
else:
    print('Você é MASTER.')