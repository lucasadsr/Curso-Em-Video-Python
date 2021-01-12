'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistarao serviço militar, se é a hora de se alistaroe se jpa passou o tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que já passoudo prazo.'''

from datetime import date
ano = date.today().year
nasc = int(input('Digite o ano de seu nascimento: '))
idade = ano - nasc
if idade < 18:
    print(f'Você ainda vai se alistar daqui a {18 - idade} anos')
elif idade > 18:
    print(f'Você passou do tempo de se alistar({idade - 18} anos)')
else:
    print('Está na hora de se alistar')
